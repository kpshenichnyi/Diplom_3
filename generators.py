import allure
from faker import Faker


@allure.step('Сгенерировать фейкового пользователя')
def generate_fake_user():
    fake_user = Faker(locale="ru_RU")
    user_email = fake_user.email()
    user_password = fake_user.password()
    user_name = fake_user.name()
    return user_email, user_password, user_name

