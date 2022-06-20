import os
import time
import logging

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dialog_flow_functions import detect_intent_texts

from logger import BotLogger


logger = logging.getLogger('Logger')


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        f'Привет, {user.mention_markdown_v2()}\!',
    )


def bot_answer(update: Update, context: CallbackContext):
    app_id = os.environ['GOOGLE_PROJECT_ID']
    user_id = update.message.from_user.id
    message = update.message.text
    bot_answer, answer_is_fallback = detect_intent_texts(app_id, user_id, message, 'ru')

    update.message.reply_text(bot_answer)


if __name__ == '__main__':
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    admin_tg_chat_id = os.environ['ADMIN_TG_ID']
    updater = Updater(telegram_token, use_context=True)
    logger.setLevel(logging.INFO)
    logger.addHandler(BotLogger(updater.bot, admin_tg_chat_id))
    logger.info('🔥 Бот запущен!')

    try:
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=bot_answer))
    except ConnectionError:
        logger.exception('Connection error, ухожу в сон на 1 минуту.')
        time.sleep(60)
    except Exception:
        logger.exception('Бот упал с ошибкой:')

    updater.start_polling()
    updater.idle()
