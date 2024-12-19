import telebot


def create_back_button():
    return telebot.types.KeyboardButton('Назад')


# создаем кнопки согласия на обработку персональных данных
def create_consent_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    assept_button = telebot.types.InlineKeyboardButton('Принять', callback_data='accept')
    reject_button = telebot.types.InlineKeyboardButton('Отклонить', callback_data='reject')
    keyboard.add(assept_button, reject_button)
    return keyboard


# Создаем первый набор кнопок
def create_first_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.KeyboardButton("Выбрать салон")
    button2 = telebot.types.KeyboardButton("Выбрать любимого специалиста")
    button3 = telebot.types.KeyboardButton("Хочу записаться по номеру телефона")

    keyboard.row(button1)
    keyboard.row(button2, button3)

    return keyboard

# Создаем второй набор кнопок
def create_second_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button5 = telebot.types.KeyboardButton("Прайс на процедуры")
    button6 = telebot.types.KeyboardButton("Запись по времени")
    button7 = telebot.types.KeyboardButton("Наши салоны")
    back_button = create_back_button()
    keyboard.row(button5, button6)
    keyboard.row(button7, back_button)

    return keyboard

#создаем инлайн кнопки
def create_salons_inline_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    salon_1 = telebot.types.InlineKeyboardButton('Кучерявая жизнь', callback_data='salon_1')
    salon_2 = telebot.types.InlineKeyboardButton('Штукатурка наше всё', callback_data='salon_2')
    salon_3 = telebot.types.InlineKeyboardButton('Толерантный Makeup', callback_data='salon_3')
    keyboard.row(salon_1)
    keyboard.row(salon_2)
    keyboard.row(salon_3)
    return keyboard

print()


def create_specialits_inline_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    master_1 = telebot.types.InlineKeyboardButton("Фёдор Сумкин. Окрашивание волос", callback_data='master_1')
    master_2 = telebot.types.InlineKeyboardButton("Сеня Ганжубас. Вечерниий макияж", callback_data='master_2')
    master_3 = telebot.types.InlineKeyboardButton("Арвен. Окрашивание волос", callback_data='master_3')
    master_4 = telebot.types.InlineKeyboardButton("Элетродрель. Свадебный макияж", callback_data='master_4')
    master_5 = telebot.types.InlineKeyboardButton("Сарумян. Дневной макияж", callback_data='master_5')
    master_6 = telebot.types.InlineKeyboardButton("Голый. Наращивание волос", callback_data='master_6')
    master_7 = telebot.types.InlineKeyboardButton("Гиви. Вечерний макияж", callback_data='master_7')
    master_8 = telebot.types.InlineKeyboardButton("Мерин Гек. Педикюр", callback_data='master_8')
    master_9 = telebot.types.InlineKeyboardButton("Пилигрим Чук. Маникюр", callback_data='master_9')
    master_10 = telebot.types.InlineKeyboardButton("агент Смит. Укладка волос", callback_data='master_10')
    keyboard.row(master_1)
    keyboard.row(master_2)
    keyboard.row(master_3)
    keyboard.row(master_4)
    keyboard.row(master_5)
    keyboard.row(master_6)
    keyboard.row(master_7)
    keyboard.row(master_8)
    keyboard.row(master_9)
    keyboard.row(master_10)
    return keyboard
