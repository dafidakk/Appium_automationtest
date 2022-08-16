# adb shell
# dumpsys window windows | grep -E 'mCurrentFocus'

# alternative : adb shell dumpsys window | findstr mCurrentFocus    !!!!!!!1


# find already runnig server appium : netstat -aon | findstr 4723
# kill that by id : taskkill /f /pid 2512

#uıautomator path = "C:\Users\User(You)\AppData\Local\Android\Sdk\tools\bin\uiautomatorviewer.bat"


# find running port       netstat -ano|findstr "PID :4723"
# kill port               taskkill /pid 3548 /f


# FOR REPORTS
#pip install pytest-html
#pytest test_appium_integration.py --html=testreport.html
#it has to be at the same venv directory
# ALLURE REPORT
# install allure from : https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.18.1/
# add bin folder PATH directory to system environments C:\Users\amper\Downloads\allure-2.18.1\bin
# add allure:pytest in pycharm
# generate report and run command below
# allure serve ./allurereports

# Screen shot
# conftest settings and fixtures
# conftest global settings
