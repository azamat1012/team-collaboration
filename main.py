from dotenv import load_dotenv
import os
import telebot
from heandlers import handle_start, handle_messages, handle_callbacks


def main():
    load_dotenv()
    token_tg = os.environ['TG_TOKEN']#token#
    bot = telebot.TeleBot(token_tg)

    handle_start(bot)
    handle_messages(bot)
    handle_callbacks(bot)

    bot.polling()
print()

if __name__ == '__main__':
    main()