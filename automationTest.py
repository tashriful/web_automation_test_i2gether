from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome(executable_path ="C:/chromedriver/chromedriver.exe")

driver.get("https://www.youtube.com/user/edurekaIN")
# # driver.find_element_by_id().send_keys("Movies")
# driver.find_element_by_name("q").send_keys("Selenium")
# driver.find_element_by_name('btnk').click()
driver.find_element_by_xpath("//app-header/div[@id='contentContainer']/div[@id='channel-container']/div[@id='channel-header']/div[@id='channel-header-container']/div[@id='inner-header-container']/div[@id='buttons']/div[@id='subscribe-button']/ytd-button-renderer[1]/a[1]/paper-button[1]/yt-formatted-string[1]").click()
