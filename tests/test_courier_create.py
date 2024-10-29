import pytest
import data
import allure

class TestCreateCourier:
    @allure.description('Проверяем, что курьер создается и удаляем его')
    def test_courier_can_be_created(self, courier_method, login_method):
        status_code, response_context, credentials = courier_method.register_new_courier_and_return_login_password()
        assert status_code == 201
        login = credentials['login']
        password = credentials['password']
        login_status_code, login_response = login_method.login_courier(login, password)
        courier_id = login_response.get('id')
        courier_method.delete_courier(courier_id)

    @allure.description('Проверяем, что курьер создается и в ответе приходит корректный текст')
    def test_courier_creation_correct_answer(self, courier_method, login_method):
        status_code, response_context, credentials = courier_method.register_new_courier_and_return_login_password()
        assert response_context.get("ok") is True
        login = credentials['login']
        password = credentials['password']
        login_status_code, login_response = login_method.login_courier(login, password)
        courier_id = login_response.get('id')
        courier_method.delete_courier(courier_id)

    @allure.description('Проверяем, что нельзя создать двух одинаковых курьеров и удаляем первого созданного')
    def test_two_equal_couriers_error(self, courier_method, login_method):
        status_code, response_context, data_courier= courier_method.create_new_courier_twice(data.COURIER1)
        assert status_code == 409
        login = data_courier['login']
        password = data_courier['password']
        login_status_code, login_response = login_method.login_courier(login, password)
        courier_id = login_response.get('id')
        courier_method.delete_courier(courier_id)

    @allure.description('Проверяем, что курьера нельзя создать если не передается логин или пароль')
    @pytest.mark.parametrize('courier_data', [data.COURIER_NO_LOGIN, data.CPURIER_NO_PASSWORD])
    def test_create_courier_without_required_field(self, courier_method, login_method,  courier_data):
        status_code, response_context, data = courier_method.create_new_courier_twice(courier_data)
        assert response_context.get('message') == "Недостаточно данных для создания учетной записи"













