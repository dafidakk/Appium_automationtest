import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope="function")
def appium_driver():
    # global appium_service
    # appium_service = AppiumService()
    # appium_service.start()
    desired_caps = {}

    desired_caps['deviceName'] = 'Android'
    desired_caps['platformName'] = 'Android'
    desired_caps['appPackage'] = 'com.etstur'
    desired_caps['appActivity'] = 'com.etstur.modules.common.main.MainActivity'
    desired_caps['noReset'] = True
    # noReset : app will be launch as you launch as you did before
    global driver
    driver = webdriver.Remote('http://127.0.0.1:4724/wd/hub', desired_caps)
    yield driver
    driver.quit()


@pytest.fixture()
def log_on_failure(request,appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
