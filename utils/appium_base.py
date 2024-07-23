from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

from config.config import Config


class AppiumBase:
    def __init__(self, driver):
        """This method initializes the BasePage object"""
        self.driver = driver

    def element_is_present(
            self, locator: WebElement or tuple[str, str], timeout: int = Config.WAIT_TIMEOUT
    ) -> WebElement:
        """
        This method expects to verify that the element is present in the DOM tree,
        but not necessarily visible and displayed on the page.
        Locator - is used to find the element.
        Timeout - the duration it will wait for.
        """
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_visible(
            self, locator: WebElement or tuple[str, str], timeout: int = Config.WAIT_TIMEOUT
    ) -> WebElement:
        """
        This method expects to verify that the element is present in the DOM tree, visible, and displayed on the page.
        Visibility means that the element is not only displayed but also has a height and width greater than 0.
        Locator - is used to find the element.
        Timeout - the duration it will wait for.
        """
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def is_element_displayed(self, locator: WebElement or tuple[str, str]) -> bool:
        """
        This method checks if the specified element is displayed on the webpage.
        It uses the element_is_displayed method to find the element and returns True
        if the element is displayed within the specified timeout, otherwise, it returns False.
        """
        try:
            element = self.element_is_visible(locator)
            return element.is_displayed()
        except TimeoutException:
            return False

    def perform_swipe(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """
        Perform a swipe action on the screen.
        x1 - starting x-coordinate of the swipe.
        y1 - starting y-coordinate of the swipe.
        x2 - ending x-coordinate of the swipe.
        y2 - ending y-coordinate of the swipe.
        """
        self.driver.swipe(x1, y1, x2, y2)
