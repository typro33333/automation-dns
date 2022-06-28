from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext

def not_found_command(update: Update, context: CallbackContext):
  update.message.reply_text("Sorry '{}' is not a valid command".format(update.message.text))

def unknown_text(update: Update, context: CallbackContext):
  update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)