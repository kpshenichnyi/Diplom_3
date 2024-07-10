import allure
from locators.login_page_locators import LocatorsLoginPage
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Ввести email пользователя')
    def set_user_email(self, email):
        self.set_value(LocatorsLoginPage.EMAIL_FIELD, email)

    @allure.step('Ввести пароль пользователя')
    def set_user_password(self, password):
        self.set_value(LocatorsLoginPage.PASSWORD_FIELD, password)

    @allure.step('Авторизоваться под пользователя')
    def confirm_user_authorization(self):
        self.click_element_with_wait(LocatorsLoginPage.LOGIN_BUTTON)

    @allure.step('Дождаться отображение окна авторизации')
    def view_authorization_form(self):
        return self.find_and_wait_element(LocatorsLoginPage.LOGIN_BUTTON).text
