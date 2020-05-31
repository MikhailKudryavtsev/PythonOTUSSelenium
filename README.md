# PythonOTUSSelenium
Тестирование OpenCart.

Тестовые функции принимает 2 параметра:

- `url` ;
- `driver` - может принимать значения `chrome`, `firefox`, `ie` .

Пример запуска `pytest tests/first_test.py --url=http://localhost/ --driver=chrome`

`Opencart.log` содержит логи проекта.

Метод `browser_logs` логирует консоль браузера.

Метод `proxy_logs` логирует прокси сервер по ключу `entries`.