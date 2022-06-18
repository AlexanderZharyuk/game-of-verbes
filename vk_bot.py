import os
import random
import time
import logging

import vk_api
import telegram

from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType

from dialog_flow_functions import detect_intent_texts


logger = logging.getLogger('Logger')


class BotLogger(logging.Handler):

    def __init__(self, bot, chat_id):
        super().__init__()
        self.bot = bot
        self.chat_id = chat_id

    def emit(self, record):
        log_entry = self.format(record)
        self.bot.send_message(text=log_entry, chat_id=self.chat_id)


def reply_to_user(event, vk_api):
    app_id = os.environ['GOOGLE_PROJECT_ID']
    answer_to_user = detect_intent_texts(app_id, event.user_id, event.text.split(), 'ru')

    if answer_to_user:
        vk_api.messages.send(
            user_id=event.user_id,
            message=answer_to_user,
            random_id=random.randint(1, 1000)
        )


if __name__ == '__main__':
    load_dotenv()
    vk_token = os.environ['VK_TOKEN']
    tg_token = os.environ['INFO_VK_BOT_TOKEN']
    admin_chat_id = os.environ['CHAT_ID']
    bot = telegram.Bot(tg_token)
    logger.setLevel(logging.INFO)
    logger.addHandler(BotLogger(bot, admin_chat_id))
    logger.info('🔥 Бот запущен!')

    vk_session = vk_api.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    while True:
        try:
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    reply_to_user(event, vk_api)
        except ConnectionError:
            logger.exception('Connection error, ухожу в сон на 1 минуту.')
            time.sleep(60)
            continue
        except Exception:
            logger.exception('Бот упал с ошибкой:')
            continue
