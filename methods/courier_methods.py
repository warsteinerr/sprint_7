import allure
import requests
import random
import string
from data import COURIER_URL, BASE_URL
import requests

class CourierMethods:

    @allure.step('Создаем нового юзера и возращаем данные о нем')
    def register_new_courier_and_return_login_password(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login_pass = []

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(f'{BASE_URL}{COURIER_URL}', data=payload)

        if response.status_code == 201:
            return response.status_code, response.json(), {
                'login': login,
                'password': password,
                'firstName': first_name,
            }
        return response.status_code, {}, {}

    @allure.step('Дважды создаем одного курьера')
    def create_new_courier_twice(self, courier_data):
        requests.post(f'{BASE_URL}{COURIER_URL}', data=courier_data)
        response = requests.post(f'{BASE_URL}{COURIER_URL}', data=courier_data)
        return response.status_code, response.json(), courier_data

    @allure.step('Создаем курьеров с параметризацией')
    def create_new_courier_with_params(self, courier_data):
        response = requests.post(f'{BASE_URL}{COURIER_URL}', data=courier_data)
        return response.status_code, response.json(), courier_data

    @allure.step('Удаление курьера')
    def delete_courier(self, courier_id):
        delete_data = {
            "id": courier_id
        }
        response = requests.delete(f'{BASE_URL}{COURIER_URL}{courier_id}', data=delete_data)
        return response.status_code, response.json()


