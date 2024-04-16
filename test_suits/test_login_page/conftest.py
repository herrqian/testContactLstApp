from typing import Union

import pytest
from selenium import webdriver
from selenium.webdriver import Chrome, Firefox, Edge


@pytest.fixture(scope="module")
def setup() -> Union[Chrome, Firefox, Edge]:
    driver = webdriver.Chrome()
    driver.get("https://thinking-tester-contact-list.herokuapp.com/login")
    return driver
