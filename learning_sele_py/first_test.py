from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service ##for selenium 4
from selenium.webdriver.common.by import By ##for selenium 4
from selenium.webdriver.support.wait import webdriverWait
from selenium.webdriver.support import expected_conditions as EC

# selenium 4
# serv=Service("C:\\Users\Harish kumar\Downloads\drivers\Chromedriver.exe")
# driver = webdriver.Chrome(service=serv)
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.demoblaze.com/")
# driver.find_element_by_id("login2").click()
driver.find_element(By.ID,"login2").click()
time.sleep(1)
driver.find_element(By.ID,"loginusername").send_keys("hs009")
driver.find_element(By.ID,"loginpassword").send_keys("HS@009")
time.sleep(1)
print("username and password has been entered")
driver.find_element(By.XPATH,"//button[@onclick='logIn()']").click()
print("successfully Logged In...")

actual_title=driver.title
expected_title="STORE"
print("This is the title expected: "+expected_title)
print("Actual title: "+driver.title)
if actual_title==expected_title:
    print("Login sucess")
else:
    print("Login fail")

images = driver.find_elements(By.CLASS_NAME,'modal fade')
print(len(images))
link_text=driver.find_elements(By.LINK_TEXT,"PRODUCT STORE")
print(len(link_text))
links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))
mywait=webdriverWait(driver,10)
# mywait.until(EC.text_to_be_present_in_element())
time.sleep(2)
driver.close()
driver.quit()











# selenium 3
# driver = webdriver.Chrome(executable_path="C:\\Users\\Harish kumar\\Downloads\\drivers\\Chromedriver.exe")
# driver.get("https://www.demoblaze.com/")
# driver.find_element_by_id("login2").click()
# time.sleep(1)
# driver.find_element_by_id("loginusername").send_keys("hs009")
# driver.find_element_by_id("loginpassword").send_keys("HS@009")
# time.sleep(1)
# print("username and password has been entered")
# driver.find_element_by_xpath("//button[@onclick='logIn()']").click()
#
# print("successfully Logged In...")
#
# actual_title=driver.title
# expected_title="STORE"
#
# if actual_title==expected_title:
#     print("Login sucess")
# else:
#     print("Login fail")
#


