import pytest
from selenium import webdriver

from utils.pages.LoginPage import LoginPage
from utils.pages.SignUpPage import SignUpPage


@pytest.fixture(scope="function")
def setup_signin() -> LoginPage:
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=opts)
    driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
    login_page = LoginPage(driver)
    yield login_page

    driver.quit()
    del login_page
    del driver


@pytest.fixture(scope="function")
def setup_signup() -> SignUpPage:
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=opts)
    driver.get("https://thinking-tester-contact-list.herokuapp.com/addUser")
    signup_page = SignUpPage(driver)
    yield signup_page

    driver.quit()
    del signup_page
    del driver
