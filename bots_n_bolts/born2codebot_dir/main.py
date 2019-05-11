#!/usr/bin/env
# By ch3rrydrunk <@ch3rrydrunk>
# Built with grace on python-telegram-bot
import logging as log
import os
from uuid import uuid4

from telegram import (ReplyKeyboardMarkup, CallbackQuery, InlineQueryResultArticle, ParseMode, 
    						InputTextMessageContent)
from telegram.ext import (Updater, CallbackContext, ConversationHandler,
							InlineQueryHandler, Filters)
from telegram.ext import CommandHandler as CMH 
from telegram.ext import MessageHandler as MSH
from telegram.utils.helpers import escape_markdown

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
	update.message.reply_text("Здесь, ты можешь узнать больше о нашей школе\n"
								"Выбери вопрос в выпадающем списке!\n"
								"Используй руки для навигации ;)\n"
								"Обработка естественных запросов coming soon:)",
								reply_markup=faq_markup)
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
	
	update.message.reply_text("https://www.instagram.com/21coding/",
								reply_markup=markup)
	update.message.reply_text("https://www.facebook.com/21coding",
								reply_markup=markup)
	update.message.reply_text("https://vk.com/coding21",
								reply_markup=markup)
	update.message.reply_text("https://21-school.ru/",
								reply_markup=markup)
	return MAIN


def rewind(update, context):
	return MAIN


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def inlinequery(update, context):
    """Handle the inline query."""
    query = update.inline_query.query
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title="Caps",
            input_message_content=InputTextMessageContent(
                query.upper())),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Bold",
            input_message_content=InputTextMessageContent(
                "*{}*".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN)),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Italic",
            input_message_content=InputTextMessageContent(
                "_{}_".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN))]

    update.inline_query.answer(results)


####### IGNITION #######
TOKEN = os.getenv("BOT_API_TOKEN")
bot_core = Updater(TOKEN, use_context=True)
bot = bot_core.dispatcher

#======= LOGICS =======#

#˜˜˜˜˜˜ KEYMAPS  ˜˜˜˜˜˜#

# MAIN MARKUP
main_keyboard = [['🌈 Подписаться на 21_Daily_Tips 🌈'],
				  ['🤷‍♂️ 21_FAQ 🤷', '🔮 Всякое 🔮'],
                  ['📲 Свяжись с нами! 📲'],
				  ['^🕸🔗📱$']]
markup = ReplyKeyboardMarkup(main_keyboard, one_time_keyboard=True)

# FAQ MARKUP
faq_keyboard = [['👈🏿, 🤙🏿'],
				  ['🤷‍♂️ FAQ 🤷', '🔮 Всякое 🔮'],
				  ['🌈 Подписаться на 21_Daily_Tips 🌈']]
faq_markup = ReplyKeyboardMarkup(faq_keyboard, one_time_keyboard=True)

#˜˜˜˜˜˜  MANAGER ˜˜˜˜˜˜#
MAIN, STORY, FAQ, MISC, CONTACT = range(5)

# MAIN States
main_states = [MSH(Filters.regex('^🌈 Подписаться на 21_Daily_Tips 🌈$'), to_story),
					MSH(Filters.regex('^🤷‍♂️ 21_FAQ 🤷$'), to_faq),
					MSH(Filters.regex('^🔮 Всякое 🔮$'), to_misc),
					MSH(Filters.regex('^📲 Свяжись с нами! 📲$'), to_contact, pass_user_data=True),
					MSH(Filters.regex('^🕸🔗📱$'), to_links)
]

return_states = [MSH(Filters.regex('^👈🏿$'), rewind),
					MSH(Filters.regex('^🤙🏿$'), to_links)]

inliner = [InlineQueryHandler(inlinequery)]

conv_handler = ConversationHandler(
	entry_points=[CMH('start', start),
					MSH(Filters.all, rewind),
	],

	states={
		MAIN:	main_states,
		STORY:	main_states.__add__(return_states),
		FAQ:	main_states.__add__(inliner),
		MISC:	main_states.__add__(return_states),
		CONTACT:main_states.__add__(return_states),
	},
	fallbacks=[MSH(Filters.all, help)],
)

bot.add_handler(conv_handler)

#Errors
bot.add_error_handler(error)

#˜˜˜˜˜˜ Gogogo ˜˜˜˜˜˜#
bot_core.start_polling()
bot_core.idle()
