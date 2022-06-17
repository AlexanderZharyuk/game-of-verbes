import os
import json

from google.cloud import dialogflow
from dotenv import load_dotenv


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)

        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(display_name=display_name, training_phrases=training_phrases, messages=[message])

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    return response


if __name__ == '__main__':
    load_dotenv()
    project_id = os.environ['GOOGLE_PROJECT_ID']
    intent_display_name = 'Как устроиться к вам на работу'

    with open('questions.json', 'r') as json_file:
        answers_and_questions = json.load(json_file)

    employment_questions = answers_and_questions['Устройство на работу']['questions']
    employment_answer = answers_and_questions['Устройство на работу']['answer']

    create_intent(project_id, intent_display_name, employment_questions, [employment_answer])
