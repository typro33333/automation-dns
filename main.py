from models.ip import Ip

from telegram.update import Update
from telegram.ext.updater import Updater
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

from contants import BOT_TELEGRAM_API_KEY

"""
  - Updater: This will contain the API key we got from BotFather to specify in which bot we are adding functionalities to using our python code.
  - Update: This will invoke every time a bot receives an update i.e. message or command and will send the user a message.
  - CallbackContext: We will not use its functionality directly in our code but when we will be adding the dispatcher it is required (and it will work internally)
  - CommandHandler: This Handler class is used to handle any command sent by the user to the bot, a command always starts with “/” i.e “/start”,”/help” etc.
  - MessageHandler: This Handler class is used to handle any normal message sent by the user to the bot,
  - FIlters: This will filter normal text, commands, images, etc from a sent message.
"""

updater = Updater(BOT_TELEGRAM_API_KEY, use_context=True)

def start(update: Update, context: CallbackContext):
  update.message.reply_text(
    "Hello sir, Welcome to the Bot.Please write\
    /help to see the commands available."
  )

def current_ip(update: Update, context: CallbackContext):
  current_ipv4 = Ip.get_ip_public()
  update.message.reply_text(
    "Current ip now: ".format(current_ipv4)
  )

def help(update: Update, context: CallbackContext):
  update.message.reply_text("List command: /ip will ip current")

def not_found_command(update: Update, context: CallbackContext):
  update.message.reply_text("Sorry '{}' is not a valid command".format(update.message.text))

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)

def main():
  updater.dispatcher.add_handler(CommandHandler('start', start))
  updater.dispatcher.add_handler(CommandHandler('help', help))
  updater.dispatcher.add_handler(CommandHandler('ip', current_ip))
  updater.dispatcher.add_handler(MessageHandler(Filters.text, not_found_command))    # Filters out unknown messages.
  updater.dispatcher.add_handler(MessageHandler(Filters.command, not_found_command)) # Filters out unknown commands
  updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

  updater.start_polling()

if __name__ == '__main__':
  print('Server is running!')
  main()