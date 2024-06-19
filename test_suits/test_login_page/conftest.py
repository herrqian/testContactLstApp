import pytest
from selenium import webdriver

from utils.pages.LoginPage import LoginPage
from utils.pages.SignUpPage import SignUpPage


def setup_driver():
    selenium_remote_url = "http://localhost:4444/wd/hub"
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor=selenium_remote_url, options=options)
    return driver


@pytest.fixture(scope="function")
def setup_signin() -> LoginPage:
    driver = setup_driver()
    driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
    login_page = LoginPage(driver)
    yield login_page

    driver.quit()
    del login_page
    del driver


@pytest.fixture(scope="function")
def setup_signup() -> SignUpPage:
    driver = setup_driver()
    driver.get("https://thinking-tester-contact-list.herokuapp.com/addUser")
    signup_page = SignUpPage(driver)
    yield signup_page

    driver.quit()
    del signup_page
    del driver
