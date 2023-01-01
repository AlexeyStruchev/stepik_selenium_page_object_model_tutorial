from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link, 5)
    page.open()
    page.should_be_login_form()

def test_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link, 5)
    page.open()
    page.should_be_register_form()

def test_should_be_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link, 5)
    page.open()
    page.should_be_login_url()

def test_should_be_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link, 5)
    page.open()
    page.should_be_login_page()