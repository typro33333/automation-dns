from telegram.update import Update
from telegram.ext.updater import Updater
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

from contants import BOT_TELEGRAM_API_KEY

class TelegramBot():
  """
    - Updater: This will contain the API key we got from BotFather to specify in which bot we are adding functionalities to using our python code.
    - Update: This will invoke every time a bot receives an update i.e. message or command and will send the user a message.
    - CallbackContext: We will not use its functionality directly in our code but when we will be adding the dispatcher it is required (and it will work internally)
    - CommandHandler: This Handler class is used to handle any command sent by the user to the bot, a command always starts with “/” i.e “/start”,”/help” etc.
    - MessageHandler: This Handler class is used to handle any normal message sent by the user to the bot,
    - FIlters: This will filter normal text, commands, images, etc from a sent message.
  """

  updater = ''

  def __init__(self, key):
    self.updater = Updater(key, use_context=True)

  def command_handler(self, name, function):
    """
      - name: auto add '/' at fisrt ex: info => /info.
      - function: def, class method, helps, etc.
    """
    return CommandHandler(name, function)

  def message_handler(self, name, function):
    """
      - name: like filters or string, etc.
      - function: def, class method, help, etc.
    """
    return MessageHandler(name, function)

  def add_handler(self, command):
    self.updater.dispatcher.add_handler(command)

  def error_handler(self, command):
    self.updater.dispatcher.error_handlers(command)

  def start_polling(self):
    self.updater.start_polling()

