import ptbot
import os
from dotenv import load_dotenv
load_dotenv()
TGBOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
TG_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']


def timer_start(bot, chat_id):
    print("Мне написал пользователь с ID:", chat_id, ", начинаю таймер.")
    bot.create_timer(5, timer_end)


def timer_end():
    print("Прошло 5 секунд!")


def main():
    bot = ptbot.Bot(TGBOT_TOKEN)
    bot.send_message(TG_CHAT_ID, "Таймер запущен")
    bot.reply_on_message(timer_start, bot=bot, chat_id=chat_id)
    bot.run_bot()


if __name__ == '__main__':
    main()
