# Discord chat Analysis


## About Project
The user can use this tool to analyse and monitor the channel's chat real time,like the sentiment of the chats and filter out a specific message based on it's sentiment value or toxicity.
The project is built using Django Web Framework.

## Before runnig the project
1. Go to file `discord_bot.py` and copy your Bot Token from discord developer page.

2. Go to file `dashboard\app\api\expertai_api.py` and enter your password and username for the ExpertAi NLAPI.

## How to run the project 

1. clone the repo to your local machine
2. create a python virtual environment
3. install the required depdencies using `requirements.txt`
4. got to dashboard folder and start server using `python manage.py runserver`
4. open a second terminal and start run `discord_bot.py` for our Discord Bot

