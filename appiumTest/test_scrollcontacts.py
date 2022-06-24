import time

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

desired_caps = {}

desired_caps['deviceName'] = 'Android'
desired_caps['platformName'] = 'Android'
desired_caps['appPackage'] = 'com.android.contacts'
desired_caps['appActivity'] = 'com.android.contacts.activities.PeopleActivity'


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)


driver.hide_keyboard()

time.sleep(2)
driver.quit()


