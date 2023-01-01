from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = MainPage(browser, link, 5)
    page.open()
    page.should_be_login_form()