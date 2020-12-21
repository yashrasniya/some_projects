from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
with open("path.txt" ) as path:
    path = path.read()

name = input("enter the name: ")
message = input("enter the message: ")
try:
    times = int(input("enter the number of times: "))
except ValueError:
    times = 1

driver = webdriver.Chrome(path)
driver.get("https://web.whatsapp.com/")
print("scan QR code with in 30 sec")
time.sleep(30)
print("started ")
# scrche = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
# scrche.send_keys(name)
# scrche.send_keys(Keys.RETURN)

id = driver.find_element_by_xpath(f'//span[@title="{name}"]')
id.click()

for a in range(times):
    text = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    text.send_keys(message)
    text.send_keys(Keys.RETURN)
