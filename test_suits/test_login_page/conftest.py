from typing import Union

import pytest
from selenium import webdriver
from selenium.webdriver import Chrome, Firefox, Edge


@pytest.fixture(scope="function")
def setup_signin() -> Union[Chrome, Firefox, Edge]:
    driver = webdriver.Chrome()
    driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
    return driver


@pytest.fixture(scope="function")
def setup_signup() -> Union[Chrome, Firefox, Edge]:
    driver = webdriver.Chrome()
    driver.get("https://thinking-tester-contact-list.herokuapp.com/addUser")
    return driver
