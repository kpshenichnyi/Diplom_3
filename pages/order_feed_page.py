import allure
from data import URLs
from locators.order_feed_page_locators import LocatorsOrderFeedPage
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step('Найти заголовок страницы "Лента заказов".')
    def view_orders_feed_form(self):
        return self.find_and_wait_element(LocatorsOrderFeedPage.HEADER_ORDER_LIST).text

    @allure.step('Открыть страницу "Лента заказов"')
    def open_order_feed_page(self):
        self.open_page(URLs.PAGE_ORDER_LIST)

    @allure.step('Перейти на Главную страницу')
    def go_to_main_page(self):
        self.click_element_with_wait(LocatorsOrderFeedPage.BUTTON_CONSTRUCTOR)

    @allure.step('Открыть первый заказ в списке заказов')
    def click_on_first_order_in_feed(self):
        self.click_element(LocatorsOrderFeedPage.FIRST_ORDER_LIST)

    @allure.step('Найти текст "Состав" в открывающемся окне с деталями заказа')
    def get_text_composition_from_window(self):
        return self.find_and_wait_element(LocatorsOrderFeedPage.MODEL_ORDER_WINDOW).text

    @allure.step('Проверить счётчик "Выполнено за всё время".')
    def view_all_time_done_orders(self):
        all_time_count = self.find_and_wait_element(LocatorsOrderFeedPage.ALL_TIME_COUNT).text
        return all_time_count

    @allure.step('Проверить счётчик "Выполнено за сегодня".')
    def view_today_done_orders(self):
        today_count = self.find_and_wait_element(LocatorsOrderFeedPage.TODAY_COUNT).text
        return today_count

    @allure.step('Просмотреть заказ в разделе "В работе".')
    def view_created_order_in_work(self, order_count):
        order_number_in_work_formatted = self.format_locator(LocatorsOrderFeedPage.ORDER_NUMBER_IN_WORK, order_count)
        return self.find_and_wait_element(order_number_in_work_formatted).text

    @allure.step('Найти все заказы в ленте заказов.')
    def collect_order_numbers_in_feed(self):
        order_elements = self.find_elements(LocatorsOrderFeedPage.BLOCK_ORDERS_LIST)
        order_numbers = []
        for order_element in order_elements:
            order_number_element = order_element.find_element(*LocatorsOrderFeedPage.ALL_ORDERS)
            order_number = order_number_element.text
            order_numbers.append(order_number)
        return order_numbers
