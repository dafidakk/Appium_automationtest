import time

import pytest
from appium import webdriver

from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy


def get_data():
    return [

        ["Adana"],
        ["Konya"],

    ]


def setup_function():
    global appium_service
    appium_service = AppiumService()
    appium_service.start()
    desired_caps = {}

    desired_caps['deviceName'] = 'Android'
    desired_caps['platformName'] = 'Android'
    desired_caps['appPackage'] = 'com.etstur'
    desired_caps['appActivity'] = 'com.etstur.modules.common.main.MainActivity'
    desired_caps['noReset'] = True
    # noReset : app will be launch as you launch as you did before
    global driver
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


def teardown_function():
    time.sleep(2)
    driver.quit()
    appium_service.stop()


@pytest.mark.parametrize("city", get_data())
def test_dologin(city):
    driver.implicitly_wait(2)
    driver.find_element(by=AppiumBy.ID, value='com.etstur:id/etInput').click()
    driver.implicitly_wait(2)
    driver.find_element(by=AppiumBy.ID, value='com.etstur:id/et_input').send_keys(city)
    driver.implicitly_wait(2)
    driver.find_elements(by=AppiumBy.ID, value='com.etstur:id/tvSuggestion')[0].click()
    driver.implicitly_wait(2)
    driver.find_element(by=AppiumBy.ID, value='com.etstur:id/btnSearch').click()
    driver.implicitly_wait(2)
    cityText = driver.find_element(by=AppiumBy.ID, value='com.etstur:id/tv_title').text
    print(cityText)
    newText = str(cityText).replace("Otelleri","").replace(" ","")
    print(newText)
    assert newText in city
