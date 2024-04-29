import pytest

from test_suits.test_login_page.test_data import invalid_credentials, valid_credentials


class TestSignUp:
    @pytest.mark.usefixtures("setup_signup")
    @pytest.mark.parametrize("credentials", invalid_credentials)
    def test_signup_with_invalid_credentials(self, setup_signup, credentials):
        signup_page = setup_signup
        signup_page.signup(credentials)
        expected_res = True
        got_res = signup_page.is_signup_failed()
        assert expected_res == got_res, signup_page.logger.warn("FAILED")
        signup_page.logger.info("PASSED")
        del signup_page

    @pytest.mark.usefixtures("setup_signup")
    @pytest.mark.parametrize("credentials", valid_credentials)
    def test_sign_up_with_valid_credentials(self, setup_signup, credentials):
        signup_page = setup_signup
        signup_page.signup(credentials)
        expected_res = True
        got_res = signup_page.is_signup_succeed()
        assert expected_res == got_res, signup_page.logger.warn("FAILED")
        signup_page.logger.info("PASSED")
        del signup_page
