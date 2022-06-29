import time
from pathlib import Path

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from appiumTest.scroll_util import ScrollUtil

desired_caps = {}
desired_caps['deviceName'] = 'Android'
desired_caps['platformName'] = 'Android'
# desired_caps['app'] = str(Path().absolute().parent) + '\\app\\fliptest.apk'
desired_caps['appPackage'] = 'flipboard.app'
desired_caps['appActivity'] = 'flipboard.activities.LaunchActivityAlias'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


el1 = driver.find_element(by=AppiumBy.ID, value="flipboard.app:id/first_launch_get_started_button")
el1.click()

driver.implicitly_wait(2)

el2 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("# HABER")')
el2.click()
el3 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("# EKONOMİ")')
el3.click()
el4 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("# TEKNOLOJİ")')
el4.click()
el5 = driver.find_element(by=AppiumBy.ID, value="flipboard.app:id/topic_picker_continue_button")
el5.click()
driver.implicitly_wait(3)
el6 = driver.find_element(by=AppiumBy.ID, value="flipboard.app:id/edu_full_screen_sheet_action_primary")
el6.click()
driver.implicitly_wait(3)
el7 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Devam Et")')
el7.click()
driver.implicitly_wait(3)
el8 = driver.find_element(by=AppiumBy.ID, value="flipboard.app:id/account_login_buttons_skip")
el8.click()
time.sleep(4)
ScrollUtil.swipe_up(4, driver)
time.sleep(4)
ScrollUtil.swipe_down(4, driver)
time.sleep(4)
ScrollUtil.swipe_left(2, driver)
time.sleep(4)
ScrollUtil.swipe_right(2, driver)

time.sleep(2)
driver.quit()



