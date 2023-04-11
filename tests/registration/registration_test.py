import pytest


@pytest.mark.parametrize(
    'username, email, email_confirm, phone_number, password, password_confirm, expected_result',
    [pytest.param(
        'Roman Kakhnii',
        'super.rk76@gmail.com',
        'super.rk76@gmail.com',
        '992145170',
        'Roman123445!',
        'Roman123445!',
        True,
        id='All data is entered correctly'
    ), pytest.param(
        'Roman Kakhnii',
        'super.rk76@gmail.com',
        'super@gmail.com',
        '992145170',
        'Roman123445!',
        'Roman123445!',
        False,
        id='Incorrect email confirmation'
    ), pytest.param(
        'Roman Kakhnii',
        'super.rk76@gmail.com',
        'super.rk76@gmail.com',
        '992145170',
        'Roman123445!',
        'Roman1234',
        False,
        id='Incorrect password confirmation'
    ), pytest.param(
        '',
        'super.rk76@gmail.com',
        'super.rk76@gmail.com',
        '992145170',
        'Roman123445!',
        'Roman123445!',
        False,
        id='Empty user name field'
    ), pytest.param(
        '',
        '',
        '',
        '',
        '',
        '',
        False,
        id='Empty user name fields'
    )]
)
def test_user_registration(username,
                           email,
                           email_confirm,
                           phone_number,
                           password,
                           password_confirm,
                           expected_result,
                           user_registration_fixture):
    registration_page = user_registration_fixture
    res = registration_page.registration(
        username,
        email,
        email_confirm,
        phone_number,
        password,
        password_confirm,
    )
    assert res is expected_result
