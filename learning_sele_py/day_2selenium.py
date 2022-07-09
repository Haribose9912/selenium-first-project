import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(
driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
driver.find_element(By.ID,'')
driver.quit()