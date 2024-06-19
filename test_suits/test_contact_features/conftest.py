import pytest
from selenium import webdriver

from utils.pages.AddContactPage import AddContactPage
from utils.pages.ContactDetailPage import ContactDetailPage
from utils.pages.ContactListPage import ContactListPage
from utils.pages.LoginPage import LoginPage


def login(driver):
    login_page = LoginPage(driver)
    login_page.login("321@123.com", "12345678")

@pytest.fixture(scope="function")
def setup_add_contact() -> AddContactPage:
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=opts)
    # first of all, visit the login page or any page without permission
    # see https://stackoverflow.com/questions/59877561/selenium-common-exceptions-invalidcookiedomainexception-message-invalid-cookie
    driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
    # # add cookie
    # driver.add_cookie(COOKIE)
    # # get the addContact page
    # driver.get("https://thinking-tester-contact-list.herokuapp.com/addContact")
    login(driver)
    add_contact_page = AddContactPage(driver)
    yield add_contact_page

    driver.quit()
    del add_contact_page
    del driver


@pytest.fixture(scope="function")
def setup_contact_overview() -> ContactListPage:
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=opts)
    # first of all, visit the login page or any page without permission
    # see https://stackoverflow.com/questions/59877561/selenium-common-exceptions-invalidcookiedomainexception-message-invalid-cookie
    driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
    # # add cookie
    # driver.add_cookie(COOKIE)
    # # get the addContact page
    # driver.get("https://thinking-tester-contact-list.herokuapp.com/contactList")
    login(driver)
    contact_list_page = ContactListPage(driver)
    yield contact_list_page

    driver.quit()
    del contact_list_page
    del driver


@pytest.fixture(scope="function")
def setup_contact_details() -> ContactDetailPage:
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=opts)
    driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
    # # add cookie
    # driver.add_cookie(COOKIE)
    # # get the addContact page
    # driver.get("https://thinking-tester-contact-list.herokuapp.com/contactList")
    login(driver)
    contact_list_page = ContactListPage(driver)
    contact_list_page.select_contact_by_name("abc efd")
    contact_details_page = ContactDetailPage(driver)
    yield contact_details_page

    driver.quit()
    del contact_list_page
    del driver
