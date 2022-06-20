import time

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

desired_caps = {}

desired_caps['deviceName'] = 'Android'
desired_caps['platformName'] = 'Android'
desired_caps['appPackage'] = 'com.sec.android.app.popupcalculator'
desired_caps['appActivity'] = 'com.sec.android.app.popupcalculator.Calculator'


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="5")
el1.click()
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Artı")
el2.click()
el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="3")
el3.click()
el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Eşit")
el4.click()
result = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Hesaplama girin.")

print(result)
assert int(result) == 8

driver.hide_keyboard()

time.sleep(2)
driver.quit()


