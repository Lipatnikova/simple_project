import allure
from appium.webdriver.common.appiumby import AppiumBy
from utils.appium_base import AppiumBase


class MainScr(AppiumBase):
    SECTION_MORE_TO_LOVE = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="com.alibaba.aliexpresshd:id/title" and @text="More To Love"]'
    )

    # side menu
    MENU_LIST = (AppiumBy.ID, 'com.alibaba.aliexpresshd:id/navdrawer_items_list')

    def load_screen(self) -> None:
        with allure.step("Подождать загрузку Главного экрана"):
            self.element_is_visible(self.SECTION_MORE_TO_LOVE)

    def open_side_menu_with_swipe(self) -> None:
        with allure.step("Сделать свайп вправо от левого края"):
            self.perform_swipe(10, 800, 850, 800)

    def close_side_menu_with_swipe(self) -> None:
        with allure.step("Сделать свайп влево"):
            self.perform_swipe(960, 800, 350, 800)

    def verify_side_menu_is_displayed(self) -> bool:
        with allure.step("Проверить отображение бокового меню"):
            return self.is_element_displayed(self.MENU_LIST)
