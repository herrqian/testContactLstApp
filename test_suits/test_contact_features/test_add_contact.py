import time

import pytest

from test_suits.test_contact_features.test_data import invalid_test_contacts, valid_test_contacts


class TestAddContact:
    @pytest.mark.usefixtures("setup_add_contact")
    @pytest.mark.parametrize("contact, expected_err", invalid_test_contacts)
    def test_add_contact_with_invalid_data(self, setup_add_contact, contact, expected_err):
        add_contact_page = setup_add_contact
        add_contact_page.add_contact(contact)
        add_contact_page.click()
        error_msg = add_contact_page.get_error_message()
        assert expected_err in error_msg, add_contact_page.logger.warn("FAILED")
        add_contact_page.logger.info("SUCCEED")

    @pytest.mark.usefixtures("setup_add_contact")
    @pytest.mark.parametrize("contact", valid_test_contacts)
    def test_add_contact_with_valid_data(self, setup_add_contact, contact):
        add_contact_page = setup_add_contact
        add_contact_page.add_contact(contact)
        add_contact_page.click()
        time.sleep(1)
        assert add_contact_page.title() != "Add Contact", add_contact_page.logger.warn("FAILED")
        add_contact_page.logger.info("SUCCEED")
