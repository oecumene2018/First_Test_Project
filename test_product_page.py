
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


def test_guest_can_add_product_to_basket(browser):

    page = ProductPage(browser, ProductPageLocators.PRODUCT_URL)
    page.open()
    add_button = browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
    add_button.click()
    page.solve_quiz_and_get_code()
    browser.implicitly_wait(3)
    page.should_be_message_product_added_to_basket()
    page.should_be_same_price_page_and_basket()




