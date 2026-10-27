# Проект 2. API-тестирование (Postman + Newman)

**Статус:** ⚪ Запланировано

## Цель
Проверка публичного API: статус-коды, структура и данные ответов, негативные сценарии.

## Объект тестирования
Выберите одно: Swagger Petstore (https://petstore.swagger.io), reqres.in или JSONPlaceholder.

## План
- [ ] Изучить документацию (Swagger)
- [ ] Коллекция Postman: CRUD-запросы (GET, POST, PUT, DELETE)
- [ ] Переменные окружения (`baseUrl`, токены)
- [ ] Проверки (tests): статус-код, время ответа, поля JSON, схема
- [ ] Негативные сценарии: неверные данные, несуществующий ID, без авторизации
- [ ] Прогон коллекции через Newman и HTML-отчёт
- [ ] Список найденных замечаний

## Структура
- `collection/` — экспорт коллекции (`.postman_collection.json`)
- `environment/` — окружение (без секретов!)
- `reports/` — отчёты Newman

## Запуск
```
npm install -g newman newman-reporter-htmlextra
newman run collection/<имя>.postman_collection.json -e environment/<имя>.postman_environment.json -r htmlextra --reporter-htmlextra-export reports/report.html
```

## Результаты
(Количество запросов, пройдено/упало, найденные проблемы, ссылка на отчёт.)
