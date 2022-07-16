import pytest


@pytest.fixture(scope='module')
def setup():
    print("Creating DB Connection")

    yield
    print("Closing DB Connection")

@pytest.fixture(scope='function')
def before():
    print("Launching Browser")

    yield

    print("Closing Browser")

# test function can get both fixtures as a parameter
# def test_logintest(setup, before):
#     print("Executing Login test case")
#
# def test_regtest(setup, before):
#     print("Executing Reg test case")

# or test function can get one fixture as a parameter
# def test_logintest(before):
#     print("Executing Login test case")
#
# def test_regtest(before):
#     print("Executing Reg test case")

# test function can get fixtures as a mark decorator

@pytest.mark.usefixtures("setup", "before")
def test_logintest():
    print("Executing Login test case")

@pytest.mark.usefixtures("setup", "before")
def test_regtest():
    print("Executing Reg test case")
