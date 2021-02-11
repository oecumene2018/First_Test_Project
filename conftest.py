import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help="Choose language version: ru, en-gb, es, fr (etc.)")


@pytest.fixture(scope='function')
# Можно в фикстуре browser файла conftest указать вместо function указать module или session (все это проходили изучая фикстуры)
#     и в тестe (test_product_page.py) первым действием очистку куки
#         def test_guest_can_add_product_to_basket(browser, link):
#         browser.delete_all_cookies()
#     Тогда тест пройдет в одном браузере и не будет считать сумму добавленных товаров."""
def browser(request):
    browser_name = request.config.getoption('browser_name')
    version_lang = request.config.getoption('language')
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs',
                                        {'intl.accept_languages': version_lang})
        print(f"\nStarting browser for testing {version_lang} version...")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', version_lang)
        print(f"\nStarting browser for testing {version_lang} version...")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print(f"Browser {version_lang} still is not implemented")
    yield browser
    print("\nQuitting browser...")
    browser.quit()
