from utils.logger.LoggerUtils import set_logger
from utils.pages.BasePage import BasePage


class AddContactPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, set_logger(__name__))

    def add_contact(self, contact: dict):
        pass


