from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

from selenium.webdriver.chrome.service import Service
# from webdriver_manager.core.driver_cache import DriverCacheManager

# cache_manager=DriverCacheManager('driver')
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
# myProxy = "91.192.81.157:40145"

def create_driver():
  options = webdriver.ChromeOptions()
  options.add_argument('--ignore-certificate-errors')
  # options.add_argument('--incognito')
  options.add_argument("no-sandbox")
  options.add_argument("start-maximized")
  options.add_experimental_option("prefs",{"credentials_enable_service": False,"profile.password_manager_enabled": False,"profile.default_content_setting_values.notifications" : 2,"useAutomationExtension" :False})
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  driver = webdriver.Chrome(service=Service("chromedriver.exe"), options=options)
  return driver