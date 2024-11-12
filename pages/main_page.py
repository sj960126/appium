from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy  # AppiumBy로 변경

class MainPage(BasePage):
    # 요소 정의
    CATEGORY = (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.nolbal.nolbal:id/main_tab_item_layout"])[4]')   

    # 메서드 정의
    def tap_category_button(self):
        self.click(self.CATEGORY)
