import os
import random

import vk_api

from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType

from dialog_flow_functions import detect_intent_texts


def reply_to_user(event, vk_api):
    app_id = os.environ['GOOGLE_PROJECT_ID']
    answer_to_user = detect_intent_texts(app_id, event.user_id, event.text.split(), 'ru')

    if answer_to_user is not None:
        vk_api.messages.send(
            user_id=event.user_id,
            message=answer_to_user,
            random_id=random.randint(1, 1000)
        )


if __name__ == '__main__':
    load_dotenv()
    vk_token = os.environ['VK_TOKEN']
    vk_session = vk_api.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            reply_to_user(event, vk_api)
