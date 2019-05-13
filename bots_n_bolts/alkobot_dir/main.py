#!/usr/bin/python3
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler, CallbackContext, Filters, ConversationHandler
from telegram.ext import MessageHandler as MSH
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging as log

############################# Logging ##########################################


log.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=log.INFO)
logger = log.getLogger(__name__)


############################### Bot ############################################

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def start(update, context):
    kb = [[telegram.KeyboardButton('🍷 Каталог'),
          telegram.KeyboardButton('🛒 Корзина')],
          [telegram.KeyboardButton('🕓 Статус заказа'),
          telegram.KeyboardButton('ℹ️ Помощь')]]
    kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True, one_time_keyboard=True)

    update.message.reply_text(
                     text=start_message(),
                     parse_mode=telegram.ParseMode.HTML,
                     reply_markup=kb_markup)
    return MAIN


def info(update, context):
    update.message.reply_text(text=info_message(),
                              parse_mode=telegram.ParseMode.HTML)
    return INFO


def main_menu(update, context):
    update.message.reply_text(text=main_menu_message(),
                              reply_markup=main_menu_keyboard())
    return CATALOG


def main_menu_kastil_nemnogo_koroche_moego_hera(update, context):
    update.callback_query.edit_message_text(text=main_menu_message(),
                                            reply_markup=main_menu_keyboard())


def menu_1(update, context):
    update.callback_query.edit_message_text(text=menu_1_message(),
                                            reply_markup=menu_1_keyboard())
    return CATALOG


def menu_1_1(update, context):
    update.callback_query.edit_message_text(text=menu_1_1_message(),
                                            reply_markup=menu_1_1_keyboard())
    return CATALOG


def menu_1_1_1(update, context):
    bla = update.callback_query.data
    update.callback_query.edit_message_text(text=menu_1_1_1_message(bla),
                                            parse_mode=telegram.ParseMode.HTML,
                                            reply_markup=menu_1_1_1_keyboard())
    return CATALOG


def menu_2(update, context):
    update.callback_query.edit_message_text(text=menu_2_message(),
                                            reply_markup=menu_2_keyboard())
    return CATALOG


# and so on for every callback_data option
############################ Keyboards #########################################


def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Виски', callback_data='m1')],
                [InlineKeyboardButton('Водка', callback_data='m2'),
                 InlineKeyboardButton('Пиво', callback_data='m2')],
                [InlineKeyboardButton('Вино', callback_data='m2'),
                 InlineKeyboardButton('Коньяк', callback_data='m2')],
                [InlineKeyboardButton('Шампанское', callback_data='m2'),
                 InlineKeyboardButton('Ликеры', callback_data='m2')],
                [InlineKeyboardButton('Текила', callback_data='m2'),
                 InlineKeyboardButton('Аперитивы', callback_data='m2')],
                [InlineKeyboardButton('Джин', callback_data='m2'),
                 InlineKeyboardButton('Абсент', callback_data='m2')]]
    return InlineKeyboardMarkup(keyboard)


def menu_1_keyboard():
    keyboard = [[InlineKeyboardButton('Jack Daniels', callback_data='m1_1')],

                [InlineKeyboardButton('Jameson', callback_data='m1_2'),
                 InlineKeyboardButton('White Horse', callback_data='m1_3')],

                [InlineKeyboardButton('Jim Beam', callback_data='m1_4'),
                 InlineKeyboardButton('Ballantines', callback_data='m1_5')],

                [InlineKeyboardButton('Johnnie Walker', callback_data='m1_6'),
                 InlineKeyboardButton('Chivas Regal', callback_data='m1_7')],

                [InlineKeyboardButton('Macallan ', callback_data='m1_8')],

                [InlineKeyboardButton('<< Назад', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def menu_1_1_keyboard():
    keyboard = [[InlineKeyboardButton('Виски "Джек Дениелс" 0,5 L', callback_data='m1_1_1')],

                [InlineKeyboardButton('Виски "Джек Дениелс" 0,7 L', callback_data='m1_1_2')],

                [InlineKeyboardButton('Виски "Джек Дениелс Теннеси Хани" 0,7 L', callback_data='m1_1_3')],

                [InlineKeyboardButton('<< Назад', callback_data='m1')]]
    return InlineKeyboardMarkup(keyboard)


def menu_1_1_1_keyboard():
    keyboard = [[InlineKeyboardButton('<< Назад', callback_data='m1_1'),

                 InlineKeyboardButton('В корзину', callback_data='main')],

                [InlineKeyboardButton('Посмотреть на сайте', url='http://google.com', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def menu_2_keyboard():
    keyboard = [[InlineKeyboardButton('<< Назад', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


############################# Messages #########################################

def start_message():
    return 'Вас приветствует бот магазина <b>Магазин</b>!\n' \
            '<a href="http://www.google.com/">Наш сайт</a>\n' \
            'Телефон: +7 (495) 123-45-67 или +7 (495) 234-56-78\n' \
            'Звонки принимаются с 21:00 до 9:00\n\n' \
            '🎁При заказе через бота действует скидка 10%'

def main_menu_message():
    return 'Выберите категорию:'


def info_message():
    return 'Данный бот создан компанией Алкотаун, для доставки алкоголя ночью от 30 минут.\n' \
            'Через него вы всегда можете узнать актуальный номер телефона и адрес сайта, а так же сделать заказ.\n' \
            'Алкотаун - это более 5 лет работы на рынке алкоголя и более 1000 отзывов от довольных клиентов!\n\n' \
            'Доставка:\n' \
            'Стоимость доставки по Москве 390 рублей.\n' \
            'Стоимость доставки за МКАД от 490 рублей, уточняйте у оператора.\n' \
            'Заказы в Москве на сумму более 4990 рублей доставляются бесплатно!\n' \
            'Заказы за МКАД на сумму более 9990 рублей доставляются бесплатно!\n' \
            'Вы можете оплатить по безналичному расчету. (VISA и MasterCard)\n\n' \
            'Минимальная сумма заказа - 990 рублей.\n\n' \
            '⚠️ Мы не доставляем алкоголь лицам моложе 18 лет.\n\n' \
            'Если вы нашли ошибку в работе бота, пожалуйста свяжитесь с нами по телефону ' \
            '+7 (499) 653-65-92 или через почту <a href="info@alctown.ru">info@alctown.ru.</a>'


def menu_1_message():
    return 'Категория: Виски'


def menu_1_1_message():
    return 'Категория Jack Daniels'


def menu_1_1_1_message(bla):
    drink = drinks.get(bla)
    a = drink.get("name")
    b = drink.get("price")
 #   c = drink.get("link")
    return 'Просмотр товара в категории: Jack Daniels\n\n' \
           + a + \
           '\n\n<b>Цена:</b> ' + b + ' руб' \
           '<a href="https://solovino.com.ua/wp-content/uploads/2016/03/jack_daniels_0-600x800.jpg">.</a>'


def menu_2_message():
    return 'Ведутся работы, загляните позже...'




############################### Manager ##########################################
MAIN, CATALOG, ORDER, STATUS, INFO = range(5)

con_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        MAIN: [MSH(Filters.regex('^🍷 Каталог$'), main_menu),
               MSH(Filters.regex('^🛒 Корзина$'), main_menu),
               MSH(Filters.regex('^🕓 Статус заказа$'), main_menu),
               MSH(Filters.regex('^ℹ️ Помощь$'), info)],

        CATALOG: [CallbackQueryHandler(main_menu_kastil_nemnogo_koroche_moego_hera, pattern='^main$'),
                  CallbackQueryHandler(menu_1, pattern='^m1$'),
                  CallbackQueryHandler(menu_1_1, pattern='^m1_1$'),
                  CallbackQueryHandler(menu_1_1_1, pattern='^m1_1_*'),
                  CallbackQueryHandler(menu_2, pattern='^m2$')],

        ORDER: [],

        STATUS: [],

        INFO: []
    },
    fallbacks=[MSH(Filters.all, start)],
)


############################# Handlers #########################################

updater = Updater('897186343:AAEepgoedjm902MDmb8qw4i1xKqbusb8V1U',  use_context=True)

updater.dispatcher.add_handler(con_handler)

updater.dispatcher.add_error_handler(error)

updater.start_polling()

d1 = {
  "name": "<b>Виски \"Джек Дениелс\" 0,5 L</b>",
  "price": "2 290",
  "link": "https://solovino.com.ua/wp-content/uploads/2016/03/jack_daniels_0-600x800.jpg"
}

d2 = {
  "name": "<b>Виски \"Джек Дениелс\" 0,7 L</b>",
  "price": "2 850",
  "link": "https://solovino.com.ua/wp-content/uploads/2016/03/jack_daniels_0-600x800.jpg"
}

d3 = {
  "name": "<b>Виски \"Джек Дениелс Теннеси Хани\" 0,7 L</b>",
  "price": "3 050",
  "link": "https://solovino.com.ua/wp-content/uploads/2016/03/jack_daniels_0-600x800.jpg"
}

drinks = {
    "m1_1_1": d1,
    "m1_1_2": d2,
    "m1_1_3": d3
}
