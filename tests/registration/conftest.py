import pytest

from framework.registration_page import RegistrationPage


@pytest.fixture(scope="function")
def user_registration_fixture(driver):
    driver.launch_app()
    yield RegistrationPage(driver)
    driver.close_app()
