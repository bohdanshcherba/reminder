from datetime import datetime
import schedule
import time
import telebot
from config import config
from threading import Thread

import sys

# setting path
sys.path.append('../reminderBot')
from basa.basa import *

chat_id = 846592602
current_week = [WEEK_ALL, WEEK_B]


def check_cur_week():
    week_num = datetime.now().isocalendar()[1]

    if week_num % 2 == 0:
        current_week[1] = WEEK_B
    else:
        current_week[1] = WEEK_A


check_cur_week()

bot = telebot.TeleBot(config.bot_token)


@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, msg.chat.id)


def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)


def function_to_run():
    day = datetime.today().strftime("%A").lower()
    now_time = datetime.now().strftime("%H:%M")

    for subject in base:
        if subject[WEEK] in current_week and subject[DAY] == day and subject[TIME] == now_time:
            bot.send_message(chat_id, f'{subject[NAME]}\n'
                                      f'{subject[URL]}')
            return


schedule.every().monday.at('01:00').do(check_cur_week)
schedule.every().day.at(l1).do(function_to_run)
schedule.every().day.at(l2).do(function_to_run)
schedule.every().day.at(l3).do(function_to_run)
schedule.every().day.at(l4).do(function_to_run)
schedule.every().day.at(l5).do(function_to_run)

Thread(target=schedule_checker).start()

bot.polling(none_stop=True)
