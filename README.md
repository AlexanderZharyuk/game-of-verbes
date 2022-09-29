# Social Networks Support Bots

**Jardeko** company support bots!

## About the project

Bots are created to facilitate the work of the company's staff. They are trained by the [DialogFlow](https://dialogflow.cloud.google.com/) platform. You can find the list of questions in the `json/questions.json` file.

Bots work in VK and Telergam socials.

You can see how they work below.

## Get started

If you want to test bots or use them for your own purposes - you can use this repository to perform these tasks, for this:
1. Install the required libraries:
```
pip install -r requirements.txt
```
2. Create a `.env` file that contain your data:
```
TELEGRAM_TOKEN={YOUR-TELEGRAM-SUPPORT-BOT}
INFO_VK_BOT_TOKEN={YOUR-TELEGRAM-BOT-TOKEN-THAT-CHECK-VK-BOT-STATUS}
GOOGLE_APPLICATION_CREDENTIALS={FILENAME-WITH-YOUR-CREDENTIALS.json}
GOOGLE_PROJECT_ID={YOUR-GOOGLE-PROJECT-ID}
VK_TOKEN={YOUR-VK-TOKEN}
ADMIN_TG_ID={YOUR-ID-IN-TELEGRAM}
QUESTIONS_FILE_NAME={YOUR-QUESTIONS-DATA.json}
```

3. If you want to train the bot with new answers, fill in the file whose name is specified in `.env` in the `QUESTIONS_FILE_NAME` variable with the necessary data.
In this repository, the `json_files/questions.json` file is a template, you can fill it with data and specify it in `.env`.

For example:
```
QUESTIONS_FILE_NAME=questions.json
```

P.S.

json file with your GOOGLE-CREDENTIALS should be in the same place as the executable files. Do not save it in other subfolders.

## Bot training
After you have filled in the `questions.json` file or the file with your name, train the bots to answer the phrases. To do this, use the command:

```
python3 dialog_flow_functions.py
```

## Run bots
All bots are started by running separate files.
Commands for running bots:

* Telegram bot:
```
python3 telegram_bot.py
```
* VK-bot:
```
python3 vk_bot.py
```

### Examples of how chatbots work

<img src="https://github.com/AlexanderZharyuk/game-of-verbs/blob/main/repo_media/vk-bot-preview.gif?raw=true" data-canonical-src="https:// gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="400" height="220" />

<br>

<img src="https://github.com/AlexanderZharyuk/game-of-verbs/blob/main/repo_media/TG-preview.gif?raw=true" data-canonical-src="https://gyazo. com/eb5c5741b6a9a16c692170a41a49c858.png" width="450" height="350" />


## Created with

* [BITLY](https://bitly.com/) - Service for creating short links

## The authors

* [Alexander Zharyuk](https://gist.github.com/AlexanderZharyuk)
