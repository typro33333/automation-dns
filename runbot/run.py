from telegram.ext.filters import Filters
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler

from models.bot.telegrambot import TelegramBot
from .handler.commands import start, current_ip, help
from .handler.messages import not_found_command, unknown_text

from contants import BOT_TELEGRAM_API_KEY

bot = TelegramBot(BOT_TELEGRAM_API_KEY)

def get_commands():
  bot.add_handler(CommandHandler('start', start))
  bot.add_handler(CommandHandler('help', help))
  bot.add_handler(CommandHandler('getip', current_ip))

def get_messages():
  bot.add_handler(MessageHandler(Filters.text, not_found_command))    # Filters out unknown messages.
  bot.add_handler(MessageHandler(Filters.command, not_found_command)) # Filters out unknown commands
  bot.add_handler(MessageHandler(Filters.text, unknown_text))

def start_bot_telegram():
  # Start bot telegram
  get_commands()
  get_messages()
  bot.start_polling()