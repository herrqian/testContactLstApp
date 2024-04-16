import pytest

from utils.pages.LoginPage import LoginPage


def test_signup_with_invalid_input(setup):
    login_page = LoginPage(setup)

    login_page.signup()


def test_title(setup):
    login_page = LoginPage(setup)
    expected_res = "Contact List App"
    got_res = login_page.title()
    login_page.logger.info(f"Expected Title of Website = {expected_res}")
    login_page.logger.info(f"Get Title of Website = {got_res}")
    if expected_res == got_res:
        login_page.logger.info("PASSED")
    else:
        login_page.logger.warn("FAILED")
