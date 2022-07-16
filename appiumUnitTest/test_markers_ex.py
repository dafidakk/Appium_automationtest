import pytest

# pytest test_markers_ex.py -s -v -k login this command only run login test
# pytest test_markers_ex.py -s -v -k "not login" command only run exept login test
# pytest test_markers_ex.py -s -v -m functional command only run user define markes as functional
# how to mark test functions : https://docs.pytest.org/en/stable/how-to/mark.html
@pytest.mark.functional
def test_login():
    print("Executing login test")

@pytest.mark.regression
def test_user_reg():
    print("Executing User reg test")

@pytest.mark.functional
def test_compose_email():
    print("Executing compose email test")

@pytest.mark.skip
def test_skip():
    print("skipped")
