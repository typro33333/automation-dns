import time
import datetime
from models.selenium.selenium import Selenium
from models.users.users import User
from models.ip import Ip
from models.field import Field_NoIp

class NoIP(Selenium, Field_NoIp):
  """
    This is NoIP provide dns for ip public. Using selenium auto catch field
    in noip and auto dns term by date (3 day, 7day, 28day) can't longer because
    1 dns have 30 days expired! Please noitce that.
    And on account free can create maxium 3 dns.
  """
  # Current time
  current_time = datetime.datetime.now()

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
      # self.user.login_noip() log information user
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
        warning = False
        time_create = self.get_text(self.date_hostname(i)).split('\n', 1)
        datetime_object = datetime.datetime.strptime(time_create[0], '%b %d, %Y') + datetime.timedelta(30)
        time_left = datetime_object - self.current_time
        if time_left.days <= 7:
          warning = True
        dns_hostname = {
          'hostname': self.get_text(self.hostname(i)),
          'date': time_create[0],
          'ip_target': self.get_text(self.ip_targert_hostname(i)),
          'time_left': f"{time_left.days} days left",
          'warning': warning
        }
        list_host_name.append(dns_hostname)
      return list_host_name

    except:
      print("Can't catch list host name")
      return list_host_name

  def check_exits_host(self, hostname):
    for i in self.list_host_name():
      if i['hostname'] == hostname:
        return True
    return False

  def index_hostname(self, hostname):
    index = 1
    for i in self.list_host_name():
      if i['hostname'] == hostname:
        break
      index += 1
    return index

  def create_new_hostname(self, hostname, ipv4):
    hostname_dns = f"{hostname}.ddns.net"
    if self.check_exits_host(hostname_dns):
      print("Can't create host name, {} is exists".format(hostname))
      return False

    # Wait button create
    self.wait_loading_page(self.xpath_button_new_host).click()

    # Wait form create show
    time.sleep(self.time_deplay)
    self.input(self.xpath_input_hostname, hostname)
    self.input(self.xpath_input_ipv4, ipv4)
    self.button_click(self.xpath_button_create)
    time.sleep(self.time_deplay)
    print(f"Create {hostname} complete!")
    return True

  def delete_hostname(self, hostname, index):
    # Check exist hostname
    if self.check_exits_host(hostname):
      self.element_click(self.button_delete_host(index))
      time.sleep(self.time_deplay)
      self.button_click(self.xpath_button_comfirm_delete)
      print("Delete hostname: {} complete!".format(hostname))
      return True
    print ("{} doesn't exists for delete!".format(hostname))
    return False

  def update_domain_manual(self, hostname, ip):
    """
      Need provide ip manual
      Update domain when ipv4 diffirent with server. And provide new lienses (30 days) again.
      This action will force update hostname and no care of time left noip
    """
    hostname_dns = f"{hostname}.ddns.net"

    if self.delete_hostname(hostname_dns, self.index_hostname(hostname_dns)) == False:
      return False

    time.sleep(self.time_deplay)
    self.create_new_hostname(hostname, ip)
    print(f"Update {hostname} complete")
    return True

  def update_domain_auto(self, hostname):
    """
      Don't need provide ip manual, ip will set by ip public.
      Noice: If you use this function, the ip auto get from on local
      Update domain when ipv4 diffirent with server. And provide new lienses (30 days) again.
      This action will force update hostname and no care of time left noip
    """
    hostname_dns = f"{hostname}.ddns.net"

    if self.delete_hostname(hostname_dns, self.index_hostname(hostname_dns)) == False:
      return False

    time.sleep(self.time_deplay)
    self.create_new_hostname(hostname, self.ip)
    print(f"Update {hostname} complete")
    return True
