import pytest

@pytest.fixture(scope="session")
def pre_setup():
    print("Session Scope : Pre-setup - I set up Browser Instance")
    return "HomePage"

@pytest.fixture(scope="session")
def post_setup():
    print("Session Scope : Post-setup - Pass App URL")
    yield
    print("Teardown - I clean up / Close the Browser Instance")