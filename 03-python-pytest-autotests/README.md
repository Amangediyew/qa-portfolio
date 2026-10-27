# Проект 3. Автотесты на Python (pytest)

**Статус:** ⚪ Запланировано

## Цель
Автоматизировать проверки API и ключевые UI-сценарии.

## Стек
Python 3.x, pytest, requests, Playwright или Selenium, GitHub Actions.

## План
- [ ] API-тесты: 10–15 проверок (`requests` + `pytest`)
- [ ] UI-тесты для saucedemo.com: логин, корзина, оформление заказа
- [ ] Паттерн Page Object (`pages/`)
- [ ] Параметризация, фикстуры, маркеры (`smoke`, `regression`)
- [ ] HTML-отчёт (`pytest-html`) или Allure
- [ ] CI: запуск тестов в GitHub Actions

## Структура
- `tests/` — тесты
- `pages/` — page objects
- `requirements.txt` — зависимости (добавить)

## Запуск
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

## Результаты
(Количество тестов, скриншот прогона, ссылка на CI.)
