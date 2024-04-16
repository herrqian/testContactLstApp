from utils.pages.BasePage import BasePage
from utils.locators.login_locators import *


class LoginPage(BasePage):

    def login(self):
        pass

    def signup(self):
        pass

    def set_email(self):
        pass

    def set_password(self):
        pass

    def title(self):
        return self.driver.title

    def error(self):
        return self.find_element(self.driver, "ID", ERROR)
