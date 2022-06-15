import time

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    appPackage='com.android.contacts',
    appActivity='com.android.contacts.activities.PeopleActivity'

)

numpad_id = 'com.android.contacts:id/tab_custom_view_icon'
numpad_one_id = 'com.android.contacts:id/one'
numpad_two_id = 'com.android.contacts:id/two'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.find_element(by=By.ID, value=numpad_id).click()
driver.find_element(by=By.ID, value=numpad_one_id).click()
driver.find_element(by=By.ID, value=numpad_two_id).click()
driver.find_element(by=By.ID, value=numpad_two_id).click()
driver.find_element(by=By.ID, value=numpad_two_id).click()

time.sleep(2)
driver.quit()
