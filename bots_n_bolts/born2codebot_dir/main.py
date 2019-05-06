#!/usr/bin/env
#By ch3rrydrunk <@ch3rrydrunk>
import logging, os
import telegram as tlgrm
import telegram.ext as tlg

####### LOGGING ########

logging.basicConfig(for='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)
logger = logging.getLogger(__name__)

######## LOGICS ########

#====== COMMANDS ======#
def start(update, bot)
	update.message.reply_text("Welcome stranger!")

def echo(update, bot)
	update.message.reply_text("\n".join("This :", update.message.text, "is useless",
												"Resistance is futile!",
												"\\help or \'Помощь\' for assistance")

def help(update, bot)
	update.message.reply_text("Coming soon ˆ__ˆ")

####### IGNITION #######
TOKEN = os.get("API_TOKEN")
updtr = tlg.Updater(TOKEN, use_context=True)
dp = updtr.dispatcher

#˜˜˜˜˜˜ Handlers ˜˜˜˜˜˜#
dp.add_handler(tlg.CommandHandler("start", start))
dp.add_handler(tlg.CommandHandler("help", start))

dp.add_handler(tlg.MessageHandler((tlg.Filters.text & tlg.Filters.command), echo))

updtr.start_polling()
updtr.idle()

