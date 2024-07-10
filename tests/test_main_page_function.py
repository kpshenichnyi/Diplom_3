import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestMainPage:
    @allure.title('Проверить, переход по клику на «Конструктор»')
    def test_go_to_click_constructor_form(self, driver):
        main_page = MainPage(driver)

        assert main_page.view_constructor_form() == 'Соберите бургер'

    @allure.title('Проверить, переход по клику на «Лента заказов»')
    def test_go_to_click_orders_list(self, driver):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)
        main_page.open_orders_list()

        assert order_page.view_orders_feed_form() == 'Лента заказов'

    @allure.title('Проверить, что если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient_window_is_open(self, driver):
        main_page = MainPage(driver)

        assert main_page.view_window_ingredient() == 'Детали ингредиента'

    @allure.title('Проверить, что всплывающее окно закрывается кликом по крестику')
    def test_click_cross_in_window_ingredient_closes_window(self, driver):
        main_page = MainPage(driver)
        main_page.view_window_ingredient()
        main_page.click_on_button_сross_in_window_ingredient()

        assert main_page.check_window_is_closed()

    @allure.title('Проверить, что при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_add_ingredient_in_order_counters_ingredient_is_increasing(self, driver):
        main_page = MainPage(driver)
        count_ingredient_start = main_page.get_ingredient_count()
        main_page.drag_and_drop_bun_to_the_constructor_burger()
        count_ingredient_finish = main_page.get_ingredient_count()

        assert count_ingredient_finish > count_ingredient_start

    @allure.title('Проверить, что авторизованный пользователь может оформить заказ')
    def test_auth_user_can_place_an_order(self, ui_auth_user):
        main_page = MainPage(ui_auth_user)
        main_page.make_an_order()
        assert main_page.find_text_in_window_order() == 'Ваш заказ начали готовить'
