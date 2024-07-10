class URLs:
    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site'
    PAGE_LOGIN = f'{MAIN_PAGE}/login'
    PAGE_FORGOT_PASSWORD = f'{MAIN_PAGE}/forgot-password'
    PAGE_RESET_PASSWORD = f'{MAIN_PAGE}/reset-password'
    PAGE_ACCOUNT_PROFILE = f'{MAIN_PAGE}/account/profile'
    PAGE_ORDER_HISTORY = f'{MAIN_PAGE}/account/order-history'
    PAGE_ORDER_LIST = f'{MAIN_PAGE}/feed'

class ApiEndpoints:
    API_CREATE_USER = f'{URLs.MAIN_PAGE}/api/auth/register'
    API_LOGIN_USER = f'{URLs.MAIN_PAGE}/api/auth/login'
    API_DELETE_USER = f'{URLs.MAIN_PAGE}/api/auth/user'
    API_CREATE_ORDER = f'{URLs.MAIN_PAGE}/api/orders'

class DefaultUserData:
    DEFAULT_EMAIL = 'itpetry@ya.ru'
    DEFAULT_PASSWORD = '1@qwerty&9'
