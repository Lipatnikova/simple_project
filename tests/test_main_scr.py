import allure
import pytest

from screens.main_scr import MainScr


class TestMainScr:
    @pytest.mark.basic_autotests
    @allure.epic("Главный экран")
    @allure.feature("Боковое меню")
    @allure.title("Открытие бокового меню свайпом")
    @allure.severity(allure.severity_level.MINOR)
    @allure.testcase("W_2_3")
    @allure.description("""
        Цель: проверить открытие бокового меню свайпом.
        Предусловие: открыт главный экран приложения.
        Шаги:
        1. Сделать свайп вправо от левого края.
        2. Проверить, что отображается боковое меню.
        3. Сделать свайп влево.
        4. Проверить, что боковое меню закрылось. """
                        )
    def test_opening_side_menu_by_swiping(self, driver):
        scr = MainScr(driver)
        scr.load_screen()
        scr.open_side_menu_with_swipe()
        with allure.step("Проверить, что отображается боковое меню"):
            assert scr.verify_side_menu_is_displayed(), \
                "The side menu does not appear after swiping from left to right"
        scr.close_side_menu_with_swipe()
        with allure.step("Проверить, что боковое меню закрылось"):
            assert scr.verify_side_menu_is_displayed() is False, \
                "The side menu after swiping from the right edge to the left is displayed"

    @pytest.mark.basic_autotests
    @allure.epic("Главный экран")
    @allure.feature("Боковое меню")
    @allure.title("Открытие бокового меню свайпом 2")
    @allure.severity(allure.severity_level.MINOR)
    @allure.testcase("W_2_3")
    @allure.description("""
            Цель: проверить открытие бокового меню свайпом.
            Предусловие: открыт главный экран приложения.
            Шаги:
            1. Сделать свайп вправо от левого края.
            2. Проверить, что отображается боковое меню.
            3. Сделать свайп влево.
            4. Проверить, что боковое меню закрылось. """
                        )
    def test_opening_side_menu_by_swiping_2(self, driver):
        scr = MainScr(driver)
        scr.load_screen()
        scr.open_side_menu_with_swipe()
        with allure.step("Проверить, что отображается боковое меню"):
            assert scr.verify_side_menu_is_displayed(), \
                "The side menu does not appear after swiping from left to right"
        scr.close_side_menu_with_swipe()
        with allure.step("Проверить, что боковое меню закрылось"):
            assert scr.verify_side_menu_is_displayed() is False, \
                "The side menu after swiping from the right edge to the left is displayed"

