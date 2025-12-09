# КУРСОВАЯ РАБОТА
по МДК 11.01 «Технология разработки и защиты баз данных»

**Специальность:** 09.02.07 «Информационные системы и программирование»

**Тема:** «База данных агентства по аренде квартир»

**Срок представления работы к защите:** 20 декабря 2025 года

---

## **1. Анализ предметной области. Постановка задачи**

### **1.1. Описание предметной области и функции решаемых задач**

**Предметная область:** Агентство по краткосрочной и долгосрочной аренде квартир. Система предназначена для автоматизации бизнес-процессов управления объектами недвижимости, бронированиями, клиентами, сотрудниками и финансовыми операциями.

**Основные функции системы:**

1. Управление каталогом объектов недвижимости
2. Онлайн-бронирование квартир клиентами
3. Управление бронированиями (подтверждение, отмена, изменение)
4. Финансовый учёт (платежи, депозиты, возвраты)
5. Управление задачами по уборке и обслуживанию объектов
6. Ведение чёрного списка клиентов
7. Управление отзывами и рейтингами
8. Администрирование пользователей и ролевой доступ
9. Аналитика и отчётность
10. Работа с дополнительными услугами (трансфер, завтраки и др.)

### **1.2. Перечень входных данных**

**Данные пользователей:**

*   Регистрационные данные (email, пароль, ФИО, телефон)
*   Паспортные данные гостей
*   Данные сотрудников (должность, отдел, зарплата)

**Данные объектов недвижимости:**

*   Характеристики квартир (адрес, площадь, комнаты, удобства)
*   Фотографии объектов
*   Тарифы и цены
*   Информация о владельцах

**Данные бронирований:**

*   Даты заезда/выезда
*   Количество гостей
*   Особые пожелания
*   Выбранные услуги

**Финансовые данные:**

*   Информация о платежах
*   Данные промокодов и скидок
*   Стоимость уборок и дополнительных услуг

**Операционные данные:**

*   Задачи на уборку
*   Отзывы клиентов
*   Инвентарные проверки
*   Системные настройки

### **1.3. Перечень выходных данных**

**Отчёты и статистика:**

*   Отчёт по загрузке объектов
*   Финансовая отчётность
*   Статистика бронирований
*   Рейтинги объектов и гостей

**Документы:**

*   Подтверждения бронирования
*   Счета на оплату
*   Акты приёма-передачи имущества
*   Отчёты по уборкам

**Веб-интерфейс:**

*   Каталог доступных объектов
*   Панель управления для сотрудников
*   Личный кабинет клиента

**Уведомления:**

*   Email-уведомления о бронированиях
*   Напоминания о заездах/выездах
*   Уведомления о платежах
*   Сообщения о новых задачах

### **1.4. Ограничения предметной области**

**Безопасность данных:**

*   Конфиденциальность паспортных данных
*   Защита финансовой информации
*   Ограничение доступа к персональным данным

**Бизнес-правила:**

*   Минимальный срок бронирования — 1 ночь
*   Максимальный срок — 90 дней
*   Бесплатная отмена за 48 часов до заезда
*   Обязательный депозит 20% от стоимости

**Технические ограничения:**

*   Поддержка только российских номеров телефонов
*   Валюты расчётов — RUB
*   Интеграция с российскими платежными системами

### **1.5. Взаимодействие с другими программами**

**Платежные системы:**

*   ЮKassa
*   Тинькофф
*   Сбербанк Онлайн

**Email-сервисы:**

*   Отправка транзакционных писем
*   Рассылка маркетинговых материалов

**СМС-сервисы:**

*   Отправка подтверждений бронирования
*   Напоминания о заездах

**Картографические сервисы:**

*   Яндекс.Карты для отображения объектов
*   Построение маршрутов

---

## **2. Инфологическая (концептуальная) модель базы данных**

### **2.1. Выделение информационных объектов**

Основные информационные объекты системы:

1.  **Пользователь** — физическое лицо, работающее с системой
2.  **Сотрудник** — работник агентства
3.  **Гость** — клиент агентства
4.  **Объект недвижимости** — квартира/апартаменты для аренды
5.  **Тип объекта** — классификация объектов (квартира, студия, лофт и т.д.)
6.  **Категория объекта** — целевое назначение (эконом, премиум, бизнес)
7.  **Бронирование** — договор аренды на определённый период
8.  **Тариф** — условия аренды (посуточно, помесячно)
9.  **Платеж** — финансовая операция
10. **Услуга** — дополнительные опции (трансфер, уборка и др.)
11. **Уборка** — задача по обслуживанию объекта
12. **Отзыв** — оценка и комментарий гостя
13. **Инвентарь** — предметы мебели и техники в объекте

### **2.2. Определение атрибутов объектов**

**Пользователь:** ID, email, хеш пароля, роль, активность, телефон, аватар, дата последнего входа

**Объект недвижимости:** ID, владелец, тип, категория, адрес, город, район, метро, координаты, площадь, комнаты, гости, кровати, удобства, описание, статус активности

**Бронирование:** ID, номер брони, объект, гость, тариф, даты заезда/выезда, количество ночей, гости, стоимость, статус, особые пожелания

**Платеж:** ID, бронирование, сумма, способ оплаты, платежная система, статус, назначение, описание

### **2.3. Определение отношений и мощности отношений между объектами**

1.  **Пользователь (1) → Сотрудник (0..1)** — один к одному (опционально)
2.  **Пользователь (1) → Гость (0..1)** — один к одному (опционально)
3.  **Объект (1) → Бронирование (0..N)** — один ко многим
4.  **Гость (1) → Бронирование (0..N)** — один ко многим
5.  **Бронирование (1) → Платеж (1..N)** — один ко многим
6.  **Объект (1) → Уборка (0..N)** — один ко многим
7.  **Бронирование (1) → Отзыв (0..1)** — один к одному (опционально)
8.  **Объект (1) → Инвентарь (0..N)** — один ко многим

### **2.4. Построение концептуальной модели**

[Пользователь] 1---0..1 [Сотрудник]
| |
| 1---0..1 |
| |
[Гость] 1---0..N [Бронирование] 1---1..N [Платеж]
| | 1
| |
[Черный список] 0..1---1 [Объект] 1---0..N [Уборка]
|
| 1---0..N [Инвентарь]
|
[Отзыв] 0..1---1 [Бронирование]
text


---

## **3. Логическая структура БД**

**СУБД:** PostgreSQL 14+

**Нормализация:** Третья нормальная форма (3NF)

**Ключевые таблицы и связи:**

```sql
-- Основные таблицы
users (user_id PK)
employee (employee_id PK, user_id FK)
guest (guest_id PK, user_id FK)
property (property_id PK)
property_type (type_id PK)
property_category (category_id PK)
booking (booking_id PK, property_id FK, guest_id FK)
payment (payment_id PK, booking_id FK)
cleaning_task (task_id PK, booking_id FK, property_id FK)
review (review_id PK, booking_id FK, guest_id FK, property_id FK)

-- Справочники
rental_plan (plan_id PK)
service (service_id PK)
inventory_category (category_id PK)
site_setting (setting_id PK)
promo_code (promo_id PK)

-- Операционные таблицы
price_calendar (price_id PK, property_id FK)
booking_service (booking_service_id PK, booking_id FK, service_id FK)
inventory_item (item_id PK, property_id FK, category_id FK)
inventory_check (check_id PK, booking_id FK)

4. Физическая структура базы данных

Характеристики БД:

    Кодировка: UTF-8

    Схема: public

    Размер БД: ~1-2 ГБ (прогноз на 10 000 объектов)

    Количество таблиц: 25

Типы данных:

    Числовые: SERIAL (автоинкремент), INTEGER, DECIMAL(10,2)

    Строковые: VARCHAR(255), TEXT

    Дата/время: DATE, TIME, TIMESTAMP WITH TIME ZONE

    Логические: BOOLEAN

    Специальные: JSONB, INET (IP-адреса)

Ограничения целостности:

    Первичные ключи (PRIMARY KEY)

    Внешние ключи (FOREIGN KEY) с каскадным удалением

    Проверочные ограничения (CHECK)

    Уникальные ограничения (UNIQUE)

5. Реализация проекта в среде конкретной СУБД
5.1. Создание таблиц

Полный скрипт создания таблиц представлен в папке kochanov/kochanov.md. Создано 27 таблиц с полным набором ограничений целостности.

Особенности реализации:

    Использование SERIAL для автоинкремента

    Триггеры для автоматического обновления updated_at

    Генерация уникальных номеров бронирований

    Проверочные ограничения для статусов

5.2. Создание запросов

Типовые запросы системы:

    Поиск доступных объектов на даты:
    sql

SELECT p.*, pt.type_name, pc.category_name
FROM property p
JOIN property_type pt ON p.property_type_id = pt.type_id
JOIN property_category pc ON p.category_id = pc.category_id
WHERE p.is_active = TRUE
AND p.property_id NOT IN (
    SELECT property_id 
    FROM booking 
    WHERE status IN ('confirmed', 'active', 'paid')
    AND check_in_date <= '2024-12-25'
    AND check_out_date >= '2024-12-20'
)
AND p.city = 'Москва'
AND p.max_guests >= 2
ORDER BY p.rating DESC;

Отчёт по загрузке объектов:
sql

SELECT 
    p.property_id,
    p.title,
    p.city,
    COUNT(b.booking_id) as total_bookings,
    SUM(b.nights) as total_nights,
    SUM(b.total_price) as total_revenue,
    ROUND(AVG(r.overall_rating), 2) as avg_rating
FROM property p
LEFT JOIN booking b ON p.property_id = b.property_id 
    AND b.status IN ('completed', 'active')
LEFT JOIN review r ON p.property_id = r.property_id
WHERE p.is_active = TRUE
GROUP BY p.property_id, p.title, p.city
ORDER BY total_revenue DESC;

Финансовый отчёт за период:
sql

SELECT 
    DATE_TRUNC('month', p.created_at) as month,
    COUNT(p.payment_id) as payments_count,
    SUM(p.amount) as total_amount,
    COUNT(DISTINCT p.booking_id) as unique_bookings,
    AVG(p.amount) as avg_payment
FROM payment p
WHERE p.payment_status = 'completed'
    AND p.created_at BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY DATE_TRUNC('month', p.created_at)
ORDER BY month DESC;

5.3. Разработка интерфейса

Архитектура веб-приложения:

    Frontend: HTML5, CSS3, Bootstrap 5, JavaScript

    Backend: PHP 8.1+

    Сервер: Apache 2.4

    СУБД: PostgreSQL 14+

Структура веб-приложения:
text

/var/www/html/rental_simple/
├── index.php          # Главная страница
├── login.php          # Страница входа
├── register.php       # Регистрация пользователей
├── logout.php         # Выход из системы
├── stats.php          # Статистика
├── config.php         # Конфигурация БД
├── auth.php           # Функции аутентификации
├── functions.php      # Общие функции
├── navbar.php         # Навигационная панель
├── style.css          # Стили
└── admin.php          # Админ-панель

Основные возможности интерфейса:

    Аутентификация и авторизация

    Просмотр и управление таблицами БД

    Выполнение SQL-запросов (для администраторов)

    Панель статистики

    Адаптивный дизайн для мобильных устройств

    Ролевой доступ (гость, сотрудник, администратор)

5.4. Назначение прав доступа

Роли пользователей:

    Гость (guest):

        Просмотр доступных объектов

        Создание бронирований

        Просмотр своих бронирований

        Оставление отзывов

    Сотрудник (employee):

        Все права гостей

        Управление бронированиями

        Просмотр всех объектов

        Управление задачами по уборке

        Работа с отзывами (модерация)

    Уборщик (cleaner):

        Просмотр задач по уборке

        Отметка о выполнении задач

        Просмотр информации об объектах

    Администратор (admin):

        Полный доступ ко всем данным

        Управление пользователями

        Настройка системы

        Выполнение произвольных SQL-запросов

        Доступ к админ-панели

SQL для создания ролей:
sql

-- Создание ролей в PostgreSQL
CREATE ROLE rental_guest;
CREATE ROLE rental_employee;
CREATE ROLE rental_cleaner;
CREATE ROLE rental_admin;

-- Назначение прав
GRANT SELECT ON property, property_type, property_category TO rental_guest;
GRANT INSERT, UPDATE ON booking, payment TO rental_guest;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO rental_employee;
GRANT INSERT, UPDATE, DELETE ON booking, payment, cleaning_task TO rental_employee;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO rental_admin;

5.5. Создание индексов

Критически важные индексы:
sql

-- Для быстрого поиска пользователей
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role ON users(role);
CREATE INDEX idx_users_last_login ON users(last_login);

-- Для поиска объектов
CREATE INDEX idx_property_city ON property(city);
CREATE INDEX idx_property_dates ON property(is_active, featured);
CREATE INDEX idx_property_type ON property(property_type_id);
CREATE INDEX idx_property_category ON property(category_id);

-- Для работы с бронированиями
CREATE INDEX idx_booking_dates ON booking(check_in_date, check_out_date, status);
CREATE INDEX idx_booking_guest ON booking(guest_id, status);
CREATE INDEX idx_booking_property ON booking(property_id, status);
CREATE INDEX idx_booking_dates_range ON booking 
    USING gist (daterange(check_in_date, check_out_date));

-- Для финансовых операций
CREATE INDEX idx_payment_booking ON payment(booking_id);
CREATE INDEX idx_payment_status ON payment(payment_status);
CREATE INDEX idx_payment_created ON payment(created_at);

-- Для поиска в черном списке
CREATE INDEX idx_blacklist_search ON blacklist(banned_phone, banned_passport, is_active);

-- Для полнотекстового поиска объектов
CREATE INDEX idx_property_search ON property USING gin(
    to_tsvector('russian', 
        title || ' ' || 
        address || ' ' || 
        city || ' ' || 
        description || ' ' || 
        short_description
    )
);

Составные индексы для оптимизации частых запросов:
sql

-- Для календаря цен
CREATE INDEX idx_price_calendar_search ON price_calendar(property_id, date, is_blocked);

-- Для поиска отзывов
CREATE INDEX idx_review_property ON review(property_id, is_approved, created_at DESC);

-- Для статистических запросов
CREATE INDEX idx_booking_financial ON booking(created_at, status, total_price);

5.6. Разработка стратегии резервного копирования базы данных

Ежедневные инкрементальные бэкапы:
bash

#!/bin/bash
# backup_daily.sh
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backup/postgres/daily"
PGPASSWORD="yourpassword" pg_dump -h localhost -U postgres -d kursovaya -Fc -f $BACKUP_DIR/kursovaya_$DATE.dump
find $BACKUP_DIR -name "*.dump" -mtime +7 -delete

Еженедельные полные бэкапы:
bash

#!/bin/bash
# backup_weekly.sh
DATE=$(date +%Y%m%d)
BACKUP_DIR="/backup/postgres/weekly"
PGPASSWORD="yourpassword" pg_dump -h localhost -U postgres -d kursovaya -Fc -f $BACKUP_DIR/kursovaya_full_$DATE.dump
find $BACKUP_DIR -name "*.dump" -mtime +30 -delete

Репликация:
sql

-- Настройка мастер-слейв репликации
-- На мастере:
ALTER SYSTEM SET wal_level = replica;
ALTER SYSTEM SET max_wal_senders = 10;
ALTER SYSTEM SET wal_keep_size = 1024;

-- На слейве:
pg_basebackup -h master_host -D /var/lib/postgresql/14/main -U replicator -P -v -R

План восстановления:

    Критическая потеря данных (до 1 часа):
    bash

pg_restore -h localhost -U postgres -d kursovaya -c /backup/postgres/daily/latest.dump

Аварийное восстановление (до 24 часов):
bash

pg_restore -h standby_server -U postgres -d kursovaya -c /backup/postgres/weekly/latest.dump

Мониторинг бэкапов:
sql

-- Проверка последнего бэкапа
SELECT 
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size
FROM pg_tables 
WHERE schemaname NOT IN ('pg_catalog', 'information_schema')
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;

Заключение

В ходе курсовой работы была разработана полноценная информационная система управления арендой квартир, включающая:

    Проектирование БД — создана нормализованная структура из 27 таблиц

    Реализация на PostgreSQL — использованы современные возможности СУБД (JSONB, триггеры, индексы)

    Веб-интерфейс — разработан интуитивно понятный интерфейс на PHP/HTML/CSS

    Система безопасности — реализована многоуровневая аутентификация и авторизация

    Оптимизация — созданы индексы для критически важных запросов

    Стратегия резервного копирования — разработан план сохранности данных

Система готова к использованию в реальных условиях работы агентства аренды недвижимости и может быть масштабирована для поддержки тысяч объектов и десятков тысяч пользователей.

Руководитель работы __________________ /И. В. Пунгин/

Задание принял к исполнению __________________ /Кочанов А.М./
text
