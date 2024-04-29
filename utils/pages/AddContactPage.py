from utils.constants.common import LOCATE_BY_XPATH
from utils.logger.LoggerUtils import set_logger
from utils.pages.BasePage import BasePage


class AddContactPage(BasePage):
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

    def add_contact(self, contact: dict):
        for key, value in contact.items():
            self._set_value(self._mapping_table[key], value)

    def _set_value(self, web_ele, value):
        element = self.find_element(self.driver, *web_ele)
        element.clear()
        # self.logger.infor(f"Set {element} to {value}")
        element.send_keys(value)

    def click(self):
        self.find_element(self.driver, *self._submit_locator).click()

    def cancel(self):
        self.find_element(self.driver, *self._cancel_locator).click()

    def get_error_message(self):
        self.wait_element_to_be_visible(self.driver, *self._error_locator)
        return self.find_element(self.driver, *self._error_locator).text

    def title(self):
        return self.driver.title
