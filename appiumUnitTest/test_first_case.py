import pytest

def setup_module(module):
    """
    module level setup run very first beginning of the case
    """
    print("Creating DB Connection")

def teardown_module(module):
    """
    module level teardown run very first beginning of the case
    """
    print("Closing DB Connection")


def setup_function(function):
    """
    this is called test Fixtures..
    :param function: mandatory feature for function base setup function setup
    this function execute peace of code, runs initial commands before each function below
    """
    print("Launching the browser")

def teardown_function(function):

    print("Quitting the browser")

def test_logintest():
    print("Executing Login test case")

def test_regtest():
    print("Executing Reg test case")
