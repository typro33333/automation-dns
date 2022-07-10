from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext

from models.NoIP.NoIP import NoIP
from models.ip import Ip

from contants import USERNAME_NOIP, MAIN_DOMAIN_NOIP

ip_class = Ip()
ip_pub = Ip.get_ip_public()
noIp = NoIP()

def start(update: Update, context: CallbackContext):
  update.message.reply_text(
    "Hello sir, Welcome to the Bot.Please write \
    /help to see the commands available."
  )

def current_ip(update: Update, context: CallbackContext):
  current_ipv4 = ip_pub
  update.message.reply_text(
    f"Current ip now: {current_ipv4}"
  )

def sumnoip(update: Update, context: CallbackContext):
  update.message.reply_text('Please wait a second!')

  print(noIp.driver.title)

  if noIp.driver.title != 'My No-IP':
    noIp.login()
    update.message.reply_text('Login NoIp complete! Try to get list host name')

  list = noIp.list_host_name()
  list_dns = ""
  for i in list:
    list_dns += f"- Host name: {i['hostname']}.\n- Created: {i['date']}.\n- Ip: {i['ip_target']}.\n- Time left: {i['time_left']}.\nWarning: {i['warning']}.\n_____________________________\n"
  response = f"*** NoIP Summary ***\n_____________________________\nAccount login NoIP: {USERNAME_NOIP}.\n\n___________List DNS__________\n" + list_dns + "Noice: /what help you inderstand more.\n"

  return update.message.reply_text(
    response
  )

def summatbao(update: Update, context: CallbackContext):
  update.message.reply_text(
    "This function still devepment"
  )

def newhostmanual(update: Update, context: CallbackContext):
  try:
    hostname = context.args[0]
    ip = context.args[1]

    if ip_class.validate_ip(ip) is False:
      return update.message.reply_text(
      "Invaild Ipv4!"
    )

    if noIp.driver.title != 'My No-IP':
      noIp.login()
      update.message.reply_text('Login NoIp complete! Try to get list host name')

    if noIp.create_new_hostname(hostname, ip):
      return update.message.reply_text(
        f"Create {hostname}.ddns.net complete!"
      )
    return update.message.reply_text(
      "Exist hostname can't create!"
    )
  except IndexError:
    return update.message.reply_text(
      "Invalid input!"
    )

def newhostauto(update: Update, context: CallbackContext):

  if noIp.driver.title != 'My No-IP':
    noIp.login()
    update.message.reply_text('Login NoIp complete! Try to get list host name')

  # With params hostname
  try:

    hostname = context.args[0]

    if noIp.create_new_hostname(hostname, ip_pub):
      return update.message.reply_text(
        f"Create {hostname}.ddns.net complete!"
      )
    return update.message.reply_text(
      "Exist hostname can't create!"
    )

  # Without params new hostname
  except IndexError:
    update.message.reply_text(
      f"Without params, will create main hostname setting {MAIN_DOMAIN_NOIP}"
    )

    if noIp.create_new_hostname(MAIN_DOMAIN_NOIP, ip_pub):
      return update.message.reply_text(
        f"Create {MAIN_DOMAIN_NOIP}.ddns.net complete!"
      )
    return update.message.reply_text(
      f"{MAIN_DOMAIN_NOIP} is exist!"
    )


def deletehost(update: Update, context: CallbackContext):

  if noIp.driver.title != 'My No-IP':
    noIp.login()
    update.message.reply_text('Login NoIp complete! Try to get list host name')

  # With param
  try:
    hostname = context.args[0]

    hostname_domain = f"{hostname}.ddns.net"

    if noIp.delete_hostname(hostname_domain, noIp.index_hostname(hostname_domain)):
      return update.message.reply_text(
        f"Delete {hostname_domain} complete"
      )
    return update.message.reply_text(
      f"{hostname_domain} not found!\n Command /sumnoip to show list hostname"
    )

  # Without param
  except IndexError:

    hostname_domain = f"{MAIN_DOMAIN_NOIP}.ddns.net"

    if noIp.delete_hostname(hostname_domain, noIp.index_hostname(hostname_domain)):
      return update.message.reply_text(
        f"Delete {hostname_domain} complete"
      )
    return update.message.reply_text(
      f"{hostname_domain} not found!\n Command /sumnoip to show list hostname"
    )


def update_manual(update: Update, context: CallbackContext):

  if noIp.driver.title != 'My No-IP':
    noIp.login()
    update.message.reply_text('Login NoIp complete! Try to get list host name')

  try:

    hostname = context.args[0]
    ip = context.args[1]

    # check input ipv4 invalid
    if ip_class.validate_ip(ip) is False:
      return update.message.reply_text(
      "Invaild Ip!"
    )

    try:
      if noIp.update_domain_manual(hostname, ip):
        return update.message.reply_text(
          f"Update {hostname} complete"
        )
      return update.message.reply_text(
        f"Can't update this {hostname}"
      )
    except:
      return update.message.reply_text(
        f"Something error when update manual {hostname}"
      )
  except IndexError:
    update.message.reply_text(
      f'Invalid input!'
    )

def update_auto(update: Update, context: CallbackContext):

  update.message.reply_text(
    f"Please wait!"
  )

  if noIp.driver.title != 'My No-IP':
    noIp.login()
    update.message.reply_text('Login NoIp complete! Try to get list host name')

  try:

    hostname = context.args[0]

    try:
      if noIp.update_domain_auto(hostname):
        return update.message.reply_text(
          f"Update {hostname} complete"
        )
      return update.message.reply_text(
        f"Can't update {hostname}"
      )
    except:
      return update.message.reply_text(
        f"Something error when update auto {hostname}"
      )

  except IndexError:

    hostname = MAIN_DOMAIN_NOIP

    update.message.reply_text(
      "Input hostname not found will auto update on main hostname."
    )

    try:
      if noIp.update_domain_auto(hostname):
        return update.message.reply_text(
          f"Update main {hostname} complete!"
        )
      return update.message.reply_text(
        f"Can't update main {hostname}"
      )
    except:
      return update.message.reply_text(
        f"Something error when update auto {hostname}"
      )

# def detective_dirrent_ip(update: Update, context: CallbackContext):
#   list = noIp.list_host_name()
#   main_hostname = MAIN_DOMAIN_NOIP

#   if noIp.driver.title != 'My No-IP':
#     noIp.login()

#   ip_public = noIp.ip

#   if list[noIp.index_hostname(main_hostname)].ip_target != ip_public:
#     context.bot.send_message(chat_id=context.job.context, text='A single message with 5s delay')

#   context.bot.send_message(text='A single message with 5s delay')

def what_warning(update: Update, context: CallbackContext):
  update.message.reply_text(
    "Explain: any hostname will one warning and if it equal [True] that mean NoIp can't access that ip you've provided for NoIp"
  )

def help(update: Update, context: CallbackContext):
  update.message.reply_text("--- List command ---:\n\
    1. /ip will get current ip public on server.\n\
    2. /sumnoip show full imformation on Noip.\n\
    3. /summatbao show full imformation on Matbao.\n\
    4. /newhostmanual create new host on NoIp e.g. /newhost [hostname] [ip].\n\
    6. /newhostauto create new host on NoIp e.g. /newhost [hostname] [ip].\n\
    7. /deletehost delete host has provided on NoIp e.g. /deletehost [hostname].\n\
    8. /updm update host name manual e.g. /updm [hostname] [ip].\n\
    9. /upda update auto e.g. /upda [hostname].\n\
    ")