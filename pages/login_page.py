from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """реализуйте проверку на корректный url адрес"""
        url = self.browser.current_url
        assert all(sub_str in url for sub_str in ("http://selenium1py.pythonanywhere.com", "/accounts/login/")), \
            "Not the login page url"
        print("It is the loging url")

    def should_be_login_form(self):
        """реализуйте проверку, что есть форма логина"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not present"

    def register_new_user(self, email, password):
        """Method to create a new fake user"""
        self.browser.find_element(By.ID, 'id_registration-email').send_keys(email)
        self.browser.find_element(By.ID, 'id_registration-password1').send_keys(password)
        self.browser.find_element(By.ID, 'id_registration-password2').send_keys(password)
        submit_button = self.browser.find_element(By.NAME, 'registration_submit')
        submit_button.click()






