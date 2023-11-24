import ptbot
import os
import dotenv
import pytimeparse

TGBOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
TG_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']


def progressbarplus(total, iteration, prefix='', suffix=' ', postsuffix='', length=20, fill='▓', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.2f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    progressbar = fill * filled_length + zfill * (length - filled_length)
    return f"{prefix}{progressbar}{suffix}{percent}%{postsuffix}"


def timer_start(chat_id, reply_text, bot):
    message_id = bot.send_message(chat_id, "Запускаю таймер...")
    bot.create_countdown(pytimeparse.parse(reply_text),
                         timer_count,
                         chat_id=chat_id,
                         message_id=message_id,
                         secs_total=pytimeparse.parse(reply_text),
                         bot=bot)
    bot.create_timer(pytimeparse.parse(reply_text),
                     timer_end,
                     chat_id=chat_id,
                     bot=bot)


def timer_count(secs_left, chat_id, message_id, secs_total, bot):
    bot.update_message(chat_id, message_id, f"Осталось {secs_left} сек.\n{progressbarplus(secs_total, secs_total-secs_left)}")


def timer_end(chat_id, bot):
    bot.send_message(chat_id, "Время вышло!")


def main():
    dotenv.load_dotenv()
    bot = ptbot.Bot(TGBOT_TOKEN)
    bot.send_message(TG_CHAT_ID, "Введите время (Например: 3s, 1m).")
    bot.reply_on_message(timer_start, bot=bot)
    bot.run_bot()


if __name__ == '__main__':
    main()
