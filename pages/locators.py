from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/accounts/login/"


class ProductPageLocators:
    ADD_PRODUCT_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, "//*[@class='col-sm-6 product_main']/h1")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    SUCCESS_ALERT = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRICE_SUCCESS_ALERT = (By.XPATH, "//div[@id='messages']//strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
    PRODUCT_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    PRODUCT_PAGE_TEST_LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")



