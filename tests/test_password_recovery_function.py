import allure
from data import URLs
from pages.password_recovery_page import PasswordRecoveryPage
from pages.main_page import MainPage


class TestPasswordRecoveryPage:
    @allure.title('Проверить переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_open_password_recovery_page_click_recovery_password(self, driver):
        recovery_password_page = PasswordRecoveryPage(driver)
        main_page = MainPage(driver)
        main_page.open_account_profile()
        recovery_password_page.open_recovery_password_page()

        assert driver.current_url == URLs.PAGE_FORGOT_PASSWORD

    @allure.title('Проверить ввод почты и клик по кнопке «Восстановить»')
    def test_input_email_for_recovery(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.open_recovery_password_page()
        password_recovery_page.set_email_value()
        password_recovery_page.open_reset_password_page()
        element_text = password_recovery_page.wait_for_load_headers_reset_password()

        assert element_text == 'Восстановление пароля'

    @allure.title('Проверить, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_button_visibility_password_highlight_him(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.open_recovery_password_page()
        password_recovery_page.set_email_value()
        password_recovery_page.open_reset_password_page()
        password_recovery_page.set_new_password_value()
        password_recovery_page.click_to_button_visibility()
        element = password_recovery_page.find_element_field_password_active()

        assert element.is_displayed()
