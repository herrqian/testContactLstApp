import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    selenium_remote_url = "http://localhost:4444/wd/hub"
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor=selenium_remote_url, options=options)
    yield driver
    driver.quit()


def test_google_title(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title
