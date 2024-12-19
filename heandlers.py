import telebot

from keyboards import (create_consent_keyboard,
                       create_first_keyboard, create_second_keyboard,
                       create_salons_inline_keyboard,
                       create_specialits_inline_keyboard)


def read_price():
    with open('price1.txt', 'r', encoding='utf-8') as file:
        return file.read()

# Обработчик команды /start
def handle_start(bot: telebot.TeleBot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        with open('agreement.txt', 'rb') as file:
            bot.send_document(message.chat.id, file)
        bot.send_message(message.chat.id, "Для продолжения работы с ботом необходимо принять соглашение "
                                          "об обработке персональных данных."
                                        " Прочтите соглашение и нажмите кнопку 'Принять'.",
                                        reply_markup=create_consent_keyboard()
                         )

# обработчик стандартной клавиатуры
def handle_messages(bot: telebot.TeleBot):
    @bot.message_handler(func=lambda message: True)
    def handler_message(message):
        if message.text == "Хочу записаться по номеру телефона":
            bot.send_message(message.chat.id, "Для связи с администратором позвоните по номеру: +7 (123) 456-78-90")
        elif message.text == "Выбрать салон":
            bot.send_message(message.chat.id, "Далее вы можете узнать цены на процедуры или записаться по времени",
            reply_markup=create_second_keyboard())
        elif message.text == 'Прайс на процедуры':
            bot.send_message(message.chat.id, read_price())
        elif message.text == 'Назад':
            bot.send_message(message.chat.id, "Вы вернулись в Главное Меню",
                             reply_markup=create_first_keyboard())
        elif message.text == 'Наши салоны':
            bot.send_message(message.chat.id, "Выберите салон:",
                             reply_markup=create_salons_inline_keyboard())
        elif message.text == "Выбрать любимого специалиста":
            bot.send_message(message.chat.id, "Наши специалисты",
                             reply_markup=create_specialits_inline_keyboard())


print()
# Обработчик нажатий  инлайн-кнопки
def handle_callbacks(bot: telebot.TeleBot):
    @bot.callback_query_handler(func=lambda call: True)
    def handle_callback(call):
        if call.data == 'accept':
            bot.send_message(call.message.chat.id, "Спасибо! Вы приняли соглашение. Теперь вы можете продолжить.",
                             reply_markup=create_first_keyboard())
        elif call.data == 'reject':
            bot.send_message(call.message.chat.id,
                             "Вы не приняли соглашение. Для продолжения работы с ботом необходимо дать согласие.")