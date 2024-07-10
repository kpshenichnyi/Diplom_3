import allure
import pytest
import requests

from data import URLs
from generators import generate_fake_user
from pages.login_page import LoginPage
from pages.main_page import MainPage
from api import APIPages

from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


def _get_driver(name):
    if name == "chrome":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        return webdriver.Chrome(service=service)
    elif name == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        return webdriver.Firefox(service=service)
    else:
        raise TypeError("Driver is not found")

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    # browser = None
    # if request.param == 'chrome':
    #     browser = webdriver.Chrome()
    # elif request.param == 'firefox':
    #     browser = webdriver.Firefox()
    browser = _get_driver(request.param)
    browser.get(URLs.MAIN_PAGE)
    yield browser
    browser.quit()

@allure.step('Сгенерировать данные пользователя для регистрации')
@pytest.fixture
def generate_user_data():
    data_user = generate_fake_user()
    payload = {'email': data_user[0], 'password': data_user[1], 'name': data_user[2]}
    return payload, data_user


@allure.step('Зарегистрировать пользователя через API, авторизоваться, и по завершении удалить')
@pytest.fixture
def api_register_user_and_delete(generate_user_data):
    payload_register = generate_user_data[0]
    register_user_data = generate_user_data[1]
    response_register_user = APIPages().create_new_user(payload_register)
    auth_user_data = []
    if response_register_user.status_code == 200:
        auth_user_data.append(register_user_data[0])
        auth_user_data.append(register_user_data[1])
    payload_auth_user = {'email': register_user_data[0], 'password': register_user_data[1]}
    response_auth_user = APIPages().auth_login_user(payload_auth_user)
    yield auth_user_data
    token_user = response_auth_user.json()['accessToken']
    APIPages().delete_user(token_user)

@allure.step('Авторизоваться под пользователем через UI')
@pytest.fixture
def ui_auth_user(driver, api_register_user_and_delete):
    email = api_register_user_and_delete[0]
    password = api_register_user_and_delete[1]
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    main_page.open_account_profile()
    login_page.set_user_email(email)
    login_page.set_user_password(password)
    login_page.confirm_user_authorization()
    main_page.wait_for_load_main_page()
    return driver

