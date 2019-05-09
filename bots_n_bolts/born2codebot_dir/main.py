#!/usr/bin/env
# By ch3rrydrunk <@ch3rrydrunk>
# Built with grace on python-telegram-bot
import logging as log
import os

from telegram import ReplyKeyboardMarkup, CallbackQuery
from telegram.ext import (Updater, CallbackContext, ConversationHandler, Filters)
from telegram.ext import CommandHandler as CMH 
from telegram.ext import MessageHandler as MSH

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

######### LOGICS ########
#~~~~~~~ Commands ~~~~~~#
def start(update, context):
	update.message.reply_text("Welcome stranger!",
								reply_markup=markup)
	return MAIN


def help(update, context):
	update.message.reply_text("Серьезно? :)\n"
								"Просто используй кнопки для навигации по боту\n"
								"или набери '/start' для перезагрузки!",
								reply_markup=markup)
	return MAIN

#~~~~~~~~ States ~~~~~~~#
def	to_story(update, context):
	update.message.reply_text("Загляни чуть позже;)\n"
								"Ведутся работы!",
								reply_markup=markup)
	return STORY


def	to_faq(update, context):
	update.message.reply_text("Загляни чуть позже;)\n"
								"Ведутся работы!",
								reply_markup=markup)
	return FAQ


def	to_misc(update, context):
	update.message.reply_text("Загляни чуть позже;)\n"
								"Ведутся работы!",
								reply_markup=markup)
	return MISC


def	to_contact(update, context):
	update.message.reply_text("Загляни чуть позже;)\n"
								"Ведутся работы!",
								reply_markup=markup)
	return CONTACT
	
def	to_links(update, context):
	text = update.message.text
	if (text.find('📱', 0)):
		update.message.reply_text("https://www.instagram.com/21coding/",
								reply_markup=markup)
	elif (text.find('🙃', 0)):
		update.message.reply_text("https://www.facebook.com/21coding",
								reply_markup=markup)
	elif (text.find('🅱️', 0)):
		update.message.reply_text("https://vk.com/coding21",
								reply_markup=markup)
	elif (text.find('🕸', 0)):
		update.message.reply_text("https://21-school.ru/",
								reply_markup=markup)
	return MAIN

def rewind(update, context):
	return MAIN


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


####### IGNITION #######
TOKEN = os.getenv("BOT_API_TOKEN")
bot_core = Updater(TOKEN, use_context=True)
bot = bot_core.dispatcher

#======= LOGICS =======#

#˜˜˜˜˜˜  KEYMAP  ˜˜˜˜˜˜#
reply_keyboard = [['🌈 Узнать больше о Школе 🌈'],
				  ['🤷‍♂️ FAQ 🤷', '🔮 Всякое 🔮'],
                  ['📲 Свяжись с нами! 📲'],
				  ['📱📷', '🙃📖', '🅱️🙏', '🕸🔗']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

#˜˜˜˜˜˜  MANAGER ˜˜˜˜˜˜#
MAIN, STORY, FAQ, MISC, CONTACT = range(5)

conv_handler = ConversationHandler(
	entry_points=[CMH('start', start),
					CMH('help', help),
	],

	states={
		MAIN:	[MSH(Filters.regex('^🌈 Узнать больше о Школе 🌈$'), to_story),
					MSH(Filters.regex('^🤷‍♂️ FAQ 🤷$'), to_faq),
					MSH(Filters.regex('^🔮 Всякое 🔮$'), to_misc),
					MSH(Filters.regex('^📲 Свяжись с нами! 📲$'), to_contact),
					MSH((Filters.regex('^📱📷$') | Filters.regex('^🙃📖$') | 
							Filters.regex('^🅱️🙏$') | Filters.regex('^🕸🔗$')), to_links),
					
		],
		STORY:	[MSH(Filters.regex('^🌈 Узнать больше о Школе 🌈$'), to_story),
					MSH(Filters.regex('^🤷‍♂️ FAQ 🤷$'), to_faq),
					MSH(Filters.regex('^🔮 Всякое 🔮$'), to_misc),
					MSH(Filters.regex('^📲 Свяжись с нами! 📲$'), to_contact),
					MSH((Filters.regex('^📱📷$') | Filters.regex('^🙃📖$') | 
							Filters.regex('^🅱️🙏$') | Filters.regex('^🕸🔗$')), to_links),
					
		],
		FAQ:	[MSH(Filters.regex('^🌈 Узнать больше о Школе 🌈$'), to_story),
					MSH(Filters.regex('^🤷‍♂️ FAQ 🤷$'), to_faq),
					MSH(Filters.regex('^🔮 Всякое 🔮$'), to_misc),
					MSH(Filters.regex('^📲 Свяжись с нами! 📲$'), to_contact),
					MSH((Filters.regex('^📱📷$') | Filters.regex('^🙃📖$') | 
							Filters.regex('^🅱️🙏$') | Filters.regex('^🕸🔗$')), to_links),
					
		],
		MISC:	[MSH(Filters.regex('^🌈 Узнать больше о Школе 🌈$'), to_story),
					MSH(Filters.regex('^🤷‍♂️ FAQ 🤷$'), to_faq),
					MSH(Filters.regex('^🔮 Всякое 🔮$'), to_misc),
					MSH(Filters.regex('^📲 Свяжись с нами! 📲$'), to_contact),
					MSH((Filters.regex('^📱📷$') | Filters.regex('^🙃📖$') | 
							Filters.regex('^🅱️🙏$') | Filters.regex('^🕸🔗$')), to_links),
					
		],
		CONTACT:[MSH(Filters.regex('^🌈 Узнать больше о Школе 🌈$'), to_story),
					MSH(Filters.regex('^🤷‍♂️ FAQ 🤷$'), to_faq),
					MSH(Filters.regex('^🔮 Всякое 🔮$'), to_misc),
					MSH(Filters.regex('^📲 Свяжись с нами! 📲$'), to_contact),
					MSH((Filters.regex('^📱📷$') | Filters.regex('^🙃📖$') | 
							Filters.regex('^🅱️🙏$') | Filters.regex('^🕸🔗$')), to_links),
					
		],
	},
	fallbacks=[MSH(Filters.all, help)],
)

bot.add_handler(conv_handler)

#Errors
bot.add_error_handler(error)

#˜˜˜˜˜˜ Gogogo ˜˜˜˜˜˜#
bot_core.start_polling()
bot_core.idle()
