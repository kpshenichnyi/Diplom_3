import allure
from data import URLs
from pages.account_profile_page import AccountProfilePage
from pages.main_page import MainPage


class TestAccountProfilePage:
    @allure.title('Проверить переход по клику на «Личный кабинет» для авторизованного пользователя')
    def test_go_to_forgot_password_page_click_on_link_recover_page(self, ui_auth_user):
        account_profile_page = AccountProfilePage(ui_auth_user)
        main_page = MainPage(ui_auth_user)
        main_page.open_account_profile()

        assert account_profile_page.view_header_profile_in_account_profile_page().text == 'Профиль'

    @allure.title('Проверить переход в раздел «История заказов» из профиля аккаунта')
    def test_go_to_account_profile_when_user_login(self, ui_auth_user):
        account_profile_page = AccountProfilePage(ui_auth_user)
        main_page = MainPage(ui_auth_user)
        main_page.open_account_profile()
        account_profile_page.open_order_history_page()
        account_profile_page.wait_for_open_page(URLs.PAGE_ORDER_HISTORY)

        assert ui_auth_user.current_url == URLs.PAGE_ORDER_HISTORY

    @allure.title('Проверить выход из профиля аккаунта при нажатии на кнопку "Выход"')
    def test_logout_of_account_profile_by_click_button_logout(self, ui_auth_user):
        account_profile_page = AccountProfilePage(ui_auth_user)
        main_page = MainPage(ui_auth_user)
        main_page.open_account_profile()
        account_profile_page.logout_of_account_profile()
        account_profile_page.wait_for_open_page(URLs.PAGE_LOGIN)

        assert ui_auth_user.current_url == URLs.PAGE_LOGIN
