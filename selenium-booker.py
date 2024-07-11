from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

from dotenv import load_dotenv
load_dotenv()
USERNAME = os.getenv('USERNAME')
PASS = os.getenv('PASS')

driver = webdriver.Chrome()

driver.get("https://ttp.cbp.dhs.gov/")

# log in button
driver.find_element(By.CSS_SELECTOR, '.login-button').click()

# confirm button
consent = driver.find_element(By.CSS_SELECTOR, "security-modal:nth-child(2) > #security-warn .col-xs-12:nth-child(1) > .btn")
driver.implicitly_wait(10)
consent.click()

# login form
driver.find_element(By.ID, "user_email").send_keys(USERNAME)
pass_f = driver.find_element(By.XPATH, "//*[contains(@id, 'password-toggle-input')]")
driver.implicitly_wait(10)
pass_f.send_keys(PASS)
driver.find_element(By.NAME, "button").click()

# explicit wait
elem = WebDriverWait(driver, 30).until(
EC.presence_of_element_located((By.TAG_NAME, "go-dashboard")) #This is a dummy element
)
# continue selection
driver.find_element(By.CSS_SELECTOR, ".main:nth-child(2) > h2").click()
driver.find_element(By.CSS_SELECTOR, ".col-xs-12:nth-child(1) > .btn-default > span").click()
driver.find_element(By.CSS_SELECTOR, "#centerDetailsUS70 span").click()


while(True):
       pass

