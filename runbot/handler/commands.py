from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext

from models.NoIP.NoIP import NoIP
from models.ip import Ip

from contants import USERNAME_NOIP

ip_pub = Ip.get_ip_public()
noIp = NoIP()

def start(update: Update, context: CallbackContext):
  update.message.reply_text(
    "Hello sir, Welcome to the Bot.Please write \
    /help to see the commands available."
  )

def sumnoip(update: Update, context: CallbackContext):
  update.message.reply_text('Please wait a second!')
  noIp.login()
  update.message.reply_text('Login NoIp complete! Try to get list host name')
  list = noIp.list_host_name()
  list_dns = ""
  for i in list:
    list_dns += f"- Host name: {i['hostname']}.\n- Created: {i['date']}.\n- Ip: {i['ip_target']}.\n- Time left: {i['time_left']}.\nWarning: {i['warning']}.\n_____________________________\n"
  response = f"*** NoIP Summary ***\n_____________________________\nAccount login NoIP: {USERNAME_NOIP}.\n\n___________List DNS__________\n" + list_dns + "Noice: /what help you inderstand more.\n"
  update.message.reply_text(
    response
  )

def summatbao(update: Update, context: CallbackContext):
  update.message.reply_text(
    "This function still devepment"
  )

def newhost(update: Update, context: CallbackContext):
  update.message.reply_text(
    "This function still devepment"
  )

def deletehost(update: Update, context: CallbackContext):
  update.message.reply_text(
    "This function still devepment"
  )

def current_ip(update: Update, context: CallbackContext):
  current_ipv4 = ip_pub
  update.message.reply_text(
    f"Current ip now: {current_ipv4}"
  )

def update_manual(update: Update, context: CallbackContext):
  update.message.reply_text(
    "This function still devepment"
  )

def update_auto(update: Update, context: CallbackContext):
  update.message.reply_text(
    "This function still devepment"
  )

def what_warning(update: Update, context: CallbackContext):
  update.message.reply_text(
    "Explain: any hostname will one warning and if it equal [True] that mean NoIp can't access that ip you've provided for NoIp"
  )

def help(update: Update, context: CallbackContext):
  update.message.reply_text("--- List command ---:\n\
    1. /ip will get current ip public on server.\n\
    2. /sumnoip show full imformation on Noip.\n\
    3. /summatbao show full imformation on Matbao.\n\
    4. /newhost create new host on NoIp e.g. /newhost [hostname] [ip].\n\
    5. /deletehost delete host has provided on NoIp e.g. /deletehost [hostname].\n\
    6. /updm update host name manual e.g. /updm [hostname] [ip].\n\
    7. /upda update auto e.g. /upda [hostname].\n\
    ")