import allure
import requests
import random
import string
from data import COURIER_URL
import requests

class CourierMethods:

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

        response = requests.post(f'{COURIER_URL}', data=payload)

        if response.status_code == 201:
            return response.status_code, response.json(), {
                'login': login,
                'password': password,
                'firstName': first_name,
            }
        return response.status_code, {}, {}

    def create_new_courier_twice(self, courier_data):
        requests.post(f'{COURIER_URL}', data=courier_data)
        response = requests.post(f'{COURIER_URL}', data=courier_data)
        return response.status_code, response.json(), courier_data

    def create_new_courier_with_params(self, courier_data):
        response = requests.post(f'{COURIER_URL}', data=courier_data)
        return response.status_code, response.json(), courier_data


    def delete_courier(self, courier_id):
        delete_data = {
            "id": courier_id
        }
        response = requests.delete(f'{COURIER_URL}{courier_id}', data=delete_data)
        return response.status_code, response.json()


