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

  def refresh_page(self, url):
    self.get_url(url)

  def login(self):
    try:
      self.user.login_noip()
      self.get_url(self.url_login)
      self.input(self.xpath_username, self.username)
      self.input(self.xpath_password, self.password)
      self.button_click(self.xpath_button_login)
      self.wait_loading_page(self.xpath_access_list_host).click()
    except:
      print('Time out connect NoIP')

  def total_host(self):
    try:
      # Wait load table
      self.wait_loading_page(self.xpath_list_row_table)
      return len(self.get_list_element(self.xpath_list_row_table))
    except:
      print("Can't catch list host name")

  def list_host_name(self):
    list_host_name = []
    try:
      for i in range(1, self.total_host()):
        text = self.get_text(self.hostname(i))
        list_host_name.append(text)
      return list_host_name
    except:
      print("Can't catch list host name")

  def check_exits_host(self, hostname):
    # This version just support domain ddns.net
    hostname = f"{hostname}.ddns.net"
    return hostname in self.list_host_name()

  def create_new_hostname(self, hostname, ipv4):
      if self.check_exits_host(hostname):
        print("Can't create host name, {} is existed".format(hostname))
        return False
      # Wait button create
      self.wait_loading_page(self.xpath_button_new_host).click()

      # Wait form create show
      time.sleep(self.time_sleep)
      self.input(self.xpath_input_hostname, hostname)
      self.input(self.xpath_input_ipv4, ipv4)
      self.button_click(self.xpath_button_create)
      time.sleep(self.time_sleep)
      return True

  def delete_hostname(self, hostname):
    # Check exist hostname
    if self.check_exits_host(hostname):
      hostname = f"{hostname}.ddns.net"
      index = self.list_host_name().index(hostname)+1
      self.element_click(self.button_delete_host(index))
      time.sleep(self.time_sleep)
      self.button_click(self.xpath_button_comfirm_delete)
      print("Delete hostname: {} complete!".format(hostname))
      return True
    print ("{}.ddns.net not existed can't delete please check again".format(hostname))
    return False

  def update_domain(self, hostname):
    hostname = f"{hostname}.ddns.net"
    index = self.list_host_name().index(hostname)+1
    time = self.get_text(self.get_time_created(index))
    print(time)