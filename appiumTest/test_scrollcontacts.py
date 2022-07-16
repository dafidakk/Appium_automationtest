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
desired_caps['appPackage'] = 'com.android.contacts'
desired_caps['appActivity'] = 'com.android.contacts.activities.PeopleActivity'
desired_caps['noReset'] = True
# noReset : app will be launch as you launch as you did before


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

"""
el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                          value='new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView('
                                'new UiSelector().textContains("Ahmet Hosso").instance(0))')


el4.click()
"""
'swipe up'

"""
driver.swipe(947, 1800, 947, 500, 1)
driver.swipe(947, 1800, 947, 500, 1)
driver.swipe(947, 1800, 947, 500, 1)
driver.swipe(947, 1800, 947, 500, 1)
driver.swipe(947, 1800, 947, 500, 1)


"""
'swipe down'
"""
driver.swipe(947, 500, 947, 1800, 1)
driver.swipe(947, 500, 947, 1800, 1)
driver.swipe(947, 500, 947, 1800, 1)
driver.swipe(947, 500, 947, 1800, 1)
driver.swipe(947, 500, 947, 1800, 1) 

ScrollUtil.scroll_to_text_by_android_ui_automator("Alican", driver)

ScrollUtil.swipe_up(5, driver)
ScrollUtil.swipe_down(5, driver)

"""

elements = driver.find_elements(AppiumBy.ID, "com.android.contacts:id/cliv_name_textview")
print(len(elements))

actions = TouchAction(driver)

# actions.tap(elements[0]).perform()
actions.long_press(elements[0]).perform()
time.sleep(2)
driver.quit()


