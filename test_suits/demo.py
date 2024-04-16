import time
from selenium.webdriver.common.by import By
from selenium import webdriver

url = "https://thinking-tester-contact-list.herokuapp.com/login"
driver = webdriver.Chrome()

driver.get(url)

driver.find_element(By.ID, "email").send_keys("abc")
driver.find_element(By.ID, "submit").click()

time.sleep(3)