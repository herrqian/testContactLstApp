import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.constants.common import LOCATE_BY_XPATH, LOCATE_BY_ID
from utils.logger.LoggerUtils import set_logger
from utils.pages.BasePage import BasePage


class ContactDetailPage(BasePage):
    _first_name_locator = (LOCATE_BY_XPATH, '//*[@id="firstName"]')
    _last_name_locator = (LOCATE_BY_XPATH, '//*[@id="lastName"]')
    _birth_date_locator = (LOCATE_BY_XPATH, '//*[@id="birthdate"]')
    _email_locator = (LOCATE_BY_XPATH, '//*[@id="email"]')
    _phone_locator = (LOCATE_BY_XPATH, '//*[@id="phone"]')
    _street_one_locator = (LOCATE_BY_XPATH, '//*[@id="street1"]')
    _street_two_locator = (LOCATE_BY_XPATH, '//*[@id="street2"]')
    _city_locator = (LOCATE_BY_XPATH, '//*[@id="city"]')
    _state_province_locator = (LOCATE_BY_XPATH, '//*[@id="stateProvince"]')
    _post_locator = (LOCATE_BY_XPATH, '//*[@id="postalCode"]')
    _country_locator = (LOCATE_BY_XPATH, '//*[@id="country"]')
    _submit_locator = (LOCATE_BY_XPATH, '//*[@id="submit"]')
    _cancel_locator = (LOCATE_BY_XPATH, '//*[@id="cancel"]')
    _error_locator = (LOCATE_BY_XPATH, '//*[@id="error"]')

    _edit_button_locator = (LOCATE_BY_ID, "edit-contact")
    _delete_button_locator = (LOCATE_BY_ID, "delete")
    _return_button_locator = (LOCATE_BY_ID, "return")

    _mapping_table = {
        "firstname": _first_name_locator,
        "lastname": _last_name_locator,
        "birthdate": _birth_date_locator,
        "email": _email_locator,
        "phone": _phone_locator,
        "streetOne": _street_one_locator,
        "streetTwo": _street_two_locator,
        "city": _city_locator,
        "stateProvince": _state_province_locator,
        "post": _post_locator,
        "country": _country_locator,
    }

    def __init__(self, driver):
        super().__init__(driver, set_logger(__name__))

    def edit_contact_data(self, new_contact_data: dict):
        self.wait_element_to_be_clickable(self.driver, *self._edit_button_locator)
        self.logger.info("Click the edit contact button")
        self.find_element(self.driver, *self._edit_button_locator).click()
        self.wait_element_to_be_clickable(self.driver, *self._submit_locator)
        # ensure the text of contact is displayed
        time.sleep(0.1)
        for key, value in new_contact_data.items():
            self._set_value(self._mapping_table[key], value)

    def _set_value(self, web_ele, value):
        element = self.find_element(self.driver, *web_ele)
        element.clear()
        element.send_keys(value)

    def submit(self):
        self.find_element(self.driver, *self._submit_locator).click()

    def cancel(self):
        self.find_element(self.driver, *self._cancel_locator).click()

    def get_error_message(self):
        self.wait_element_to_be_visible(self.driver, *self._error_locator)
        return self.find_element(self.driver, *self._error_locator).text

    def title(self):
        return self.driver.title

    def delete_contact(self):
        self.find_element(self.driver, *self._delete_button_locator).click()
        WebDriverWait(self.driver, 3).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')
        delete_altert = self.driver.switch_to.alert
        delete_altert.accept()
        self.logger.info("Delete action confirmed")

    def return_to_contact_list(self):
        self.find_element(self.driver, *self._return_button_locator).click()

    def get_contact_info(self):
        contact = {}
        for key, value in self._mapping_table.items():
            contact[key] = self.find_element(self.driver, *value).text
        return contact
