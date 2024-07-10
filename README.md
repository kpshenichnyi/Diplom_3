## Дипломный проект. Задание 3: UI-тестирование

### Автотесты для проверки UI сайта Stellar Burgers https://stellarburgers.nomoreparties.site/

### Структура проекта


- `allure_results` - пакет с отчетами о проведенном тестировании
- `locators` - пакет с локаторами
- `pages` - пакет с методами тестируемых страниц
- `tests` - пакет с тестами тестируемых страниц
- `conftest.py` - файл с фикстурами
- `data.py` - файл с данные для тестов
- `api.py` - файл с api-методами для доступа к сайту
- `generators.py` - файл с вспомогательными функциями
- `README.md` - описание проекта
- `requirements.txt` - файл с внешними зависимостями


### Запуск автотестов

**Установка зависимостей**

> `pip install -r requirements.txt`

**Запуск автотестов и создание отчета о тестировании в Allure**

> `pytest --alluredir=allure_results`

**Генерация отчета в html страницу**

>`allure serve allure_results`
