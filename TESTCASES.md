| Заголовок  | Предусловие | Шаги проверки | Ожидаемый результат | Статус прохождения
| :-------------: | :-------------: | :-------------: | :-------------: |  :-------------: |
| Успешное создание объявления от пользователя с корректными данными | Headers request: Content-Type: application/json  | Отправить POST запрос {{baseUrl}}/api/1/item JSON тело с полями sellerID в диапазоне 111111-999999, name Valenki, price 30000, statistics{likes 0, viewCount 0, contacts 0} | 200 Ок | Failed
| Корректная валидация типов: SellerID строкой | Headers request: Content-Type: application/json  | Отправить JSON тело с полем sellerID "111111" | 400 Bad | Passed
| Корректная проверка на отсутствие обязательных полей| Headers request: Content-Type: application/json  |  Удалить ключ и значение SellerID из тела JSON, удалить name, удалить price | 400 Bad | Passed
| Проверка на корректность значения price | Headers request: Content-Type: application/json | Ввести значение price -1 | 400 Bad | Failed
| Проверка на корректность значения price | Headers request: Content-Type: application/json | Ввести значение price 0 | 200 Ok | Failed
| Успешное создание объявления от пользователя с корректными данными | Headers request: Content-Type: application/json  | Отправить POST запрос {{baseUrl}}/api/1/item JSON тело с полями sellerID в диапазоне 111111-999999, name valenok, price 999999999, statistics{likes 1, viewCount 1, contacts 1} | 200 Ок | Passed
| Успешное получение объявления по id | Объявление создано, id сохранен  | Отправить GET запрос {{baseUrl}}/api/1/item/e481ff14-ecc1-480e-9299-4743e5d49cea | 200 Ок, ответ - тело JSON c корректными данными | Passed
| Запрос несуществующего id объявления | id объявления не создан и не сохранен | Отправить GET запрос {{baseUrl}}/api/1/item/e481ff14-ecc1-480e-9299-4743e5d49cee | 404 Not Found | Passed
| Запрос невалидного id объявления | Некорректная форма записи id  | Отправить GET запрос {{baseUrl}}/api/1/item/ahugufg | 400 Bad Request | Passed
| Корректная выдача списка всех объявлений продавца | Созданы 2 объявления на один SellerID | Отправить GET запрос {{baseUrl}}/api/1/590538/item | 200 Ok, в теле JSON есть оба запрошенных SellerID, они идентичны и совпадают с запрошенным. | Passed
| Запрос объявления по невалидному SellerID | SellerID в диапазоне меньше значения 111111 | Отправить GET запрос {{baseUrl}}/api/1/111110/item | 400 Bad Request | Failed
| Запрос объявления по невалидному SellerID | SellerID в диапазоне больше значения 999999 | Отправить GET запрос {{baseUrl}}/api/1/1000000/item | 400 Bad Request | Failed
| Запрос объявления по невалидному SellerID | SellerID равен 0 | Отправить GET запрос {{baseUrl}}/api/1/0/item | 400 Bad Request | Failed
| Запрос объявления по невалидному SellerID | SellerID равен -1 | Отправить GET запрос {{baseUrl}}/api/-1/0/item | 400 Bad Request | Failed
| Корректная выдача статистики по id объявления | Объявление создано и ему присвоен id | Отправить GET запрос {{baseUrl}}/api/2/statistic/e481ff14-ecc1-480e-9299-4743e5d49cea | 200 Ok, тело JSON содержит идентичные ранее присвоенные значения likes, viewCount, contacts и они >= 0 | Passed
| Запрос статистики для несуществующего id объявления | id объявления не создан и не сохранен | Отправить GET запрос {{baseUrl}}/api/2/statistic/e481ff14-ecc1-480e-9299-4743e5d49cee | 404 Not Found | Passed
| Запрос статистики для невалидного id объявления | Некорректная форма записи id | Отправить GET запрос {{baseUrl}}/api/2/statistic/ahugufg | 400 Bad Request | Passed
