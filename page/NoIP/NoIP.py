import time
from model.selenium import Selenium
from model.user import User
from model.ip import Ip
from model.field import Field_NoIp

class NoIP(Selenium, Field_NoIp):
  """
    This is NoIP provide dns for ip public. Using selenium auto catch field
    in noip and auto dns term by date (3 day, 7day, 28day) can't longer because
    1 dns have 30 days expired! Please noitce that.
  """

  # Declare user login NoIp
  user = User()
  ip = Ip.get_ip_public()

  # Define User and Password
  username = user.get_username()
  password = user.get_passwrod()

  def login(self):
    try:
      self.user.login_noip()
      self.get_url(self.url_login)
      self.input(self.xpath_username, self.username)
      self.input(self.xpath_password, self.password)
      self.button_click(self.xpath_button_login)
      self.wait_loading_page(self.xpath_access_list_host).click()
    except NameError:
      print(NameError)

  def check_exits_host(self):
    try:
      # Wait table load data
      self.wait_loading_page(self.xpath_list_row_table)

      # Get total host on table
      total_host = len(self.get_list_element(self.xpath_list_row_table))-1
      print(f'Tổng cộng có: {total_host}')
    except NameError:
      print(NameError)

  def create_new_hostname(self, hostname, ipv4):
    try:
      self.wait_loading_page(self.xpath_button_new_host).click()
      time.sleep(self.time_sleep)
      self.input(self.xpath_input_hostname, hostname)
      self.input(self.xpath_input_ipv4, ipv4)
      self.button_click(self.xpath_button_create)
      time.sleep(self.time_sleep)
    except NameError:
      print(NameError)

  def delete_hostname(self, hostname):
    try:
      self.get_url(self.url_dynamic)
    except NameError:
      print(NameError)