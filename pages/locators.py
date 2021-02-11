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
    SUCCESS_ALERT = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRICE_SUCCESS_ALERT = (By.XPATH, "//div[@id='messages']//strong")
    # PRODUCT_LINKS = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    #                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    #                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    #                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    #                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    #                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    #                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    #                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    #                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    #                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]




