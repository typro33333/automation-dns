from helper.helps import loadVaribleEnv, getPwd
from dotenv import load_dotenv

load_dotenv(getPwd('.env'))

# User matbao configs
USERNAME_MATBAO=loadVaribleEnv('USERNAME_MATBAO')
PASSWORD_MATBAO=loadVaribleEnv('PASSWORD_MATBAO')
MAIN_DOMAIN_MATBAO=loadVaribleEnv('MAIN_DOMAIN_MATBAO')

# User NoIp configs
USERNAME_NOIP=loadVaribleEnv('USERNAME_NOIP')
PASSWORD_NOIP=loadVaribleEnv('PASSWORD_NOIP')
MAIN_DOMAIN_NOIP=loadVaribleEnv('MAIN_DOMAIN_NOIP')

# Telegram configs
BOT_TELEGRAM_API_KEY=loadVaribleEnv('BOT_TELEGRAM_API_KEY')

# Selenium configs
TIME_DELAY=loadVaribleEnv('TIME_DELAY')
TIME_OUT=loadVaribleEnv('TIME_OUT')