
class Field_NoIp():
  """
    Provide some property has define on NoIP by xpath
    Has updated 24/6/2022
  """
  ### URL
  # Using for login
  url_login = 'https://www.noip.com/login'

  # Using for signup
  url_signup = 'https://www.noip.com/sign-up'

  # Dynamic dns dashboard
  url_dynamic = 'https://my.noip.com/dynamic-dns'

  ### Field Login NoIP
  xpath_username = "//input[@name='username']"
  xpath_password = "//input[@name='password']"
  xpath_button_login = "//button[@type='submit' and contains(.,'Log In')]"
  xpath_access_list_host = "//div[@class='col-lg-8 col-md-8 col-sm-12']//div[@class='row']//div//div//div[@class='col-sm-6']//div[@class='stat-cell link-cursor']"

  ### Dashboard dynamic dns
  xpath_list_row_table = "//table[@class='table no-margin-bv table-stack']/tbody/tr"

  ### Field create new host
  # Button open form input new host
  xpath_button_new_host = "//button[@type='button' and contains(.,'Create Hostname')]"

  # Form field new host
  xpath_form_new_host = "(//div[@class='stat-cell link-cursor'])[1]"
  xpath_input_hostname = "//input[@type='text' and @name='name']"
  xpath_input_ipv4 = "//input[@name='target' and @data-cy='ipv4-address']"
  xpath_button_create = "//button[contains(.,'Create Hostname') and contains(@class, 'ml-sm-30')]"


class Field_MatBao():
  pass