import pytest
from selenium import webdriver

from test_suits.test_contact_features.test_data import COOKIE
from utils.pages.AddContactPage import AddContactPage


@pytest.fixture(scope="function")
def setup_add_contact() -> AddContactPage:
    driver = webdriver.Chrome()
    # first of all, visit the login page or any page without permission
    # see https://stackoverflow.com/questions/59877561/selenium-common-exceptions-invalidcookiedomainexception-message-invalid-cookie
    driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
    # add cookie
    driver.add_cookie(COOKIE)
    # get the addContact page
    driver.get("https://thinking-tester-contact-list.herokuapp.com/addContact")
    add_contact_page = AddContactPage(driver)
    yield add_contact_page

    driver.quit()
    del add_contact_page
    del driver
