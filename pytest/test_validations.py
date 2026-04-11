import pytest


@pytest.mark.smoke
def test_initial_check(pre_setup, post_setup):
    print("This is First Test : Pass an Username and Password")
    assert pre_setup == "HomePage"


def test_second_check(pre_setup, post_setup):
    print("This is Second Test : Dashboard Validation")


