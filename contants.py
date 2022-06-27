from helper.helps import loadVaribleEnv, getPwd
from dotenv import load_dotenv

load_dotenv(getPwd('user.env'))

# User matbao
USERNAME_MATBAO=loadVaribleEnv('USERNAME_MATBAO')
PASSWORD_MATBAO=loadVaribleEnv('PASSWORD_MATBAO')

# User NoIp
USERNAME_NOIP=loadVaribleEnv('USERNAME_NOIP')
PASSWORD_NOIP=loadVaribleEnv('PASSWORD_NOIP')

# Telegram
BOT_TELEGRAM_API_KEY='5483920092:AAF8rk6LKH4vsek0viOTzeazASsf1DSp-aU'

# Configs
