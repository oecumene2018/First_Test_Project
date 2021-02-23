import pytest
import time
from selenium.webdriver.common.by import By
from mimesis import Generic
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.account_page import AccountPage
from .pages.locators import ProductPageLocators, LoginPageLocators

link = ProductPageLocators.PRODUCT_PAGE_TEST_LOGIN_URL


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                                marks=pytest.mark.xfail(reason="Wrong book name in basket")),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser):
    # browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()
    add_button = browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
    add_button.click()
    # page.solve_quiz_and_get_code()
    # browser.implicitly_wait(10)
    page.should_be_message_product_added_to_basket()
    page.should_be_same_price_page_and_basket()


@pytest.mark.xfail(reason="Negative test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()
    add_button = browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
    add_button.click()
    page.should_not_see_success_message()


@pytest.mark.xfail(reason="Negative test")
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_see_success_message()


@pytest.mark.xfail(reason="Negative test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    # browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()
    add_button = browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
    add_button.click()
    page.should_message_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket_text()


class FakeUser:
    """The calls allows emulating fake user data using the Mimesis module."""
    def __init__(self):
        generic = Generic('en')
        self.email = generic.person.email()
        self.password = generic.person.password(10)


# Test scenarios for registered users.
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = LoginPageLocators.LOGIN_PAGE_URL
        page = LoginPage(browser, url)
        page.open()
        new_user = FakeUser()
        page.register_new_user(new_user.email, new_user.password)
        page.should_be_authorised_user()

    def test_user_can_add_product_to_basket(self, browser):
        # browser.delete_all_cookies()
        page = ProductPage(browser, link)
        page.open()
        add_button = browser.find_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)
        add_button.click()
        page.should_be_message_product_added_to_basket()
        page.should_be_same_price_page_and_basket()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_see_success_message()