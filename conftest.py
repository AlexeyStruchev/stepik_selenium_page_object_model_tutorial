import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, ru, es, fr")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
