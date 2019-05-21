#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
import db_bot
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

CONTACT, TASK, MONEY, QUESTION = range(4)


db_data = []


def add_data(data_db):
	global db_data
	db_data.append(data_db)
	print(db_data)
	if len(db_data) == 4:
		db_bot.sqlite3_add_record('./db_bot.db', db_data, 'bot_request')
		db_data = []


def start(bot, update):
	update.message.reply_text(
        'Добрейшего вечерочка! Вы, видимо, хотите заказать у меня бота, такого же прекрасного как и я.\n'
        'Send /cancel to stop talking to me.\n\n'
        'Для начала оставьте свой контакт по которому мы сможем с вами связаться.')
	return CONTACT


def contact(bot, update):
	user = update.message.from_user
	add_data(update.message.text)
	logger.info("Contact of %s: %s", user.first_name, update.message.text)
	update.message.reply_text('Теперь опишите техническое задание для бота.\n'
                              'Либо задайте интересующий вас вопрос')

	return TASK


def task(bot, update):
	user = update.message.from_user
	add_data(update.message.text)
	logger.info("Bot technical task is: %s", update.message.text)
	update.message.reply_text('Если вы описали техническое задание для бота, то напишите ваш бюджет\n'
								'Если у вас был вопрос, то наберите /skip .')

	return MONEY


def money(bot, update):
	reply_keyboard = [['Yes', 'No']]
	user = update.message.from_user
	add_data(update.message.text)
	logger.info("Budget of %s: %s", user.first_name, update.message.text)
	update.message.reply_text(
		'Ваша заявка была вопросом?',
		reply_markup=ReplyKeyboardMarkup(reply_keyboard,one_time_keyboard=True))

	return QUESTION


def skip_money(bot, update):
	reply_keyboard = [['Yes', 'No']]
	user = update.message.from_user
	logger.info("User %s did not send a budget.", user.first_name)
	update.message.reply_text(
		'Ваша заявка была вопросом?',
		reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

	return QUESTION


def question(bot, update):
	user = update.message.from_user
	add_data(update.message.text)
	logger.info("The %s asked a question?: %s", user.first_name, update.message.text)
	update.message.reply_text('Заявка/вопрос принят(а), в ближайшее время мы с вами свяжемся!')

	return ConversationHandler.END


def cancel(bot, update):
	user = update.message.from_user
	logger.info("User %s canceled the conversation.", user.first_name)
	update.message.reply_text('Bye! I hope we can talk again some day.',
								reply_markup=ReplyKeyboardRemove())

	return ConversationHandler.END


def error(bot, update, error):
	logger.warning('Update "%s" caused error "%s"', update, error)


def main():
	updater = Updater("TOKEN")
	dp = updater.dispatcher
	data_db = []
	conv_handler = ConversationHandler(
		entry_points=[CommandHandler('start', start)],

		states={
			CONTACT: [MessageHandler(Filters.text, contact)],

			TASK: [MessageHandler(Filters.text, task),
					CommandHandler('skip', skip_money)],

			MONEY: [MessageHandler(Filters.text, money),
					CommandHandler('skip', skip_money)],

			QUESTION: [RegexHandler('^(Yes|No)$', question)]

		},

		fallbacks=[CommandHandler('cancel', cancel)]
	)

	dp.add_handler(conv_handler)
	dp.add_error_handler(error)

	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	db_bot.sqlite3_create_db()
	main()