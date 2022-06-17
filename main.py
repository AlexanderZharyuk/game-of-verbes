import os
import logging

from dotenv import load_dotenv
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from google.cloud import dialogflow


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)


def detect_intent_texts(project_id, session_id, texts, language_code):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(request={"session": session, "query_input": query_input})

        return response.query_result.fulfillment_text


async def start(update: Update, context: ContextTypes) -> None:
    await update.message.reply_html(rf"Здравствуйте!")


async def user_greeting(update: Update, context: ContextTypes) -> None:
    app_id = os.environ['GOOGLE_PROJECT_ID']
    user_id = update.message.from_user.id
    message = update.message.text.split()
    bot_text = detect_intent_texts(app_id, user_id, message, 'ru')

    await update.message.reply_text(bot_text)


def main() -> None:
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    application = Application.builder().token(telegram_token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, user_greeting))
    application.run_polling()


if __name__ == '__main__':
    main()
