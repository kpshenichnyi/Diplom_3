import allure
from data import URLs
from data import DefaultUserData
from locators.password_recovery_locators import LocatorsPasswordRecoveryPage
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):
    @allure.step('Перейти на страницу с восставновлением пароля по ссылке "Восстановить пароль"')
    def go_to_password_recovery_page(self):
        self.click_element_with_wait(LocatorsPasswordRecoveryPage.LINK_FORGOT_PASSWORD)

    @allure.step('Дождаться загрузки кнопки "Восстановить пароль"')
    def wait_for_load_link_recovery_password(self):
        self.wait_for_load_element(LocatorsPasswordRecoveryPage.LINK_FORGOT_PASSWORD)

    @allure.step('Открыть страницу c восставновлением пароля')
    def open_recovery_password_page(self):
        self.open_page(URLs.PAGE_FORGOT_PASSWORD)

    @allure.step('Ввести в поле "Email" электронную почту')
    def set_email_value(self):
        self.set_value(LocatorsPasswordRecoveryPage.FIELD_EMAIL, DefaultUserData.DEFAULT_EMAIL)

    @allure.step('Нажать на кнопку "Восстановить"')
    def open_reset_password_page(self):
        self.click_element_with_wait(LocatorsPasswordRecoveryPage.BUTTON_RECOVER)

    @allure.step('Дождаться загрузки заголовка "Восстановление пароля"')
    def wait_for_load_headers_reset_password(self):
        return self.find_and_wait_element(LocatorsPasswordRecoveryPage.HEADING_TEXT).text

    @allure.step('Ввести новый пароль')
    def set_new_password_value(self):
        self.find_and_wait_element(LocatorsPasswordRecoveryPage.FIELD_PASSWORD)
        self.set_value(LocatorsPasswordRecoveryPage.FIELD_PASSWORD, DefaultUserData.DEFAULT_PASSWORD)

    @allure.step('Нажать на кнопку "показать/скрыть пароль"')
    def click_to_button_visibility(self):
        self.click_element_with_wait(LocatorsPasswordRecoveryPage.BUTTON_VISIBILITY_PASSWORD)

    @allure.step('Найти подсветку для поля "Пароль"')
    def find_element_field_password_active(self):
        return self.find_and_wait_element(LocatorsPasswordRecoveryPage.FIELD_PASSWORD_ACTIVE)
