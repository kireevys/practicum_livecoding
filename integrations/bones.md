# Интеграция программных систем

## Что такое интеграция?

> Интегра́ция (от лат. integratio — «восстановление», «восполнение», «соединение») — процесс объединения частей в целое.

- Клиент-Сервер![Клиент.png](static/client_server.png)
- Источник
- Сервис
- Мастер система (буква S)

## Протокол обмена

- Контрактное программирование
  ![contract.png](static/contract.png)
- Варианты связей
    - Системный вызов
    - shared-resource
    - http
    - Очереди
      ![Очереди.png](static/queues.png)

## Готовность приложения к интеграции

- Версионность API

![versions](static/versions.png)

- Документация
- Специализированные методы (буква I)
- Поддержка нескольких протоколов (буква D)

![Гексагональная архитектура](static/hexagon.png)
![img.png](static/hexagon_additional.png)

- Deprecated возможности
- Обратная совместимость

## Модели и данные

- Валидация
- Паттерн Адаптер
  ![Адаптер.png](static/adapter.png)
- Расширение (буква О)
- ACL

## Согласованность изменений

- Транзакции
- Outbox