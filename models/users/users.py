from contants.contants import USERNAME_NOIP, PASSWORD_NOIP

# Class User
class User():
  username = USERNAME_NOIP
  password = PASSWORD_NOIP

  def get_username(self):
    return self.username

  def get_passwrod(self):
    return self.password

  def login_noip(self):
    print('-----------Login NoIP----------')
    print(f'Username: {self.username}')
    print(f'Password: {self.password}')
    print('-------------------------------')