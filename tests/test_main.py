import unittest
from setup.appium_setup import AppiumSetup
from pages.main_page import MainPage

class MainTest(unittest.TestCase):
    def setUp(self):
        # Appium 드라이버 시작
        appium_setup = AppiumSetup()
        self.driver = appium_setup.start_driver()
        self.main_page = MainPage(self.driver)

    def tearDown(self):
        # Appium 드라이버 종료
        self.driver.quit()

    def tap_category_button(self):
        self.main_page.tap_category_button()

if __name__ == "__main__":
    unittest.main()
