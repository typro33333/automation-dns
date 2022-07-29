import schedule, time
from telegram.ext.filters import Filters
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.update import Update
from models.NoIP.NoIP import NoIP

from models.bot.telegrambot import TelegramBot

from .handler.commands import start, current_ip, help, sumnoip, newhostmanual, deletehost, update_manual, update_auto, summatbao, what_warning, newhostauto
from .handler.messages import not_found_command, unknown_text

from contants.contants import BOT_TELEGRAM_API_KEY, MAIN_DOMAIN_NOIP

noIp = NoIP()
bot = TelegramBot(BOT_TELEGRAM_API_KEY)
# job_queue = bot.job()

def get_commands():

  # Command execute
  bot.add_handler(CommandHandler('start', start))
  bot.add_handler(CommandHandler('help', help))
  bot.add_handler(CommandHandler('ip', current_ip))
  bot.add_handler(CommandHandler('sumnoip', sumnoip))
  bot.add_handler(CommandHandler('summatbao', summatbao))
  bot.add_handler(CommandHandler('newhostmanual', newhostmanual))
  bot.add_handler(CommandHandler('newhostauto', newhostauto))
  bot.add_handler(CommandHandler('deletehost', deletehost))
  bot.add_handler(CommandHandler('updm', update_manual))
  bot.add_handler(CommandHandler('upda', update_auto))

  # Command support detail command
  bot.add_handler(CommandHandler('what_warning', what_warning))

# Job repeating
# job_second = job_queue.run_repeating(detective_dirrent_ip, interval=60, first=5)

def get_messages():
  bot.add_handler(MessageHandler(Filters.text, not_found_command))    # Filters out unknown messages.
  bot.add_handler(MessageHandler(Filters.command, not_found_command)) # Filters out unknown commands
  bot.add_handler(MessageHandler(Filters.text, unknown_text))

def start_bot_telegram():
  # Start bot telegram
  get_commands()
  get_messages()
  bot.start_polling()