from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


class AppiumSetup:
    
    def __init__(self):
        self.driver = None

    def start_driver(self):
        # Appium 서버 설정
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = "emulator-5554"
        options.app = "/Users/songhyeonsu/dev/hedge-android/presentation/debug/presentation-debug.apk"
        options.app_package = "com.hadge.hadge_android"
        options.app_activity = ".features.main.screen.container.MainActivity"
        options.automation_name = "UiAutomator2"
        options.new_command_timeout = 30  # 새로운 명령에 대한 타임아웃 설정

        # Appium 서버에 연결
        self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)  # timeout은 options로 설정
        self.driver.implicitly_wait(10)  # 암묵적 대기 설정

        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
