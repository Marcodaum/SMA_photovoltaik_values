from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess
import json
import pathlib

currentPath = pathlib.Path(__file__).parent.resolve()

config_file = open(str(currentPath) + "/configuration.json")
config = json.load(config_file)
config_file.close()

password = config["password"]
url = config["url"]

options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_experimental_option("detach", True)
driver_path = config["path_to_chromedriver"];
driver = webdriver.Chrome(executable_path=driver_path, options=options);

driver.get(url)

try:
     elem = WebDriverWait(driver, 30).until(
     EC.presence_of_element_located((By.ID, "user")))
except:
     print("Page load failed!");
else:

     driver.find_element_by_id('user').click()
     driver.find_element_by_id('user').send_keys(Keys.DOWN)
     driver.find_element_by_id('user').send_keys(Keys.DOWN)
     driver.find_element_by_id('user').send_keys(Keys.RETURN)
     driver.find_element_by_id('password').click()
     driver.find_element_by_id('password').send_keys(password)
     driver.find_element_by_id('bLogin').click()

     try:
          elem = WebDriverWait(driver, 30).until(
          EC.presence_of_element_located((By.ID, "v6180_08214800")))
     except:
          print("Page load failed!")
     else:
          subprocess.call(["xdotool", "key", "F11"])
          driver.execute_script("window.scrollTo(0, 150)")
