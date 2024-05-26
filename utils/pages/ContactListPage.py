from selenium.webdriver.common.by import By

from utils.constants.common import LOCATE_BY_XPATH
from utils.logger.LoggerUtils import set_logger
from utils.pages.BasePage import BasePage


class ContactListPage(BasePage):
    _contact_list = (LOCATE_BY_XPATH, '//*[@id="myTable"]/tr')
    _contact_by_name_locator = (By.XPATH, '//*[@id="myTable"]/tr/td[2]')
    _contact_by_email_locator = (By.XPATH, '//*[@id="myTable"]/tr/td[4]')
    _contact_entry = (By.CLASS_NAME, "contactTableBodyRow")

    def __init__(self, driver):
        super().__init__(driver, set_logger(__name__))

    def title(self):
        return self.driver.title

    def select_contact_by_name(self, name):
        self.driver.implicitly_wait(5)
        web_eles = self.driver.find_elements(*self._contact_by_name_locator)
        for web_ele in web_eles:
            if name == web_ele.text:
                self.logger.info(f"Contact with name {name} is selected by clicking")
                web_ele.click()
                return True

        self.logger.info(f"Contact with name {name} is not found")
        return False

    def select_contact_by_email(self, email):
        self.driver.implicitly_wait(5)
        web_eles = self.driver.find_elements(*self._contact_by_email_locator)
        for web_ele in web_eles:
            if email == web_ele.text:
                self.logger.info(f"Contact with name {email} is selected by clicking")
                web_ele.click()
                return True

        self.logger.info(f"Contact with name {email} is not found")
        return False
