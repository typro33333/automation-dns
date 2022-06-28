from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext

from models.ip import Ip

ip = Ip()

def start(update: Update, context: CallbackContext):
  update.message.reply_text(
    "Hello sir, Welcome to the Bot.Please write\
    /help to see the commands available."
  )

def current_ip(update: Update, context: CallbackContext):
  current_ipv4 = ip.get_ip_public()
  update.message.reply_text(
    "Current ip now: ".format(current_ipv4)
  )

def help(update: Update, context: CallbackContext):
  update.message.reply_text("List command: /ip will ip current")