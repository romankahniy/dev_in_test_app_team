import pytest


@pytest.mark.parametrize(
    'username, password, expected_result',
    [pytest.param(
        'qa.ajax.app.automation@gmail.com',
        'qa_automation_password',
        True,
        id='Correct username and password'
    ), pytest.param(
        'login',
        'qa_automation_password',
        False,
        id='Incorrect login'
    ), pytest.param(
        'qa.ajax.app.automation@gmail.com',
        'password',
        False,
        id='Incorrect password'
    ), pytest.param(
        'login',
        'password',
        False,
        id='Incorrect login and password'
    ), pytest.param(
            "",
            "",
            False,
            id="Empty fields",
    )]
)
def test_user_login(username, password, expected_result, user_login_fixture):
    login_page = user_login_fixture
    res = login_page.login(
        username,
        password
    )
    assert res is expected_result
