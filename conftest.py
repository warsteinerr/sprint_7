import pytest
from methods.courier_methods import CourierMethods
from methods.login_methods import LoginMethods
from methods.order_methods import OrderMethods


@pytest.fixture
def courier_method():
    return CourierMethods()

@pytest.fixture
def login_method():
    return LoginMethods()

@pytest.fixture
def order_method():
    return OrderMethods()

