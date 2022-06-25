from appium.webdriver.common.appiumby import AppiumBy


class ScrollUtil:

    @staticmethod
    def scroll_to_text_by_android_ui_automator(text, driver):
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                            value="new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView("
                                  "new UiSelector().textContains(\""+text+"\").instance(0))").click()

    @staticmethod
    def swipe_up(how_many_swipes, driver):
        for i in range(1, how_many_swipes + 1):
            driver.swipe(947, 1800, 947, 500, 1)

    @staticmethod
    def swipe_down(how_many_swipes, driver):
        for i in range(1, how_many_swipes + 1):
            driver.swipe(947, 500, 947, 1800, 1)
