# Implementation of the Page Object for the Main Page.

from .base_page import BasePage


class MainPage(BasePage):
    """Class MainPage inherits from parent (super) class BasePage."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




