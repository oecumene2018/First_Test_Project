from .base_page import BasePage
from .locators import MainPageLocators


class AccountPage(BasePage):
    """Class MainPage inherits from parent (super) class BasePage."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)