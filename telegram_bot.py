import os
import logging

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from dialog_flow_functions import detect_intent_texts


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes) -> None:
    await update.message.reply_html(rf"Здравствуйте!")


async def user_greeting(update: Update, context: ContextTypes) -> None:
    app_id = os.environ['GOOGLE_PROJECT_ID']
    user_id = update.message.from_user.id
    message = update.message.text
    bot_answer = detect_intent_texts(app_id, user_id, [message], 'ru')

    if bot_answer is not None:
        await update.message.reply_text(bot_answer)


def main() -> None:
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    application = Application.builder().token(telegram_token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, user_greeting))
    application.run_polling()


if __name__ == '__main__':
    main()
