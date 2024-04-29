import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.pages.LoginPage import LoginPage
from utils.pages.SignUpPage import SignUpPage


@pytest.fixture(scope="function")
def setup_signin() -> LoginPage:
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
    login_page = LoginPage(driver)
    yield login_page

    driver.quit()
    del login_page
    del driver


@pytest.fixture(scope="function")
def setup_signup() -> SignUpPage:
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://thinking-tester-contact-list.herokuapp.com/addUser")
    signup_page = SignUpPage(driver)
    yield signup_page

    driver.quit()
    del signup_page
    del driver
