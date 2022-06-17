import os
import logging

from dotenv import load_dotenv
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes) -> None:
    user = update.effective_user
    await update.message.reply_html(rf"Здравствуйте!")


async def echo(update: Update, context: ContextTypes) -> None:
    await update.message.reply_text(update.message.text)


def main() -> None:
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    application = Application.builder().token(telegram_token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling()


if __name__ == '__main__':
    main()
