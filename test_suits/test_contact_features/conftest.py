import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from test_suits.test_contact_features.test_data import COOKIE
from utils.pages.AddContactPage import AddContactPage
from utils.pages.ContactDetailPage import ContactDetailPage
from utils.pages.ContactListPage import ContactListPage


@pytest.fixture(scope="function")
def setup_add_contact() -> AddContactPage:
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
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


@pytest.fixture(scope="function")
def setup_contact_overview() -> ContactListPage:
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    # first of all, visit the login page or any page without permission
    # see https://stackoverflow.com/questions/59877561/selenium-common-exceptions-invalidcookiedomainexception-message-invalid-cookie
    driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
    # add cookie
    driver.add_cookie(COOKIE)
    # get the addContact page
    driver.get("https://thinking-tester-contact-list.herokuapp.com/contactList")
    contact_list_page = ContactListPage(driver)
    yield contact_list_page

    driver.quit()
    del contact_list_page
    del driver


@pytest.fixture(scope="function")
def setup_contact_details() -> ContactDetailPage:
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
    # add cookie
    driver.add_cookie(COOKIE)
    # get the addContact page
    driver.get("https://thinking-tester-contact-list.herokuapp.com/contactList")
    contact_list_page = ContactListPage(driver)
    contact_list_page.select_contact_by_name("abc efd")
    contact_details_page = ContactDetailPage(driver)
    yield contact_details_page

    driver.quit()
    del contact_list_page
    del driver
