import pytest


def test_title():
    """
    SOFT ASSERT
    regular assertion only run first assert, soft runs all and report
    to install soft assert:
    pip install pytest-soft-assertions
    to run test
    pytest test_validate_with_assert.py -s -v --soft-asserts
    """
    expected_title = "Google.com"
    actual_title = "Gmail.com"
    title = "This is Gmail website"

    print("Beginning")
    assert expected_title == actual_title, "Titles are not matching"
    assert "Gmails" in title, "Gmail does not exist in title"
    assert False, "Forcefully failing the test"
    print("Ending")

