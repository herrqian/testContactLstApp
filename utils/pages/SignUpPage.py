from selenium.webdriver.common.by import By

from utils.locators.signup_locators import FIRST_NAME, LAST_NAME, EMAIL, ERROR, PASSWORD, SUBMIT_BTN
from utils.pages.BasePage import BasePage


class SignUpPage(BasePage):

    def check_title(self):
        return "Add User" in self.driver.title

    def signup(self, credentials):
        self.__set_first_name(credentials["FIRST_NAME"])
        self.__set_last_name(credentials["LAST_NAME"])
        self.__set_email(credentials["EMAIL"])
        self.__set_password(credentials["PASSWORD"])
        self.logger.info("Click the SUBMIT button")
        self.driver.find_element(By.XPATH, SUBMIT_BTN).click()

    def __set_first_name(self, first_name):
        self.driver.find_element(By.XPATH, FIRST_NAME).clear()
        self.logger.info(f"Set the first name = {first_name}")
        self.driver.find_element(By.XPATH, FIRST_NAME).send_keys(first_name)

    def __set_last_name(self, last_name):
        self.driver.find_element(By.XPATH, LAST_NAME).clear()
        self.logger.info(f"Set the last name = {last_name}")
        self.driver.find_element(By.XPATH, LAST_NAME).send_keys(last_name)

    def __set_email(self, email):
        self.driver.find_element(By.XPATH, EMAIL).clear()
        self.logger.info(f"Set the email = {email}")
        self.driver.find_element(By.XPATH, EMAIL).send_keys(email)

    def __set_password(self, password):
        self.driver.find_element(By.XPATH, PASSWORD).clear()
        self.logger.info(f"Set the password = {password}")
        self.driver.find_element(By.XPATH, PASSWORD).send_keys(password)

    def is_signup_failed(self):
        err_text = self.driver.find_element(By.ID, ERROR).text
        self.logger.info(f"Error message in span = {err_text}")
        return "User validation failed" in err_text

    def is_signup_succeed(self):
        self.logger.info(f"Title of this site = {self.driver.title}")
        return "My contact" in self.driver.title
