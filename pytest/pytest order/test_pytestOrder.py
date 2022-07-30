import pytest

@pytest.mark.order(3)
def test_login001():
    print("login test passed")


@pytest.mark.order(2)
def test_login002():
    print("login test failed")

@pytest.mark.order(1)
def test_login003():
    print("login test passed again")