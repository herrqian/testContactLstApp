import pytest

from utils.pages.LoginPage import LoginPage
from utils.pages.SignUpPage import SignUpPage


def test_signup_with_invalid_credentials(setup_signup):
    signup_page = SignUpPage(setup_signup)
    credentials = {
        "FIRST_NAME": "ADAMS",
        "LAST_NAME": "SMITH",
        "EMAIL": "abc@123.de",
        "PASSWORD": "1234",
    }
    signup_page.signup(credentials)
    expected_res = True
    got_res = signup_page.is_signup_failed()
    if expected_res == got_res:
        signup_page.logger.info("PASSED")
    else:
        signup_page.logger.warn("FAILED")


def test_sign_up_with_valid_credentials(setup_signup):
    login_page = SignUpPage(setup_signup)


def test_title(setup_signin):
    login_page = LoginPage(setup_signin)
    expected_res = "Contact List App"
    got_res = login_page.title()
    login_page.logger.info(f"Expected Title of Website = {expected_res}")
    login_page.logger.info(f"Get Title of Website = {got_res}")
    if expected_res == got_res:
        login_page.logger.info("PASSED")
    else:
        login_page.logger.warn("FAILED")
