from helper.helps import loadVaribleEnv, getPwd
from dotenv import load_dotenv

load_dotenv(getPwd('user.env'))

USERNAME = loadVaribleEnv('USERNAME')
PASSWORD = loadVaribleEnv('PASSWORD')

# Class User
class User():
  username = USERNAME
  password = PASSWORD

  def get_username(self):
    return self.username

  def get_passwrod(self):
    return self.password

  def login_noip(self):
    print('-----------Login NoIP----------')
    print(f'Username: {self.username}')
    print(f'Password: {self.password}')
    print('-------------------------------')