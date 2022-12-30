from selenium.webdriver import Remote as RemoteWebDriver
from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser: RemoteWebDriver, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how_to_find, what):
        try:
            self.browser.find_element(how_to_find, what)
        except NoSuchElementException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)