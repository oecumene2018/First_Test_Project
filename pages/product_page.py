from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_add_product_to_basket(self):
        """"Check that product has been added to basket"""

        self.should_be_message_product_added_to_basket()
        self.should_be_same_price_page_and_basket()

    def should_be_message_product_added_to_basket(self):
        """Check there's a message of the product added to basket.
            Name of the product and name in basket are same"""

        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
               self.browser.find_element(*ProductPageLocators.SUCCESS_ALERT).text, "No message that product is in basket"

    def should_be_same_price_page_and_basket(self):
        """Check that price in basket is same with the product price"""

        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in \
               self.browser.find_element(*ProductPageLocators.PRICE_SUCCESS_ALERT).text, "Wrong price in basket"

    def should_not_see_success_message(self):
        """Check that there is no success message on page"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT), \
            "There is a success message, but should not be"

    def should_message_disappear(self):
        """Check that there is no success message on page"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ALERT), \
            "Success message not disappeared, but it should"

    def should_be_login_link(self):
        """Check that there is a login link on a product page"""
        assert self.is_element_present(*ProductPageLocators.LOGIN_LINK), "No login link on the product page"




