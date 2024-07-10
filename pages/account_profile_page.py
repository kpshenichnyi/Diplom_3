import allure
from locators.account_profile_locators import LocatorsAccountProfilePage
from pages.base_page import BasePage


class AccountProfilePage(BasePage):
    @allure.step('Показать заголовок "Профиль" на странице личного кабинета')
    def view_header_profile_in_account_profile_page(self):
        return self.find_and_wait_element(LocatorsAccountProfilePage.HEADER_PROFILE)

    @allure.step('Перейти к странице с историей заказов, нажав кнопку "История заказов"')
    def open_order_history_page(self):
        self.click_element_with_wait(LocatorsAccountProfilePage.BUTTON_ORDER_HISTORY)

    @allure.step('Выйти из профиля учетной записи, нажав на "Выход"')
    def logout_of_account_profile(self):
        self.click_element_with_wait(LocatorsAccountProfilePage.BUTTON_LOGOUT)

    @allure.step('Получить номер последнего заказа в истории заказов')
    def get_last_number_order_from_order_history_page(self):
        return self.find_and_wait_element(LocatorsAccountProfilePage.NUMBER_ORDER_HISTORY).text
