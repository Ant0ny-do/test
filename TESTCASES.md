| Заголовок  | Предусловие | Шаги проверки | Ожидаемо | Статус прохождения
| :-------------: | :-------------: | :-------------: | :-------------: |  :-------------: |
| Успешное создание объявления от пользователя с корректными данными | Headers request: Content-Type: application/json  | Отправить POST запрос {{baseUrl}}/api/1/item JSON тело с полями sellerID в диапазоне 111111-999999, name Valenki, price 30000, statistics{likes 0, viewCount 0, contacts 0} | 200 Ок | Failed
| Корректная валидация типов: SellerID строкой | Headers request: Content-Type: application/json  | Отправить JSON тело с полем sellerID "111111" | 400 Bad | Passed
| Корректная проверка на отсутствие обязательных полей| Headers request: Content-Type: application/json  |  Удалить ключ и значение SellerID из тела JSON, удалить name, удалить price | 400 Bad | Passed
| Проверка на корректность значения price | Headers request: Content-Type: application/json | Ввести значение price -1 | 400 Bad | Failed
| Проверка на корректность значения price | Headers request: Content-Type: application/json | Ввести значение price 0 | 200 Ok | Failed
| Успешное создание объявления от пользователя с корректными данными | Headers request: Content-Type: application/json  | Отправить POST запрос {{baseUrl}}/api/1/item JSON тело с полями sellerID в диапазоне 111111-999999, name valenok, price 999999999, statistics{likes 1, viewCount 1, contacts 1} | 200 Ок | Passed
| Успешное получение объявления по id | Объявление создано, id сохранен  | Отправить GET запрос {{baseUrl}}/api/1/item/e481ff14-ecc1-480e-9299-4743e5d49cea | 200 Ок, ответ - тело JSON c корректными данными | Passed
| Успешное получение объявления по id | Объявление создано, id сохранен  | Отправить GET запрос {{baseUrl}}/api/1/item/e481ff14-ecc1-480e-9299-4743e5d49cea | 200 Ок, ответ - тело JSON c корректными данными | Passed
| Запрос несуществующего id | id не создан и не сохранен | Отправить GET запрос {{baseUrl}}/api/1/item/e481ff14-ecc1-480e-9299-4743e5d49cee | 404 Not Found | Passed
| Запрос не валидного id | Некорректная форма записи id  | Отправить GET запрос {{baseUrl}}/api/1/item/ahugufg | 400 Bad Request | Passed
| Корректная выдача списка всех объявлений продавца | Созданы 2 объявления на один SellerID | Отправить GET запрос {{baseUrl}}/api/1/590538/item | 200 Ok, в теле JSON есть оба запрошенных ID и они одинаковые. | Passed
