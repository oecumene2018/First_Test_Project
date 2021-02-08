from selenium.webdriver.common.by import By


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
    PRODUCT_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    SUCCESS_ALERT = (By.CLASS_NAME, "alertinner")


