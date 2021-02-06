# Implementation of the Page Object for the Main Page.

from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    """Class MainPage inherits from parent (super) class BasePage."""

    def go_to_login_page(self):
        """The method argument is self as we will inherit that from the superclass.
        Self=BasePage points at a class instance used."""

        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        """The method checks that there is a login page link on the Main page."""

        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not present"



