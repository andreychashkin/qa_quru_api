from appium import webdriverfrom appium.options.android import UiAutomator2Optionsfrom appium.webdriver.common.appiumby import AppiumByfrom selenium.webdriver.support.ui import WebDriverWaitfrom selenium.webdriver.support import expected_conditions as ECimport timeoptions = UiAutomator2Options().load_capabilities({    "app": "bs://9d156b7ab338b3abbc2544d926f0eb6429bac7b3",    "platformVersion": "9.0",    "deviceName": "Google Pixel 3",                      'bstack:options':{    "projectName": "First Python project",    "buildName": "browserstack-build-1",    "sessionName": "BStack first_test",    "userName": "nestandarta_MfC84h",    "accessKey": "vLEPd9hHNiYSD8VNJcCP"}})driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)