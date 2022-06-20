import os
import random
import time
import logging

import vk_api
import telegram

from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType

from dialog_flow_functions import detect_intent_texts
from logger import BotLogger


logger = logging.getLogger('Logger')


def reply_to_user(event, vk_api):
    app_id = os.environ['GOOGLE_PROJECT_ID']
    bot_answer, answer_is_fallback = detect_intent_texts(app_id,  event.user_id, event.text, 'ru')

    if not answer_is_fallback:
        vk_api.messages.send(
            user_id=event.user_id,
            message=bot_answer,
            random_id=random.randint(1, 1000)
        )


if __name__ == '__main__':
    load_dotenv()
    vk_token = os.environ['VK_TOKEN']
    tg_token = os.environ['INFO_VK_BOT_TOKEN']
    admin_tg_chat_id = os.environ['ADMIN_TG_ID']
    bot = telegram.Bot(tg_token)
    logger.setLevel(logging.INFO)
    logger.addHandler(BotLogger(bot, admin_tg_chat_id))
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
