from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome('C:\\Users\\User\\Downloads\\chromedriver_win32(1)\\chromedriver')
driver.get("https://web.whatsapp.com")


def forward():
    element = driver.find_elements_by_class_name('Tkt2p')
    hov = ActionChains(driver).move_to_element(element[-1])
    hov.perform()
    forward = driver.find_element_by_class_name('_3kN0h')
    forward.click()
    but = driver.find_elements_by_class_name('_2dGjP')
    but[2].click()
    many = driver.find_elements_by_class_name('_1o1sm')
    mn = raw_input('How many message you want to forward: ')
    for i in range(int(mn)):
        many[-i].click()

    forw = driver.find_elements_by_class_name('PNqfx')
    forw[3].click()
    while (True):
        to_name = raw_input("The name of the person to forward this message: ")
        to = driver.find_element_by_xpath('//span[@title = "{}"]'.format(to_name))
        to.click()
        ch = raw_input("Someone else(yes/no): ")
        if ch == 'no':
            break
    cli = driver.find_element_by_class_name('eTCKi')
    cli.click()