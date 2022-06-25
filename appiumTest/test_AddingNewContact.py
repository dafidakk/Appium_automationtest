import time

from appium import webdriver
# from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    appPackage='com.android.contacts',
    appActivity='com.android.contacts.activities.PeopleActivity'

)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.find_element(by=By.ID, value='com.android.contacts:id/tab_custom_view_icon').click()
driver.implicitly_wait(5)
driver.find_element(by=By.XPATH, value="//*[contains(@text, 'Kişiler')]").click()
driver.find_element(by=By.ID, value='com.android.contacts:id/first_option_menu').click()
driver.find_element(by=By.ID, value='com.android.packageinstaller:id/permission_allow_button').click()
driver.find_element(by=By.ID, value='android:id/button1').click()
driver.find_element(by=By.XPATH, value="//*[contains(@text, 'Tamam')]").click()
driver.find_element(by=By.XPATH, value="//*[contains(@text, 'İsim')]").send_keys("Ahmet Fatih DEVECİ")
driver.find_element(by=By.ID, value='com.android.contacts:id/menu_done').click()
driver.implicitly_wait(50)
"""
driver.find_element(by=By.XPATH, value="//android.widget.EditText[@text ='İsim']").send_keys("Ahmet Fatih DEVECİ")
driver.find_element(by=By.ID, value='com.android.contacts:id/first_option_menu').click()
driver.find_element(by=By.ID, value='com.android.contacts:id/five').click()
driver.find_element(by=By.ID, value='com.android.contacts:id/four').click()
driver.find_element(by=By.ID, value='com.android.contacts:id/four').click()
driver.find_element(by=By.ID, value='com.android.contacts:id/five').click()
driver.find_element(by=By.ID, value='com.android.contacts:id/seven').click()
driver.find_element(by=By.ID, value='com.android.contacts:id/nine').click()
driver.find_element(by=By.ID, value='com.android.contacts:id/five').click()
driver.find_element(by=By.ID, value='com.android.contacts:id/six').click()
driver.find_element(by=By.ID, value='com.android.contacts:id/seven').click()
driver.find_element(by=By.ID, value='com.android.contacts:id/six').click()

driver.find_element(by=By.ID, value='com.android.contacts:id/call_add_text').click()
driver.find_element(by=By.ID, value='com.android.contacts:id/create_contact').click()

driver.find_element(by=By.XPATH, value="//android.widget.EditText[@text ='?sim']").send_keys("Ahmet Fatih DEVECİ")
driver.find_element(by=By.ID, value='com.android.contacts:id/menu_done').click()



"""
driver.hide_keyboard()

time.sleep(2)
driver.quit()
