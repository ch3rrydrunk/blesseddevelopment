#!/usr/bin/env
#By ch3rrydrunk <@ch3rrydrunk>
import logging as log
import os
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler, RegexHandler

####### SETTINGS #######
#~~~~~~~ Logging ~~~~~~#
log.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=log.INFO)
logger = log.getLogger(__name__)

#~~~~~~~ Proxyfy ~~~~~~#
'''
# Be sure to add "request_kwargs=REQUEST_KWARGS" as Updater parameter
REQUEST_KWARGS={
    'proxy_url': 'http://PROXY_HOST:PROXY_PORT/',
    # Optional, if you need authentication:
    'username': 'PROXY_USER',
    'password': 'PROXY_PASS',
}'''

######## LOGICS ########

#====== COMMANDS ======#
def start(bot, update):
	update.message.reply_text("Welcome stranger!")


def echo(bot, update):
	update.message.reply_text(update.message.text)
	update.message.reply_text("Серьезно? :)\n"
							  "Попробуй что-нибудь еще!\n"
							  "'-h' или '/help', например...")


def help(bot, update):
	update.message.reply_text("Coming soon ˆ__ˆ")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


####### IGNITION #######
TOKEN = os.getenv("BOT_API_TOKEN")
updtr = Updater(TOKEN)
dp = updtr.dispatcher

#˜˜˜˜˜˜ Handlers ˜˜˜˜˜˜#

#Commands
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))
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
