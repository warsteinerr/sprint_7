BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
COURIER_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/'
ORDER_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/orders/'


COURIER1 = {
    "login": "Alex",
    "password": "123456",
    "firstName": "Meskini"
}

COURIER_NO_LOGIN = {
    "login": "",
    "password": "123456"
}

CPURIER_NO_PASSWORD = {
    "login": "Alex",
    "password": ""
}


ORDER_BLACK = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}

ORDER_GREY = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "GREY"
    ]
}

ORDER_BOTH_COLOURS = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK", "GREY"
    ]
}

ORDER_NO_COLOUR = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [

    ]
}