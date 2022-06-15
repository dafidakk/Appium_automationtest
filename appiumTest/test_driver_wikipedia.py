import time

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    browserName='Chrome'

)

xpath = '//*[@id="searchLanguage"]'
tag_name = 'option'
appium_service = AppiumService()
appium_service.start()

print(appium_service.is_running)
print(appium_service.is_listening)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.get("https://wikipedia.org")
print(driver.title)
dropdown = driver.find_element(by=By.XPATH, value=xpath)
select = Select(dropdown)
select.select_by_value("en")

options = driver.find_elements(by=By.TAG_NAME, value=tag_name)

print(len(options))

for option in options:
    print("Text is: {}, Lang is: {}".format(option.text, option.get_attribute('Lang')))


time.sleep(2)
driver.quit()
appium_service.stop()
