cd /tmp
wget https://github.com/mozilla/geckodriver/releases/download/v0.25.0/geckodriver-v0.25.0-macos.tar.gz

tar xzf geckodriver-v0.25.0-macos.tar.gz

chmod +x geckodriver


from selenium import webdriver
driver = webdriver.Firefox(executable_path='/tmp/geckodriver')
driver.get('http://example.com')