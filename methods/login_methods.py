import requests
import random
import string
import allure
from data import COURIER_URL, BASE_URL


class LoginMethods:
    @allure.step('Авторизация курьером')
    def login_courier(self, login, password):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(f'{BASE_URL}{COURIER_URL}login', data=payload)
        return response.status_code, response.json()

    @allure.step('Генерация рандомных данных')
    def generate_random_string(self, length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @allure.step('Авторизация рандомными данными')
    def login_with_random_credentials(self):
        random_login = self.generate_random_string(10)
        random_password = self.generate_random_string(10)

        payload = {
            "login": random_login,
            "password": random_password
        }
        response = requests.post(f'{BASE_URL}{COURIER_URL}login', data=payload)
        return response.status_code, response.json()
