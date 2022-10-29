from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = 'C:\Program Files\chromedriver.exe'

browser = webdriver.Chrome(driver_path)

browser.get('https://www.feastogether.com.tw/booking/2')

time.sleep(0.5)

close_button = browser.find_element(By.LINK_TEXT, "我知道了").click()

Sign_in_botton = browser.find_element(By.XPATH, "//ul[@class='wk-member-menu clearfix']/li[2]").click()

time.sleep(0.5)

username = browser.find_element(By.XPATH, "//input[@placeholder='手機']").send_keys("*******")

time.sleep(0.5)

password = browser.find_element(By.XPATH, "//input[@type='password']").send_keys("*******")

time.sleep(1.0)

Sign_in = browser.find_element(By.NAME, "form-login").click()

time.sleep(0.5)

alert = browser.switch_to.alert.accept()

