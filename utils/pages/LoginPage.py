from utils.constants.common import *
from utils.constants.login import LOGIN_FAILED
from utils.locators.login_locators import *
from utils.logger.LoggerUtils import set_logger
from utils.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, set_logger(__name__))

    def login(self, email, password):
        """
        Type email and password, Click the submit button to perform login action
        :return: None
        """
        self._set_email(email)
        self._set_password(password)
        self.logger.info("Click the submit button")
        self.find_element(self.driver, "ID", SUBMIT).click()

    def signup(self):
        """
        Click the signup button
        :return:
        """
        self.find_element(self.driver, "ID", SIGNUP).click()

    def _set_email(self, email: str):
        """
        Fill the email field
        :param email
        :return:
        """
        self.find_element(self.driver, "ID", EMAIL).clear()
        self.logger.info(f"Set email to {email}")
        self.find_element(self.driver, "ID", EMAIL).send_keys(email)

    def _set_password(self, password: str):
        """
        Fill the password field
        :param password:
        :return:
        """
        self.find_element(self.driver, "ID", PASSWORD).clear()
        self.logger.info(f"Set password to {password}")
        self.find_element(self.driver, "ID", PASSWORD).send_keys(password)

    def title(self):
        return self.driver.title

    def is_login_failed(self):
        self.wait_element_to_be_visible(self.driver, LOCATE_BY_ID, ERROR)
        err_text = self.find_element(self.driver, LOCATE_BY_ID, ERROR).text
        self.logger.info(f"Error message in span = {err_text}")
        return err_text == LOGIN_FAILED

    def is_login_succeed(self):
        self.wait_element_to_be_visible(self.driver, LOCATE_BY_XPATH, "/html/body/div/header/h1")
        self.logger.info(f"Title of this site = {self.driver.title}")
        return "My Contacts" in self.driver.title
