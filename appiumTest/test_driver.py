import time

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    browserName='Chrome'

)

appium_service = AppiumService()
appium_service.start()

print(appium_service.is_running)
print(appium_service.is_listening)

xpath = '//*[@id="searchLanguage"]'

xpath_2 = '//*[@id="tsf"]/div[1]/div[1]/div[1]/div[1]/div/input'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.get("https://google.com")
print(driver.title)
driver.find_element(by=By.XPATH, value=xpath_2).send_keys("Hello Appium !!!")
time.sleep(2)
driver.quit()
appium_service.stop()
