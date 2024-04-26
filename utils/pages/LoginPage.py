from utils.data.login_data import LOGIN_FAILED
from utils.logger.LoggerUtils import set_logger
from utils.pages.BasePage import BasePage
from utils.locators.login_locators import *


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
        self.find_element(self.driver, "ID", EMAIL).send_keys(email)

    def _set_password(self, password: str):
        """
        Fill the password field
        :param password:
        :return:
        """
        self.find_element(self.driver, "ID", PASSWORD).clear()
        self.find_element(self.driver, "ID", PASSWORD).send_keys(password)

    def title(self):
        return self.driver.title

    def is_login_failed(self):
        return self.find_element(self.driver, "ID", ERROR).text == LOGIN_FAILED
