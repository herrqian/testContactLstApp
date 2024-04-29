import pytest

from test_suits.test_login_page.test_data import login_data


class TestSignIn:

    @pytest.mark.usefixtures("setup_signin")
    def test_title(self, setup_signin):
        login_page = setup_signin
        expected_res = "Contact List App"
        got_res = login_page.title()
        login_page.logger.info(f"Expected Title of Website = {expected_res}")
        login_page.logger.info(f"Get Title of Website = {got_res}")
        assert expected_res == got_res, login_page.logger.warn("FAILED")
        login_page.logger.info("PASSED")

    @pytest.mark.usefixtures("setup_signin")
    @pytest.mark.parametrize("email, password, expected_res", login_data)
    def test_login(self, setup_signin, email, password, expected_res):
        login_page = setup_signin
        login_page.login(email, password)
        if expected_res == "SUCCEED":
            assert login_page.is_login_succeed(), login_page.logger.warn("FAILED")
            login_page.logger.info("PASSED")
        elif expected_res == "FAILED":
            assert login_page.is_login_failed(), login_page.logger.warn("FAILED")
            login_page.logger.info("PASSED")
        else:
            assert False, login_page.logger.error("Unexpected input data")
