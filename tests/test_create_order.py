import allure
import pytest
import data
import allure


class TestCreateOrder:
    @allure.title('Создание заказа с BLACK')
    @allure.description('Проверяем, что можно создать заказ с черным цветом')
    def test_create_order_black(self, order_method):
        order_status, order_response = order_method.create_order(data.ORDER_BLACK)
        assert order_status == 201 and "track" in order_response

    @allure.title('Создание заказа с GREY')
    @allure.description('Проверяем, что можно создать заказ с серым цветом')
    def test_create_order_grey(self, order_method):
        order_status, order_response = order_method.create_order(data.ORDER_GREY)
        assert order_status == 201 and "track" in order_response

    @allure.title('Создание заказа с BLACK и GREY')
    @allure.description('Проверяем, что можно создать заказ с двумя цветами')
    def test_create_order_both_clours(self, order_method):
        order_status, order_response = order_method.create_order(data.ORDER_BOTH_COLOURS)
        assert order_status == 201 and "track" in order_response

    @allure.title('Создание заказа без цвета')
    @allure.description('Проверяем, что можно создать заказ без цвета и в ответе есть "track"')
    def test_create_order_no_clour(self, order_method):
        order_status, order_response = order_method.create_order(data.ORDER_NO_COLOUR)
        assert order_status == 201 and "track" in order_response

    @allure.title('Получение списка заказов')
    @allure.description('Проверяем, что в ответе приходит orders и он является списком')
    def test_get_list_of_orders(self, order_method):
        order_status, order_response = order_method.get_list_of_orders()
        assert isinstance(order_response["orders"], list)
