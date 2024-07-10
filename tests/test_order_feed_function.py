import allure
from pages.account_profile_page import AccountProfilePage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeedPage:
    @allure.title('Проверить, что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_open_modal_window_of_order_by_click_on_first_order_in_list(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_feed_page()
        order_feed_page.click_on_first_order_in_feed()

        assert order_feed_page.get_text_composition_from_window() == 'Cостав'

    @allure.title('Проверить, что заказы пользователя из раздела «История заказов» '
                  'отображаются на странице «Лента заказов»')
    def test_users_order_displayed_in_order_feed(self, ui_auth_user):
        order_feed_page = OrderFeedPage(ui_auth_user)
        main_page = MainPage(ui_auth_user)
        account_profile_page = AccountProfilePage(ui_auth_user)
        main_page.make_an_order()
        main_page.open_account_profile()
        account_profile_page.open_order_history_page()
        number_order_history = account_profile_page.get_last_number_order_from_order_history_page()
        order_feed_page.open_order_feed_page()
        order_texts = order_feed_page.collect_order_numbers_in_feed()

        assert number_order_history in order_texts

    @allure.title('Проверить, что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_counter_all_orders_increases_after_new_order(self, ui_auth_user):
        order_feed_page = OrderFeedPage(ui_auth_user)
        main_page = MainPage(ui_auth_user)
        main_page.open_orders_list()
        all_time_count_before = order_feed_page.view_all_time_done_orders()
        order_feed_page.go_to_main_page()
        main_page.make_an_order()
        order_feed_page.open_order_feed_page()
        all_time_count_after = order_feed_page.view_all_time_done_orders()

        assert all_time_count_after > all_time_count_before

    @allure.title('Проверить, что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_counter_today_orders_increases_after_new_order(self, ui_auth_user):
        order_feed_page = OrderFeedPage(ui_auth_user)
        main_page = MainPage(ui_auth_user)
        main_page.open_orders_list()
        today_time_count_before = order_feed_page.view_today_done_orders()
        order_feed_page.go_to_main_page()
        main_page.make_an_order()
        order_feed_page.open_order_feed_page()
        today_time_count_after = order_feed_page.view_today_done_orders()

        assert today_time_count_after > today_time_count_before

    @allure.title('Проверить, что после оформления заказа его номер появляется в разделе В работе.')
    def test_number_of_new_order_appears_in_work(self, ui_auth_user):
        order_feed_page = OrderFeedPage(ui_auth_user)
        main_page = MainPage(ui_auth_user)
        number = main_page.make_an_order_and_get_number()
        main_page.open_orders_list()

        assert order_feed_page.view_created_order_in_work(number)
