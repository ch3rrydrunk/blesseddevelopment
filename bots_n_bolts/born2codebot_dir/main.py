#!/usr/bin/env
# By ch3rrydrunk <@ch3rrydrunk>
# Built with grace on python-telegram-bot
import logging as log
import os

from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, ConversationHandler, CommandHandler, RegexHandler,
						 Filters, MessageHandler)

####### SETTINGS #######
#~~~~~~~ Logging ~~~~~~#
log.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=log.INFO)
logger = log.getLogger(__name__)

#~~~~~~~ Proxyfy ~~~~~~#
'''
# Be sure to add "request_kwargs=REQUEST_KWARGS" as Updater parameter if you wanna use proxy
REQUEST_KWARGS={
    'proxy_url': 'http://PROXY_HOST:PROXY_PORT/',
    # Optional, if you need authentication:
    'username': 'PROXY_USER',
    'password': 'PROXY_PASS',
}'''

######## LOGICS ########

#˜˜˜˜˜˜  STATES  ˜˜˜˜˜˜#
MAIN, MORE, MISC, CONTACT = range(4)
reply_keyboard = [['Узнать больше о нас'],
				  ['FAQ', 'Всякое ^__^'],
                  ['Свяжись с нами!']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

#====== COMMANDS ======#
def start(bot, update):
	update.message.reply_text("Welcome stranger!",
								reply_markup=markup)
	return MAIN

def echo(bot, update):
	update.message.reply_text(update.message.text)
	update.message.reply_text("Серьезно? :)\n"
							  "Попробуй что-нибудь еще!\n"
							  "или просто используй '/help'",
								reply_markup=markup)
	return MAIN

def help(bot, update):
	update.message.reply_text("Выбери нужный отдел и вперед!",
								reply_markup=markup)

	return MAIN
	


def rewind(bot, update):
	update.message.reply
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


####### IGNITION #######
TOKEN = os.getenv("BOT_API_TOKEN")
updtr = Updater(TOKEN)
dp = updtr.dispatcher

#˜˜˜˜˜˜ Handlers ˜˜˜˜˜˜#

#State handling (aka Conversation)
conv_handler = ConversationHandler(
	entry_points=[CommandHandler('start', start),
				  RegexHandler('^Назад$', rewind, pass_user_data=True)],

	states={
		MAIN:		[

		],
		MORE:		[

		],
		MISC:		[

		],
		CONTACT:	[

		]
	},
	fallbacks=[RegexHandler('^Назад$', rewind, pass_user_data=True)]
)
#Commands
dp.add_handler(conv_handler)
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))
dp.add_handler(RegexHandler('^Назад$', rewind, pass_user_data=True))

#Navigation


#Callback


#Junk
dp.add_handler(RegexHandler("-h", help))
dp.add_handler(MessageHandler(Filters.all, echo))
#Errors
dp.add_error_handler(error)

#˜˜˜˜˜˜ Gogogo ˜˜˜˜˜˜#
updtr.start_polling()
updtr.idle()
