import allure
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def open_page(self, page_url):
        self.driver.get(page_url)

    @allure.step('Подождать загрузки элемента')
    def wait_for_load_element(self, locator):
        return WDW(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Подождать открытия страницы')
    def wait_for_open_page(self, page_url):
        return WDW(self.driver, 10).until(EC.url_to_be(page_url))

    @allure.step('Найти элемент')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Подождать искомый элемент')
    def find_and_wait_element(self, locator):
        self.wait_for_load_element(locator)
        return self.find_element(locator)

    @allure.step('Найти элементы')
    def find_elements(self, locator):
        self.wait_for_load_element(locator)
        return self.driver.find_elements(*locator)

    @allure.step('Нажать на элемент с ожиданием')
    def click_element_with_wait(self, locator):
        element = self.find_and_wait_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Нажать на элемент')
    def click_element(self, locator):
        self.find_and_wait_element(locator).click()

    @allure.step('Установить значение')
    def set_value(self, locator, value):
        self.find_element(locator).send_keys(value)

    @allure.step('Перетащить элемент')
    def drag_and_drop_ingredient(self, locator1, locator2):
        ingredient = self.find_and_wait_element(locator1)
        target = self.find_and_wait_element(locator2)
        drag_and_drop(self.driver, ingredient, target)

    @allure.step('Подождать элемент для изменения')
    def wait_for_element_to_change_text(self, locator, text_to_be_changed):
        WDW(self.driver, 10).until_not(EC.text_to_be_present_in_element(locator, text_to_be_changed))
        return self.driver.find_element(*locator)

    @allure.step('Проверить доступность элемента')
    def check_element_is_invisible(self, locator):
        WDW(self.driver, 10).until_not(EC.presence_of_element_located(locator))
        return True

    def format_locator(self, locator, num):
        method, locator_final = locator
        locator_final = locator_final.format(num)
        return method, locator_final
