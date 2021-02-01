# Implementation of the Page Object for the Main Page.

from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    """Class MainPage inherits from parent (super) class BasePage."""

    def go_to_login_page(self):
        """The method argument is self as we will inherit that from the superclass.
        Self=BasePage points at a class instance used."""
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        """The method checks that there is a login page link on the Main page."""
        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

