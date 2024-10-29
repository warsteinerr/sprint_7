import pytest
import data
import allure


class TestLoginCourier:
    @allure.description('Проверяем, что курьер может залогиниться после создания и удаляем его')
    def test_courier_can_login(self, courier_method, login_method):
        status_code, response_context, credentials = courier_method.register_new_courier_and_return_login_password()
        login = credentials['login']
        password = credentials['password']
        login_status_code, login_response = login_method.login_courier(login, password)
        assert login_status_code == 200
        courier_id = login_response.get('id')
        courier_method.delete_courier(courier_id)

    @allure.description('Проверяем, что нельзя залогиниться без логина или праоля')
    @pytest.mark.parametrize('courier_data', [data.COURIER_NO_LOGIN, data.CPURIER_NO_PASSWORD])
    def test_required_field_for_login(self, login_method, courier_data):
        login = courier_data.get("login")
        password = courier_data.get("password")
        login_status_code, login_response = login_method.login_courier(login, password)
        assert login_response.get("message") == "Недостаточно данных для входа"

    @allure.description('Проверяем, что нельзя залогиниться с некорректным логином')
    def test_incorrect_login(self, courier_method, login_method):
        status_code, response_context, credentials = courier_method.register_new_courier_and_return_login_password()
        login = credentials['login']
        modified_login = login + "1"
        password = credentials['password']
        login_status_code, login_response = login_method.login_courier(modified_login, password)
        assert login_status_code == 404

    @allure.description('Проверяем, что нельзя залогиниться с некорректным паролем')
    def test_incorrect_password(self, courier_method, login_method):
        status_code, response_context, credentials =courier_method.register_new_courier_and_return_login_password()
        login = credentials['login']
        password = credentials['password']
        modified_password = password + '1'
        login_status_code, login_response = login_method.login_courier(login, modified_password)
        assert login_status_code == 404

    @allure.description('Проверяем, что нельзя залогиниться несуществующим юзером')
    def test_not_existing_user_login(self, login_method):
        login_status_code, login_response = login_method.login_with_random_credentials()
        assert login_response.get('message') == "Учетная запись не найдена"

    @allure.description('Проверяем, что в ответ на логин получаем id')
    def test_id_returned(self,courier_method, login_method):
        status_code, response_context, credentials = courier_method.register_new_courier_and_return_login_password()
        login = credentials['login']
        password = credentials['password']
        login_status_code, login_response = login_method.login_courier(login, password)
        assert 'id' in login_response


