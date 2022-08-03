import time

import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver

from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy


def get_data():
    return [

        ["Adana"],
        ["Konya"],

    ]



@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.parametrize("city", get_data())
def test_dologin(city,appium_driver):
    driver = appium_driver
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
    # allure.attach(driver.get_screenshot_as_png(),name="screenshot",attachment_type=AttachmentType.PNG)

