# Social Networks Support Bots 

Боты поддержки компании **Game Of Verbs**!

## О проекте

Боты созданы для облегчения работы персонала компании. Они обучены благодаря платформе [DialogFlow](https://dialogflow.cloud.google.com/). Со списком вопросов вы можете ознакомиться в файле `json/questions.json`.

Боты работают в [VK](https://vk.com/public213993013) и Telegram [@FiziqueGameOfVerbsBot]

Вы можете протестировать их работу сами или посмотреть как они работают ниже.

## Предустановка

Если вы хотите протестировать ботов или же использовать их в своих целях - вы можете использовать этот репозиторий для выполнения этих задач, для этого: 
1. Установите нобходимые библиотеки:
``` 
pip install -r requirements.txt
```
2. Создайте `.env` файл, в котором вы укажите ваши данные:
``` 
TELEGRAM_TOKEN={YOUR-TELEGRAM-SUPPORT-BOT}
INFO_VK_BOT_TOKEN={YOUR-TELEGRAM-BOT-TOKEN-THAT-CHECK-VK-BOT-STATUS}
GOOGLE_APPLICATION_CREDENTIALS={FILENAME-WITH-YOUR-CREDENTIALS.json}
GOOGLE_PROJECT_ID={YOUR-GOOGLE-PROJECT-ID}
VK_TOKEN={YOUR-VK-TOKEN}
ADMIN_TG_ID={YOUR-ID-IN-TELEGRAM}
QUESTIONS_FILE_NAME={YOUR-QUESTIONS-DATA.json}
```

3. Если вы хотите обучить бота новым ответам - заполните файл, имя которого указали в `.env` в переменной `QUESTIONS_FILE_NAME` нужными данными. 
В данном репозитории файл `json_files/questions.json`является шаблоном, вы можете заполнить его данными и указать его в `.env`.

Например:
```
QUESTIONS_FILE_NAME=questions.json
```

P.S.

json-файл с вашими GOOGLE-CREDENTIALS должен лежать там же, где и исполнительные файлы. Не сохраняйте его в других подпапках.

## Обучение ботов
После того, как вы заполнили файл `questions.json` или файл с вашим названием - обучите ботов ответам на фразы. Для этого используйте команду:

```
python3 dialog_flow_functions.py
```

## Запуск ботов
Все боты запускаются запуском отдельных файлов.
Команды для запуска ботов:

* Telegram-бот:
```
python3 telegram_bot.py

```
* VK-бот:
``` 
python3 vk_bot.py
```

### Примеры работы чат-ботов

<img src="https://github.com/AlexanderZharyuk/game-of-verbs/blob/main/repo_media/vk-bot-preview.gif?raw=true" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="400" height="220" />

<br>

<img src="https://github.com/AlexanderZharyuk/game-of-verbs/blob/main/repo_media/TG-preview.gif?raw=true" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="450" height="350" />


## Создано при помощи

* [DEVMAN](https://dvmn.org/) - Обучающая платформа
* [BITLY](https://bitly.com/) - Сервис по созданию коротких ссылок

## Авторы

* [Alexander Zharyuk](https://gist.github.com/AlexanderZharyuk)
