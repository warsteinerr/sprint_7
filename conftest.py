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


@pytest.fixture
def courier(courier_method, login_method):
    status_code, response_context, credentials = courier_method.register_new_courier_and_return_login_password()
    login = credentials['login']
    password = credentials['password']
    login_status_code, login_response = login_method.login_courier(login, password)
    courier_id = login_response.get('id')
    yield {'login': login, 'password': password, 'courier_id': courier_id}
    if courier_id:
        courier_method.delete_courier(courier_id)

