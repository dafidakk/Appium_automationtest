import time

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from appium.webdriver.common.touch_action import TouchAction

from appiumTest.scroll_util import ScrollUtil

desired_caps = {}
desired_caps['deviceName'] = 'Android'
desired_caps['platformName'] = 'Android'
desired_caps['appPackage'] = 'com.mobeta.android.demodslv'
desired_caps['appActivity'] = 'com.mobeta.android.demodslv.Launcher'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.implicitly_wait(10)

driver.find_elements(AppiumBy.ID, "com.mobeta.android.demodslv:id/activity_title")[0].click()

driver.implicitly_wait(10)

elements = driver.find_elements(AppiumBy.ID, "com.mobeta.android.demodslv:id/drag_handle")

driver.implicitly_wait(10)

actions = TouchAction(driver)

actions.press(elements[0]).wait(3000).move_to(elements[3]).perform().release()



time.sleep(2)
driver.quit()
