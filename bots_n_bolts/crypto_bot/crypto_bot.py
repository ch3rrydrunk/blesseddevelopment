#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram import *
from telegram.ext import *
from cfg.config import ConfigurationParser

import logging

import database

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

MAIN, QUESTION, CONTACT = range(3)


db_data = []


def add_data(data_db):
    global db_data
    db_data.append(data_db)
    print(db_data)
    if len(db_data) == 2:
        database.sqlite3_add_record('./database.db', db_data, 'bot_request')
        db_data = []



def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=start_message(),
        reply_markup=start_menu_markup()
    )
    return MAIN

def first_menu(update, context):
    logger.info(str(update))
    query = update.callback_query
    query.edit_message_text(
        text=first_menu_msg(),
    )
    return QUESTION


def second_menu(update, context):
    logger.info(str(update))
    query = update.callback_query
    query.edit_message_text(
        text=second_menu_msg(),
    )
    return QUESTION


def third_menu(update, context):
    logger.info(str(update))
    query = update.callback_query
    query.edit_message_text(
        text=third_menu_msg(),
    )
    return QUESTION


def question(update, context):
    user = update.message.from_user
    add_data(update.message.text)
    logger.info("The %s asked a question?: %s", user.first_name, update.message.text)
    update.message.reply_text('Оставьте контактные данные – номер телефона/Тг/почта'
                                'В формате:\n '
                                'Имя\n'
                                '+7 987 9911991\n'
                                '@ТГимя\n'
                                'почта@gmail.com')

    return CONTACT


def contact(update, context):
    user = update.message.from_user
    add_data(update.message.text)
    logger.info("The %s asked a question?: %s", user.first_name, update.message.text)
    update.message.reply_text('Спасибо, мы свяжемся с вами в ближайшее время)\n\n'
                                'А пока можете подписаться на наш канал – @smartestcapital')

    return ConversationHandler.END


def cancel(update, context):
    logger.info(str(update))
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('До свидания! Можете подписаться на наш канал – @smartestcapital',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


# Keyboards #########################################
def start_menu_markup():
    keyboard = [[InlineKeyboardButton('1⃣ Общие вопросы / Начинающий трейдер\n / Начинающий инвестор', callback_data='m1')],
                [InlineKeyboardButton('2⃣ Трейдерам / Капитал в доверительное управление', callback_data='m2')],
                [InlineKeyboardButton('3⃣ Инвесторам / Условия / Гарантии', callback_data='m3')]]
    return InlineKeyboardMarkup(keyboard)


#  Messages #########################################
def start_message():
    return 'Здравствуйте! Вас приветствует компания SmartestCapital (Safe Trading Ivestments)🤖,' \
            ' мы готовы ответить на интересующие Вас вопросы.\n' \
            'Выберите интересующее направление: 1, 2 или 3\n\n' \
            'Для завершения диалога наберите /cancel'


def first_menu_msg():
    return 'Опишите детально Ваш вопрос ' \
            'в формате: \n' \
            'Что такое криптовалюта? Как стать трейдером вашей компании? Как инвестировать? '


def second_menu_msg():
    return 'Опишите детально Ваш вопрос' \
            'В формате: \n' \
            'Как стать трейдером/аналитиком компании? Как получить капитал в доверительное управление?'


def third_menu_msg():
    return 'Опишите детально Ваш вопрос' \
            'В формате: \n' \
            'Условия для инвесторов? Ваши гарантии? Доходность и сроки?'


def main():
    cfg = ConfigurationParser()

    print(cfg.token)
    updater = Updater(cfg.token, use_context=True)
    dp = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={

            MAIN: [CallbackQueryHandler(first_menu, pattern='m1'),
                   CallbackQueryHandler(second_menu, pattern='m2'),
                   CallbackQueryHandler(third_menu, pattern='m3')],

            QUESTION: [MessageHandler(Filters.text, question)],

            CONTACT: [MessageHandler(Filters.text, contact)],

        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    database.sqlite3_create_db()
    main()