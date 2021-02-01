# The BasePage class initialisation
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """All other project page classes will inherit from this basic class"""
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """This function enables browser to open an url"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """The method to catch exceptions"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        else:
            print("Element is present")
        return True


