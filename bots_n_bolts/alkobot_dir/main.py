#!/usr/bin/python3
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler,  MessageHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


############################### Bot ############################################


def start(bot, update):

    kb = [[telegram.KeyboardButton('🍷 Каталог'),
          telegram.KeyboardButton('🛒 Корзина')],
          [telegram.KeyboardButton('🕓 Статус заказа'),
          telegram.KeyboardButton('ℹ️ Помощь')]]
    kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True, one_time_keyboard=True)

    bot.send_message(chat_id=update.message.chat_id,
                     text="Welcome!",
                     reply_markup=kb_markup)




def main_menu(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=main_menu_message(),
                          reply_markup=main_menu_keyboard())


def menu_1(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=menu_1_message(),
                          reply_markup=menu_1_keyboard())


def menu_1_1(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=menu_1_1_message(),
                          reply_markup=menu_1_1_keyboard())


def menu_1_1_1(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=menu_1_1_1_message(),
                          parse_mode=telegram.ParseMode.HTML,
                          reply_markup=menu_1_1_1_keyboard())


#                     photo=open('pics/1_1_1.jpg', 'rb'))
#  bot.send.image(chat_id=query.message.chat_id, message_id=query.message.message_id, photo=open('pics/1_1_1.jpg'))
#   bot.edit_masage(img=open('pics/1_1_1.jpg'))


def menu_1_1_2(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=menu_1_1_2_message(),
                          parse_mode=telegram.ParseMode.HTML,

                          reply_markup=menu_1_1_2_keyboard())


def menu_2(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=menu_2_message(),
                          reply_markup=menu_2_keyboard())


# and so on for every callback_data option

############################ Keyboards #########################################


def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Виски', callback_data='m1')],
                [InlineKeyboardButton('Водка', callback_data='m2'),
                 InlineKeyboardButton('Пиво', callback_data='m3')],
                [InlineKeyboardButton('Вино', callback_data='m4')]]
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

                [InlineKeyboardButton('Виски "Джек Дениелс Теннеси Хани" 0,7 L', callback_data='main')],

                [InlineKeyboardButton('<< Назад', callback_data='m1')]]
    return InlineKeyboardMarkup(keyboard)


def menu_1_1_1_keyboard():
    keyboard = [[InlineKeyboardButton('<< Назад', callback_data='m1_1'),

                 InlineKeyboardButton('В корзину', callback_data='main')],

                [InlineKeyboardButton('Посмотреть на сайте', url='http://google.com', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def menu_1_1_2_keyboard():
    keyboard = [[InlineKeyboardButton('<< Назад', callback_data='m1_1'),

                 InlineKeyboardButton('В корзину', callback_data='main')],

                [InlineKeyboardButton('Посмотреть на сайте', url='http://google.com', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def menu_2_keyboard():
    keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
                [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
                [InlineKeyboardButton('Main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


############################# Messages #########################################


def main_menu_message():
    return 'Выберите категорию:'


def menu_1_message():
    return 'Категория: Виски'


def menu_1_1_message():
    return 'Категория Jack Daniels'


def menu_1_1_1_message():
    return 'Просмотр товара в категории:' \
           'Jack Daniels\n\n<b>Виски "Джек Дениелс" 0,5 L</b>\n\n<b>Цена:</b> 2 290 руб' \
           '<a href="https://solovino.com.ua/wp-content/uploads/2016/03/jack_daniels_0-600x800.jpg">.</a>'


def menu_1_1_2_message():
    return 'Просмотр товара в категории:  Jack Daniels\n\n<b>Виски "Джек Дениелс" 0,7 L</b>\n\n<b>Цена:</b> 2 850 руб.'


def menu_2_message():
    return 'Choose the submenu in second menu:'


############################# Handlers #########################################


updater = Updater('897186343:AAEepgoedjm902MDmb8qw4i1xKqbusb8V1U')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='^main$'))
updater.dispatcher.add_handler(CallbackQueryHandler(menu_1, pattern='^m1$'))
updater.dispatcher.add_handler(CallbackQueryHandler(menu_1_1, pattern='^m1_1$'))
updater.dispatcher.add_handler(CallbackQueryHandler(menu_1_1_1, pattern='^m1_1_1$'))
updater.dispatcher.add_handler(CallbackQueryHandler(menu_1_1_2, pattern='^m1_1_2$'))
updater.dispatcher.add_handler(CallbackQueryHandler(menu_2, pattern='m2'))
updater.dispatcher.add_handler(CallbackQueryHandler(menu_2, pattern='m3'))
updater.dispatcher.add_handler(CallbackQueryHandler(menu_2, pattern='m4'))

updater.start_polling()
