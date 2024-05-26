import time

import pytest

from test_suits.test_contact_features.test_data import test_data_for_edit_contact, \
    test_data_for_edit_contact_with_error_message, test_data_for_select_by_names, test_data_for_select_by_emails


@pytest.mark.dependency(name="TestContactDetails",
                        depends=["TestAddContact::add_contact", "TestContactOverview::select_contact"])
class TestContactDetails:

    @pytest.mark.usefixtures("setup_contact_details")
    @pytest.mark.parametrize("new_contact_data", test_data_for_edit_contact)
    def test_edit_contact_with_valid_data(self, setup_contact_details, new_contact_data):
        contact_detail_page = setup_contact_details
        contact_detail_page.edit_contact_data(new_contact_data)
        contact_detail_page.submit()
        time.sleep(1)  # for load time
        edited_contact = contact_detail_page.get_contact_info()
        for key, value in new_contact_data.items():
            assert value == edited_contact[key], contact_detail_page.logger.warn(f"Check entry {key} failed")
            contact_detail_page.logger.info(f"Check entry {key} passed")

    @pytest.mark.usefixtures("setup_contact_details")
    @pytest.mark.parametrize("new_contact_data, expected_error_msg", test_data_for_edit_contact_with_error_message)
    def test_edit_contact_with_invalid_data(self, setup_contact_details, new_contact_data, expected_error_msg):
        contact_detail_page = setup_contact_details
        contact_detail_page.edit_contact_data(new_contact_data)
        contact_detail_page.submit()
        got_error_msg = contact_detail_page.get_error_message()
        assert expected_error_msg in got_error_msg, contact_detail_page.logger.warn("Check Failed")
        contact_detail_page.logger.info("Check Passed")

    @pytest.mark.usefixtures("setup_contact_overview")
    @pytest.mark.parametrize("name, expected_res", test_data_for_select_by_names)
    @pytest.mark.dependency(name="select_contact", depends=["TestAddContact::add_contact"])
    def test_select_contact_by_name(self, setup_contact_overview, name, expected_res):
        contact_over_page = setup_contact_overview
        assert contact_over_page.select_contact_by_name(name) == expected_res, contact_over_page.logger.warn("FAILED")
        contact_over_page.logger.info("PASSED")

    @pytest.mark.usefixtures("setup_contact_overview")
    @pytest.mark.parametrize("email, expected_res", test_data_for_select_by_emails)
    def test_select_contact_by_email(self, setup_contact_overview, email, expected_res):
        contact_over_page = setup_contact_overview
        assert contact_over_page.select_contact_by_email(email) == expected_res, contact_over_page.logger.warn("FAILED")
        contact_over_page.logger.info("PASSED")

    @pytest.mark.usefixtures("setup_contact_overview")
    def test_title(self, setup_contact_overview):
        contact_over_page = setup_contact_overview
        assert "My Contacts" == contact_over_page.title(), contact_over_page.logger.warn("FAILED")
        contact_over_page.logger.info("PASSED")

    @pytest.mark.dependency(depends=["select_contact"])
    @pytest.mark.usefixtures("setup_contact_details")
    def test_delete_contact(self, setup_contact_details):
        contact_detail_page = setup_contact_details
        contact_detail_page.delete_contact()
        time.sleep(1)
        assert "My Contacts" == contact_detail_page.title(), contact_detail_page.logger.warn("Check Failed")
        contact_detail_page.logger.info("Check Passed")