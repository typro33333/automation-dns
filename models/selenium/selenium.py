from helper.helps import getPwd, loaddriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from contants.contants import TIME_DELAY, TIME_OUT

class Selenium():
  """
    This default request selenium. All setting and activate selenium
    wil declare here, bellow will show a lot of function have declared.
    We use xpath for define property on website
      1. get_url will move to your brower to link provided
      2. get_element get one element by xpath
      3. get_list_element get list element have same name xpath by xpath
      4. input select input and paste your data
      5. button_click that simple click button
      6. wait_loading_page this is important, this help you wait for web page loading and access property you pass
  """

  # Option webdriver
  options = Options()
  options.add_argument("--disable-extensions")
  # options.add_argument("--no-sandbox")
  # options.add_argument('--headless') # Run without GUI
  # options.add_argument("start-maximized")
  # options.add_argument('--disable-gpu')
  # options.add_argument('--window-size=1920,1080')
  # options.add_argument('--ignore-certificate-errors')
  # options.add_argument("--disable-dev-shm-usage")
  # options.add_argument('--allow-running-insecure-content')
  # options.add_experimental_option('detach', True)
  options.add_experimental_option("detach", False)

  # Load driver selenium
  # service = ChromeService(executable_path=ChromeDriverManager().install())
  # driver = webdriver.Chrome(service=service)

  driver = webdriver.Chrome(executable_path=f"{getPwd()}/drivers/{loaddriver()}" , options=options)

  # Time delay and timeout
  time_out = int(TIME_OUT)
  time_deplay = int(TIME_DELAY)

  # Wait process load page
  wait = WebDriverWait(driver, timeout=time_out)

  # Link to url
  def get_url(self, url):
    self.driver.get(url)

  # Get text in element tag html
  def get_text(self, name_element):
    return self.driver.find_element_by_xpath(name_element).text

  # Get element tag html
  def get_element(self, name_element):
    return self.driver.find_element(By.XPATH, name_element)

  # Get list element tag html e.g: list <td>
  def get_list_element(self, name_element):
    return self.driver.find_elements_by_xpath(name_element)

  # Get tag input element html
  def input(self, name_input, key):
    input = self.driver.find_element(By.XPATH, name_input)
    input.clear()
    input.send_keys(key)

  # Create a action click on any element
  def element_click(self, name_element):
    element = self.driver.find_element(By.XPATH, name_element)
    element.click()

  # Same above but use for button only
  def button_click(self, name_button):
    button = self.driver.find_element(By.XPATH, name_button)
    button.send_keys(Keys.ENTER)

  # This will wait page loading and presence element then return element.
  def wait_loading_page(self, name):
    element = self.wait.until(EC.presence_of_element_located((By.XPATH, name)))
    return element

  # Testing
  def testing(self, text):
    assert f"{text}" not in self.driver

  #If not run in mode detach. pls can use it to exlore memory
  def close(self):
    self.driver.close()