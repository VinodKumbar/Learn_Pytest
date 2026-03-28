import pytest
#Bring functionality of pytest to I can use it in this file
# Import -> load a library or a module in Python
# pytest -> a testing framework

@pytest.fixture
def pre_setup():
    print("Launching Browser")
    print("Opening URL")
    return "Pass"


def test_initial_check(pre_setup):
    print("This is First test")
    print("Passing Login Credentials")
    print("Login Successful")
    assert pre_setup == "Pass"