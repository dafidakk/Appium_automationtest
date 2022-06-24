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
#desired_caps['app'] = str(Path().absolute().parent) + '\\app\\keep.apk'
desired_caps['app'] = str(Path().absolute().parent) + '\\app\\hepsiburadanew.apk'


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.implicitly_wait(10)

#driver.find_element_by_android_uiautomator('new UiSelector().text("Ürün, kategori veya marka ara")').click()
el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Ürün, kategori veya marka ara")')
"""
ANDROID_UIAUTOMATOR is the alternate way of, byID,XPATH etc.
"""
el4.click()
el4.send_keys("spor ayakkabı")
driver.press_keycode(66)

# el1 = driver.find_element(by=AppiumBy.ID, value="com.pozitron.hepsiburada:id/textViewSearchBox")
# el1.click()
# el2 = driver.find_element(by=AppiumBy.ID, value="com.pozitron.hepsiburada:id/etACBSearchBox")
# el2.click()
# el2.send_keys("Araba anahtarı")
#
# wait = WebDriverWait(driver, 10)
# wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]')))
"""
element_to_be_clickable waits the object clickable specific time that we were given (10) after doing the job.
"""
driver.press_keycode(66)
#el3 = driver.find_element(by=AppiumBy.XPATH, value="")
#el3.click()

time.sleep(2)
driver.quit()



