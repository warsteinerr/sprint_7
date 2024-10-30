import requests
from data import ORDER_URL, BASE_URL
import allure


class OrderMethods:
    @allure.step('Создание заказа')
    def create_order(self, order_data):
        response = requests.post(f'{BASE_URL}{ORDER_URL}', json=order_data)
        return response.status_code, response.json()

    @allure.step('Получение списка заказов')
    def get_list_of_orders(self):
        response = requests.get(f'{BASE_URL}{ORDER_URL}')
        return response.status_code, response.json()

