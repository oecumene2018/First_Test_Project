# The BasePage class initialisation
import math
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


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

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs(12*math.sin(float(x)))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
