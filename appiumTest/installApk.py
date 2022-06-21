import time
from pathlib import Path

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

desired_caps = {}

desired_caps['deviceName'] = 'Android'
desired_caps['platformName'] = 'Android'
#desired_caps['app'] = str(Path().absolute().parent) + '\\app\\keep.apk'
desired_caps['app'] = str(Path().absolute().parent) + '\\app\\hepsiburadanew.apk'


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.implicitly_wait(10)

el1 = driver.find_element(by=AppiumBy.ID, value="com.pozitron.hepsiburada:id/textViewSearchBox")
el1.click()
el2 = driver.find_element(by=AppiumBy.ID, value="com.pozitron.hepsiburada:id/etACBSearchBox")
el2.click()
el2.send_keys("Araba anahtarı")

el3 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]")
el3.click()

time.sleep(2)
driver.quit()



