import pytest

def get_data():
    return [

        ("python@dakk.com", "12345"),
        ("java@dakk.com", "12345"),
        ("go@dakk.com", "12345"),

    ]

@pytest.mark.parametrize("username,password",get_data())
def test_dologin(username,password):
    print(username, "----", password)