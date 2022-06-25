import time
from pathlib import Path

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {}

desired_caps['deviceName'] = 'Android'
desired_caps['platformName'] = 'Android'
desired_caps['app'] = str(Path().absolute().parent) + '\\app\\TrendyolSamsungN.apk'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(50)

#driver.find_element_by_android_uiautomator('new UiSelector().text("Ürün, kategori veya marka ara")').click()
#el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Ürün, kategori veya marka ara")')

el5 = driver.find_element(by=AppiumBy.ID, value='trendyol.com:id/buttonSelectGenderMan')
el5.click()

"""
ANDROID_UIAUTOMATOR is the alternate way of, byID,XPATH etc.
"""
#driver.press_keycode(66)


#time.sleep(2)
#driver.quit()



