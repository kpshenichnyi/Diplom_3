import allure
from locators.main_page_locators import LocatorsMainPage
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Открыть страницу Личного кабинета')
    def open_account_profile(self):
        self.click_element(LocatorsMainPage.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Подождать загрузки главной страницы')
    def wait_for_load_main_page(self):
        self.find_and_wait_element(LocatorsMainPage.MAIN_PAGE)

    @allure.step('Открыть страницу ленты заказов')
    def open_orders_list(self):
        self.click_element(LocatorsMainPage.BUTTON_ORDER_LIST)

    @allure.step('Нажать на "Лента заказов", далее нажать на "Конструктор, и найти заголовок "Соберите заказ"')
    def view_constructor_form(self):
        self.click_element_with_wait(LocatorsMainPage.BUTTON_ORDER_LIST)
        self.click_element_with_wait(LocatorsMainPage.BUTTON_CONSTRUCTOR)
        return self.find_and_wait_element(LocatorsMainPage.HEADER_MAIN_PAGE).text

    @allure.step('Нажать на ингредиент и найти заголовок в открывающемся окне')
    def view_window_ingredient(self):
        self.click_element_with_wait(LocatorsMainPage.BUN_FIRST_IN_LIST)
        return self.find_and_wait_element(LocatorsMainPage.HEADER_WINDOW_INGREDIENT).text

    @allure.step('Нажать на "крестик" в открытом окне с деталями ингредиента')
    def click_on_button_сross_in_window_ingredient(self):
        self.click_element_with_wait(LocatorsMainPage.BUTTON_CROSS_IN_WINDOW_INGREDIENT)

    @allure.step('Проверить закрытие окна')
    def check_window_is_closed(self):
        return self.check_element_is_invisible(LocatorsMainPage.INGREDIENT_WINDOW)

    @allure.step('Переложить булку в конструктор')
    def drag_and_drop_bun_to_the_constructor_burger(self):
        self.drag_and_drop_ingredient(LocatorsMainPage.BUN_FIRST_IN_LIST, LocatorsMainPage.BUN_IN_CONSTRUCTOR)

    @allure.step('Нажать на кнопку "Оформить заказ"')
    def click_on_button_confirm_order(self):
        self.click_element(LocatorsMainPage.BUTTON_CONFIRM_ORDER)

    @allure.step('Нажать на "крестик" в окне сформированного заказа')
    def click_on_button_сross_in_window_order(self):
        self.click_element_with_wait(LocatorsMainPage.BUTTON_CROSS_IN_WINDOW)

    @allure.step('Получить номер заказа')
    def get_number_order(self):
        return self.find_and_wait_element(LocatorsMainPage.ORDER_NUMBER).text

    @allure.step('Сделать заказ')
    def make_an_order(self):
        self.drag_and_drop_bun_to_the_constructor_burger()
        self.click_on_button_confirm_order()
        self.click_on_button_сross_in_window_order()

    @allure.step('Найти текст в открытом окне "Ваш заказ начали готовить"')
    def find_text_in_window_order(self):
        return self.find_and_wait_element(LocatorsMainPage.TEXT_IN_ORDER_WINDOW).text

    @allure.step('Получить номер счетчика ингредиента')
    def get_ingredient_count(self):
        return self.find_and_wait_element(LocatorsMainPage.COUNTER_INGREDIENT).text

    @allure.step('Оформить заказ и получить его номер')
    def make_an_order_and_get_number(self):
        self.drag_and_drop_bun_to_the_constructor_burger()
        self.click_on_button_confirm_order()
        self.wait_for_element_to_change_text(LocatorsMainPage.ORDER_NUMBER, '9999')
        number = self.get_number_order()
        self.click_on_button_сross_in_window_order()
        return number

