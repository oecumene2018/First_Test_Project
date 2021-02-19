from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket_text(self):
        """Check that there is a text that basket is empty"""
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket is not empty - no empty basket text."
        print("There is the text that basket is empty, on the basket page.")

    def should_not_see_empty_basket_text(self):
        """Check that there is no text that basket is empty"""
        assert self.is_not_element_present(**BasketPageLocators.BASKET_EMPTY), \
            "There is a text that that basket is empty on the Basket page, but it should not be there"

    def should_empty_basket_text_disappear(self):
        """Check that the text that basket is empty has disappeared from the Basket page"""
        assert self.is_disappeared(*BasketPageLocators.BASKET_EMPTY), \
            "The text that basket is empty has not disappeared from the Basket page, but it should"


