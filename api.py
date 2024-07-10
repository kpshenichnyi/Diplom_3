import allure
import requests
from data import URLs, ApiEndpoints


class APIPages:
    def __init__(self):
        self.main_url = URLs.MAIN_PAGE
        self.url_user_create = ApiEndpoints.API_CREATE_USER
        self.url_user_login = ApiEndpoints.API_LOGIN_USER
        self.url_user_delete = ApiEndpoints.API_DELETE_USER
        self.url_order = ApiEndpoints.API_CREATE_ORDER

    @allure.step('Создать пользователя')
    def create_new_user(self, payload):
        response = requests.post(self.url_user_create, data=payload)
        return response

    @allure.step('Авторизовать пользователя')
    def auth_login_user(self, payload):
        response = requests.post(self.url_user_login, data=payload)
        return response

    @allure.step('Удалить пользователя')
    def delete_user(self, token_user):
        headers = {"Authorization": token_user}
        response = requests.delete(self.url_user_delete, headers=headers)
        return response

