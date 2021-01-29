# The BasePage class initialisation

class BasePage:
    """All other project page classes will inherit from this basic class"""
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """This function enables browser to open an url"""
        self.browser.get(self.url)

