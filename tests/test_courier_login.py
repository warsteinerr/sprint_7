import pytest
import data
import allure


class TestLoginCourier:
    @allure.title('Проверка авторизации курьера')
    @allure.description('Проверяем, что курьер может залогиниться после создания и удаляем его')
    def test_courier_can_login(self, courier, login_method):
        login_status_code, login_response = login_method.login_courier(courier['login'], courier['password'])
        assert login_status_code == 200 and "id" in login_response

    @allure.title('Логин без логина или пароля')
    @allure.description('Проверяем, что нельзя залогиниться без логина или праоля')
    @pytest.mark.parametrize('courier_data', [data.COURIER_NO_LOGIN, data.CPURIER_NO_PASSWORD])
    def test_required_field_for_login(self, login_method, courier_data):
        login = courier_data.get("login")
        password = courier_data.get("password")
        login_status_code, login_response = login_method.login_courier(login, password)
        assert login_response.get("message") == data.NOT_ENOUGH_ENTER_DATA

    @allure.title('Авторизация с некорректными данными')
    @allure.description('Проверяем, что нельзя залогиниться с некорректным логином')
    def test_incorrect_login(self, courier, login_method):
        modified_login = courier['login'] + "1"  # Измененный логин
        login_status_code, login_response = login_method.login_courier(modified_login, courier['password'])
        assert login_status_code == 404 and login_response.get('message') == data.USER_NOT_FOUND

    @allure.title('Авторизация с некорректным паролем')
    @allure.description('Проверяем, что нельзя залогиниться с некорректным паролем')
    def test_incorrect_password(self, courier, login_method):
        modified_password = courier['password'] + "1"  # Измененный пароль
        login_status_code, login_response = login_method.login_courier(courier['login'], modified_password)
        assert login_status_code == 404 and login_response.get('message') == data.USER_NOT_FOUND

    @allure.title('Авторизация несущуствующим юзером')
    @allure.description('Проверяем, что нельзя залогиниться несуществующим юзером')
    def test_not_existing_user_login(self, login_method):
        login_status_code, login_response = login_method.login_with_random_credentials()
        assert login_response.get('message') == data.USER_NOT_FOUND

    @allure.title('Получение id при логине')
    @allure.description('Проверяем, что в ответ на логин получаем id')
    def test_id_returned(self, courier, login_method):
        login_status_code, login_response = login_method.login_courier(courier['login'], courier['password'])
        assert 'id' in login_response


