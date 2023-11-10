import ptbot
import os
import dotenv
import pytimeparse

dotenv.load_dotenv()
TGBOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
TG_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
bot = ptbot.Bot(TGBOT_TOKEN)


def timer_start(chat_id, reply_text):
    bot.create_countdown(int(pytimeparse.parse(reply_text)), timer_count)
    bot.create_timer(int(pytimeparse.parse(reply_text)), timer_end)


def timer_count(secs_left, chat_id):
    bot.send_message(TG_CHAT_ID, f"Осталось {secs_left}")


def timer_end(chat_id):
    bot.send_message(TG_CHAT_ID, "Время вышло!")


bot.send_message(TG_CHAT_ID, "Введите время (Например: 3s, 1m).")
bot.reply_on_message(timer_start)
bot.run_bot()
