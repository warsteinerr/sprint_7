import requests
from data import ORDER_URL


class OrderMethods:
    def create_order(self, order_data):
        response = requests.post(f'{ORDER_URL}', json=order_data)
        return response.status_code, response.json()

    def get_list_of_orders(self):
        response = requests.get(ORDER_URL)
        return response.status_code, response.json()
