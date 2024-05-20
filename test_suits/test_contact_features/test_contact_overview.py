import pytest

from test_suits.test_contact_features.test_data import test_data_for_select_by_names, test_data_for_select_by_emails


class TestContactOverview:
    @pytest.mark.usefixtures("setup_contact_overview")
    @pytest.mark.parametrize("name, expected_res", test_data_for_select_by_names)
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