Специальность: 09.02.07 "Информационные системы и программирование"

Тема курсовой работы: База данных агентства по аренде квартир.

Срок представления работы к защите: 20 декабря 2025 года.

Перечень подлежащих разработке вопросов:

  1.  Анализ предметной области. Постановка задачи.

    1.1. Описание предметной области и функции решаемых задач.
Предметная область: Агентство по краткосрочной и долгосрочной аренде квартир. Система предназначена для автоматизации бизнес-процессов управления объектами недвижимости, бронированиями, клиентами, сотрудниками и финансовыми операциями.

Основные функции системы:

    Управление каталогом объектов недвижимости

    Онлайн-бронирование квартир клиентами

    Управление бронированиями (подтверждение, отмена, изменение)

    Финансовый учёт (платежи, депозиты, возвраты)

    Управление задачами по уборке и обслуживанию объектов

    Ведение чёрного списка клиентов

    Управление отзывами и рейтингами

    Администрирование пользователей и ролевой доступ

    Аналитика и отчётность

    Работа с дополнительными услугами (трансфер, завтраки и др.)
    1.2. Перечень входных данных.
    Данные пользователей:

        Регистрационные данные (email, пароль, ФИО, телефон)

        Паспортные данные гостей

        Данные сотрудников (должность, отдел, зарплата)

    Данные объектов недвижимости:

        Характеристики квартир (адрес, площадь, комнаты, удобства)

        Фотографии объектов

        Тарифы и цены

        Информация о владельцах

    Данные бронирований:

        Даты заезда/выезда

        Количество гостей

        Особые пожелания

        Выбранные услуги

    Финансовые данные:

        Информация о платежах

        Данные промокодов и скидок

        Стоимость уборок и дополнительных услуг

    Операционные данные:

        Задачи на уборку

        Отзывы клиентов

        Инвентарные проверки

        Системные настройки
    1.3. Перечень выходных данных
    Отчёты и статистика:

        Отчёт по загрузке объектов

        Финансовая отчётность

        Статистика бронирований

        Рейтинги объектов и гостей

    Документы:

        Подтверждения бронирования

        Счета на оплату

        Акты приёма-передачи имущества

        Отчёты по уборкам

    Веб-интерфейс:

        Каталог доступных объектов

        Календарь занятости

        Панель управления для сотрудников

        Личный кабинет клиента

    Уведомления:

        Email-уведомления о бронированиях

        Напоминания о заездах/выездах

        Уведомления о платежах

        Сообщения о новых задачах
    1.4. Ограничения предметной области (если таковые имеются).
    Безопасность данных:

        Конфиденциальность паспортных данных

        Защита финансовой информации

        Ограничение доступа к персональным данным

    Бизнес-правила:

        Минимальный срок бронирования - 1 ночь

        Максимальный срок - 90 дней

        Бесплатная отмена за 48 часов до заезда

        Обязательный депозит 20% от стоимости

    Технические ограничения:

        Поддержка только российских номеров телефонов

        Валюты расчётов - RUB

        Интеграция с российскими платежными системами
    1.5. Взаимодействие с другими программами.
    Платежные системы:

        ЮKassa

        Тинькофф

        Сбербанк Онлайн

    Email-сервисы:

        Отправка транзакционных писем

        Рассылка маркетинговых материалов

    СМС-сервисы:

        Отправка подтверждений бронирования

        Напоминания о заездах

    Картографические сервисы:

        Яндекс.Карты для отображения объектов

        Построение маршрутов
   2. Инфологическая (концептуальная) модель базы данных.

    2.1. Выделение информационных объектов.
Основные информационные объекты системы:

    Пользователь - физическое лицо, работающее с системой

    Сотрудник - работник агентства

    Гость - клиент агентства

    Объект недвижимости - квартира/апартаменты для аренды

    Тип объекта - классификация объектов (квартира, студия, лофт и т.д.)

    Категория объекта - целевое назначение (эконом, премиум, бизнес)

    Бронирование - договор аренды на определённый период

    Тариф - условия аренды (посуточно, помесячно)

    Платеж - финансовая операция

    Услуга - дополнительные опции (трансфер, уборка и др.)

    Уборка - задача по обслуживанию объекта

    Отзыв - оценка и комментарий гостя

    Инвентарь - предметы мебели и техники в объекте
    2.2. Определение атрибутов объектов.
Пользователь:

    ID, email, хеш пароля, роль, активность, телефон, аватар, дата последнего входа

Объект недвижимости:

    ID, владелец, тип, категория, адрес, город, район, метро, координаты, площадь, комнаты, гости, кровати, удобства, описание, статус активности

Бронирование:

    ID, номер брони, объект, гость, тариф, даты заезда/выезда, количество ночей, гости, стоимость, статус, особые пожелания

Платеж:

    ID, бронирование, сумма, способ оплаты, платежная система, статус, назначение, описание
    2.3. Определение отношений и мощности отношений между объектами.
    Пользователь (1) → Сотрудник (0..1) - один к одному (опционально)

    Пользователь (1) → Гость (0..1) - один к одному (опционально)

    Объект (1) → Бронирование (0..N) - один ко многим

    Гость (1) → Бронирование (0..N) - один ко многим

    Бронирование (1) → Платеж (1..N) - один ко многим

    Объект (1) → Уборка (0..N) - один ко многим

    Бронирование (1) → Отзыв (0..1) - один к одному (опционально)

    Объект (1) → Инвентарь (0..N) - один ко многим
    2.4. Построение концептуальной модели.
[Пользователь] 1---0..1 [Сотрудник]
      |                     |
      | 1---0..1            |
      |                     |
    [Гость] 1---0..N [Бронирование] 1---1..N [Платеж]
      |                     | 1
      |                     | 
[Черный список] 0..1---1 [Объект] 1---0..N [Уборка]
                             |
                             | 1---0..N [Инвентарь]
                             |
                          [Отзыв] 0..1---1 [Бронирование]
   3. Логическая структура БД.
СУБД: PostgreSQL 14+

Нормализация: Третья нормальная форма (3NF)

Ключевые таблицы и связи:
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
   4. Физическая структура базы данных.
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
   5. Реализация проекта в среде конкретной СУБД.

    5.1. Создание таблиц.
-- Таблица пользователей для авторизации на сайте
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,                 -- Уникальный ID пользователя
    email VARCHAR(255) UNIQUE NOT NULL,        -- Email (логин)
    password_hash VARCHAR(255) NOT NULL,        -- Хеш пароля (bcrypt)
    role VARCHAR(50) NOT NULL DEFAULT 'guest', -- Роль: guest, employee, admin, cleaner
    is_active BOOLEAN DEFAULT TRUE,            -- Активен ли аккаунт
    email_verified BOOLEAN DEFAULT FALSE,      -- Подтвержден ли email
    phone VARCHAR(50),                          -- Телефон для связи
    avatar_url TEXT,                            -- Ссылка на аватар
    last_login TIMESTAMP WITH TIME ZONE,        -- Дата последнего входа
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
-- Сотрудники агентства (привязаны к users)
CREATE TABLE employee (
    employee_id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE REFERENCES users(user_id) ON DELETE SET NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    position VARCHAR(100) NOT NULL,           -- Должность
    hire_date DATE NOT NULL,                  -- Дата найма
    salary DECIMAL(10,2),                     -- Зарплата
    bank_account VARCHAR(100),                -- Банковский счет для зарплаты
    is_active BOOLEAN DEFAULT TRUE,
    department VARCHAR(50),                    -- Отдел: sales, cleaning, support
    notes TEXT,                               -- Дополнительные заметки
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
-- Гости/клиенты (также привязаны к users)
CREATE TABLE guest (
    guest_id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE REFERENCES users(user_id) ON DELETE SET NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    phone VARCHAR(50) UNIQUE NOT NULL,
    passport_number VARCHAR(100),              -- Номер паспорта
    passport_issue_date DATE,                  -- Дата выдачи
    passport_issued_by TEXT,                   -- Кем выдан
    date_of_birth DATE,                        -- Дата рождения
    preferred_language VARCHAR(10) DEFAULT 'ru', -- Язык предпочтений
    marketing_consent BOOLEAN DEFAULT FALSE,   -- Согласие на рассылку
    verified BOOLEAN DEFAULT FALSE,            -- Верифицирован
    rating DECIMAL(3,2) DEFAULT 5.0,           -- Рейтинг
    total_bookings INTEGER DEFAULT 0,          -- Всего бронирований
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
-- Типы объектов для фильтрации на сайте
CREATE TABLE property_type (
    type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,    -- Название типа
    icon_class VARCHAR(100),                   -- Класс иконки для сайта
    description TEXT                           -- Описание типа
);
CREATE TABLE property_category (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL UNIQUE, -- Название категории
    slug VARCHAR(50) UNIQUE NOT NULL,         -- ЧПУ для URL
    sort_order INTEGER DEFAULT 0              -- Порядок отображения
);
CREATE TABLE property (
    property_id SERIAL PRIMARY KEY,
    owner_name VARCHAR(255) NOT NULL,         -- Владелец (физическое лицо или компания)
    property_type_id INTEGER REFERENCES property_type(type_id),
    category_id INTEGER REFERENCES property_category(category_id),
    title VARCHAR(255) NOT NULL,              -- Заголовок для сайта
    slug VARCHAR(255) UNIQUE NOT NULL,        -- ЧПУ для URL объекта
    address VARCHAR(500) NOT NULL,
    city VARCHAR(100) NOT NULL,
    district VARCHAR(100),                     -- Район
    metro_station VARCHAR(100),                -- Станция метро
    latitude DECIMAL(10,8),                    -- Широта для карты
    longitude DECIMAL(11,8),                   -- Долгота для карты
    floor INTEGER NOT NULL,                    -- Этаж
    floors_in_building INTEGER,                -- Этажей в доме
    area_sq_m DECIMAL(10,2) NOT NULL,         -- Площадь
    rooms INTEGER NOT NULL,                    -- Количество комнат
    max_guests INTEGER NOT NULL,              -- Максимум гостей
    beds INTEGER NOT NULL,                     -- Количество кроватей
    has_wifi BOOLEAN DEFAULT TRUE,            -- Есть Wi-Fi
    has_tv BOOLEAN DEFAULT TRUE,              -- Есть телевизор
    has_kitchen BOOLEAN DEFAULT TRUE,         -- Есть кухня
    has_washer BOOLEAN DEFAULT FALSE,         -- Есть стиральная машина
    has_ac BOOLEAN DEFAULT FALSE,             -- Есть кондиционер
    has_parking BOOLEAN DEFAULT FALSE,        -- Есть парковка
    pets_allowed BOOLEAN DEFAULT FALSE,       -- Разрешены животные
    smoking_allowed BOOLEAN DEFAULT FALSE,    -- Разрешено курение
    description TEXT NOT NULL,                 -- Полное описание
    short_description VARCHAR(500),           -- Краткое описание для карточки
    check_in_time TIME DEFAULT '14:00',       -- Время заезда
    check_out_time TIME DEFAULT '12:00',      -- Время выезда
    is_active BOOLEAN DEFAULT TRUE,           -- Активен для бронирования
    featured BOOLEAN DEFAULT FALSE,           -- Выделенный объект на главной
    views_count INTEGER DEFAULT 0,            -- Количество просмотров
    rating DECIMAL(3,2) DEFAULT 0,            -- Средний рейтинг
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    managed_by_employee_id INTEGER REFERENCES employee(employee_id) -- Ответственный менеджер
);
CREATE TABLE property_photo (
    photo_id SERIAL PRIMARY KEY,
    property_id INTEGER NOT NULL REFERENCES property(property_id) ON DELETE CASCADE,
    photo_url TEXT NOT NULL,                  -- URL фотографии на CDN
    photo_thumb_url TEXT,                     -- URL миниатюры
    caption VARCHAR(255),                     -- Подпись к фото
    sort_order INTEGER DEFAULT 0,             -- Порядок сортировки
    is_main BOOLEAN DEFAULT FALSE,           -- Главное фото
    uploaded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE rental_plan (
    plan_id SERIAL PRIMARY KEY,
    plan_name VARCHAR(100) NOT NULL,
    rental_type VARCHAR(20) NOT NULL CHECK (rental_type IN ('daily', 'monthly')),
    min_nights INTEGER DEFAULT 1,
    max_nights INTEGER,
    base_price_per_night DECIMAL(10,2),
    monthly_discount_percent DECIMAL(5,2) DEFAULT 0,
    description TEXT,
    features JSONB DEFAULT '[]'               -- Дополнительные возможности в JSON
);
CREATE TABLE price_calendar (
    price_id SERIAL PRIMARY KEY,
    property_id INTEGER NOT NULL REFERENCES property(property_id) ON DELETE CASCADE,
    date DATE NOT NULL,                       -- Конкретная дата
    price_per_night DECIMAL(10,2) NOT NULL,   -- Цена за ночь на эту дату
    is_blocked BOOLEAN DEFAULT FALSE,         -- Заблокирована ли дата для бронирования
    min_stay INTEGER,                         -- Минимальное количество ночей на этот период
    notes VARCHAR(255),                       -- Примечания (праздники, события)
    UNIQUE(property_id, date)
);
CREATE TABLE booking (
    booking_id SERIAL PRIMARY KEY,
    property_id INTEGER NOT NULL REFERENCES property(property_id),
    guest_id INTEGER NOT NULL REFERENCES guest(guest_id),
    plan_id INTEGER NOT NULL REFERENCES rental_plan(plan_id),
    employee_id INTEGER REFERENCES employee(employee_id),
    
    -- Основные данные бронирования
    booking_number VARCHAR(20) UNIQUE NOT NULL, -- Уникальный номер для клиента (BKG-2024-001)
    status VARCHAR(30) NOT NULL CHECK (status IN ('pending', 'confirmed', 'paid', 'active', 'completed', 'cancelled', 'refunded')),
    
    -- Даты проживания
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    nights INTEGER NOT NULL,
    
    -- Гости
    adults INTEGER NOT NULL DEFAULT 1,
    children INTEGER DEFAULT 0,
    pets INTEGER DEFAULT 0,
    
    -- Цены и платежи
    base_price DECIMAL(12,2) NOT NULL,      -- Базовая стоимость
    cleaning_fee DECIMAL(8,2) DEFAULT 1000, -- Плата за уборку
    service_fee DECIMAL(8,2) DEFAULT 500,   -- Сервисный сбор
    deposit_amount DECIMAL(10,2) DEFAULT 5000, -- Залог
    total_price DECIMAL(12,2) NOT NULL,     -- Итоговая сумма
    paid_amount DECIMAL(12,2) DEFAULT 0,
    
    -- Контактная информация на время проживания
    contact_phone VARCHAR(50),
    special_requests TEXT,
    
    -- Системные поля
    source VARCHAR(50) DEFAULT 'website',   -- Источник брони: website, phone, partner
    cancellation_reason TEXT,
    refund_amount DECIMAL(10,2) DEFAULT 0,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT valid_dates CHECK (check_out_date > check_in_date),
    CONSTRAINT valid_guests CHECK (adults > 0)
);
CREATE TABLE cleaning_task (
    task_id SERIAL PRIMARY KEY,
    booking_id INTEGER REFERENCES booking(booking_id) ON DELETE SET NULL,
    property_id INTEGER NOT NULL REFERENCES property(property_id),
    cleaner_id INTEGER REFERENCES employee(employee_id),
    
    -- Детали задачи
    task_type VARCHAR(30) DEFAULT 'checkout', -- Тип: checkout, weekly, deep
    scheduled_date DATE NOT NULL,              -- Дата уборки
    scheduled_time TIME NOT NULL,              -- Время уборки
    estimated_duration INTEGER,                -- Продолжительность в минутах
    
    -- Статус и контроль качества
    status VARCHAR(20) NOT NULL CHECK (status IN ('scheduled', 'in_progress', 'completed', 'cancelled', 'requires_inspection')),
    started_at TIMESTAMP WITH TIME ZONE,
    completed_at TIMESTAMP WITH TIME ZONE,
    
    -- Контроль качества
    inspector_id INTEGER REFERENCES employee(employee_id),
    quality_rating INTEGER CHECK (quality_rating >= 1 AND quality_rating <= 5),
    inspection_notes TEXT,
    
    -- Финансы
    cleaning_cost DECIMAL(8,2) NOT NULL,       -- Стоимость уборки (зарплата клинеру)
    extra_charges DECIMAL(8,2) DEFAULT 0,      -- Дополнительные расходы (химия и т.д.)
    
    -- Материалы
    used_supplies JSONB DEFAULT '{}',          -- Использованные материалы в JSON
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE review (
    review_id SERIAL PRIMARY KEY,
    booking_id INTEGER UNIQUE NOT NULL REFERENCES booking(booking_id),
    guest_id INTEGER NOT NULL REFERENCES guest(guest_id),
    property_id INTEGER NOT NULL REFERENCES property(property_id),
    
    -- Оценки гостя
    cleanliness_rating INTEGER CHECK (cleanliness_rating >= 1 AND cleanliness_rating <= 5),
    location_rating INTEGER CHECK (location_rating >= 1 AND location_rating <= 5),
    value_rating INTEGER CHECK (value_rating >= 1 AND value_rating <= 5),
    service_rating INTEGER CHECK (service_rating >= 1 AND location_rating <= 5),
    overall_rating DECIMAL(2,1) NOT NULL,      -- Общая оценка
    
    -- Текстовые отзывы
    title VARCHAR(255),                         -- Заголовок отзыва
    comment TEXT NOT NULL,                      -- Текст отзыва
    host_response TEXT,                         -- Ответ владельца/менеджера
    
    -- Модерация
    is_approved BOOLEAN DEFAULT FALSE,         -- Одобрен для публикации
    moderated_by INTEGER REFERENCES employee(employee_id),
    moderation_notes TEXT,
    
    -- Для рекомендаций
    would_recommend BOOLEAN,                    -- Порекомендовал бы другим
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE blacklist (
    blacklist_id SERIAL PRIMARY KEY,
    guest_id INTEGER REFERENCES guest(guest_id) ON DELETE CASCADE,
    
    -- Альтернативные идентификаторы (если гость еще не в системе)
    banned_first_name VARCHAR(100),
    banned_last_name VARCHAR(100),
    banned_phone VARCHAR(50),
    banned_email VARCHAR(255),
    banned_passport VARCHAR(100),
    
    -- Причина и детали
    reason TEXT NOT NULL,
    incident_date DATE,
    incident_description TEXT,
    
    -- Уровень риска и ограничения
    risk_level VARCHAR(20) CHECK (risk_level IN ('low', 'medium', 'high', 'critical')),
    ban_type VARCHAR(30) DEFAULT 'full',       -- Тип блокировки: full, limited
    ban_duration_days INTEGER,                 -- Срок блокировки (NULL = вечная)
    
    -- Кто внес
    added_by_employee_id INTEGER REFERENCES employee(employee_id),
    added_by_reason TEXT,
    
    -- Статус
    is_active BOOLEAN DEFAULT TRUE,
    auto_check_enabled BOOLEAN DEFAULT TRUE,   -- Автоматическая проверка новых бронирований
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expires_at DATE,                           -- Дата окончания блокировки
    CONSTRAINT check_identifier CHECK (
        guest_id IS NOT NULL OR 
        banned_phone IS NOT NULL OR 
        banned_passport IS NOT NULL
    )
);
-- Таблица для сессий пользователей
CREATE TABLE user_sessions (
    session_id VARCHAR(255) PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    token TEXT NOT NULL,
    ip_address INET,
    user_agent TEXT,
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Логи действий пользователей (для аудита)
CREATE TABLE audit_log (
    log_id BIGSERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    action VARCHAR(100) NOT NULL,              -- Действие: login, booking_create, etc.
    entity_type VARCHAR(50),                    -- Сущность: booking, property, etc.
    entity_id INTEGER,                          -- ID сущности
    old_values JSONB,                           -- Старые значения
    new_values JSONB,                           -- Новые значения
    ip_address INET,
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE payment (
    payment_id SERIAL PRIMARY KEY,
    booking_id INTEGER NOT NULL REFERENCES booking(booking_id),
    user_id INTEGER REFERENCES users(user_id),           -- Кто оплатил
    amount DECIMAL(12,2) NOT NULL,                       -- Сумма платежа
    currency VARCHAR(3) DEFAULT 'RUB',                   -- Валюта
    payment_method VARCHAR(50) NOT NULL,                 -- Способ оплаты: card, cash, transfer, etc.
    payment_gateway VARCHAR(50),                         -- Платежная система: yookassa, tinkoff, etc.
    transaction_id VARCHAR(255) UNIQUE,                  -- ID транзакции в платежной системе
    payment_status VARCHAR(30) NOT NULL CHECK (           -- Статус платежа
        payment_status IN ('pending', 'processing', 'completed', 'failed', 'refunded', 'cancelled')
    ),
    purpose VARCHAR(100) NOT NULL,                       -- Назначение: booking, deposit_refund, penalty, etc.
    description TEXT,                                    -- Описание платежа
    receipt_url TEXT,                                    -- Ссылка на чек
    metadata JSONB DEFAULT '{}',                         -- Дополнительные данные платежной системы
    
    -- Для возвратов
    refund_reason TEXT,
    refunded_by INTEGER REFERENCES employee(employee_id),
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Индексы для быстрого поиска
    CONSTRAINT fk_booking FOREIGN KEY (booking_id) REFERENCES booking(booking_id) ON DELETE CASCADE
);
CREATE TABLE notification (
    notification_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    notification_type VARCHAR(50) NOT NULL,               -- Тип: booking_confirmed, payment_received, etc.
    title VARCHAR(255) NOT NULL,                         -- Заголовок уведомления
    message TEXT NOT NULL,                               -- Текст уведомления
    is_read BOOLEAN DEFAULT FALSE,                       -- Прочитано ли
    is_email_sent BOOLEAN DEFAULT FALSE,                 -- Отправлено ли на email
    is_push_sent BOOLEAN DEFAULT FALSE,                  -- Отправлено ли push
    priority VARCHAR(20) DEFAULT 'normal' CHECK (        -- Приоритет
        priority IN ('low', 'normal', 'high', 'urgent')
    ),
    
    -- Ссылка на связанную сущность
    related_entity_type VARCHAR(50),                     -- booking, payment, review
    related_entity_id INTEGER,                           -- ID связанной сущности
    
    metadata JSONB DEFAULT '{}',                         -- Дополнительные данные
    scheduled_for TIMESTAMP WITH TIME ZONE,              -- Когда отправить (для отложенных)
    sent_at TIMESTAMP WITH TIME ZONE,                    -- Когда отправлено
    read_at TIMESTAMP WITH TIME ZONE,                    -- Когда прочитано
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE message (
    message_id SERIAL PRIMARY KEY,
    thread_id VARCHAR(100) NOT NULL,                     -- ID диалога (например: user_1_employee_2)
    
    -- Участники диалога
    sender_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    receiver_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    
    -- Контент сообщения
    message_text TEXT NOT NULL,
    attachments JSONB DEFAULT '[]',                      -- Прикрепленные файлы
    
    -- Статус
    is_read BOOLEAN DEFAULT FALSE,
    read_at TIMESTAMP WITH TIME ZONE,
    
    -- Связь с бронированием (опционально)
    booking_id INTEGER REFERENCES booking(booking_id),
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Индексы для быстрого поиска диалогов
    CONSTRAINT check_different_users CHECK (sender_id != receiver_id)
);
CREATE TABLE service (
    service_id SERIAL PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,                  -- Название услуги
    service_type VARCHAR(50) NOT NULL CHECK (            -- Тип услуги
        service_type IN ('cleaning', 'transfer', 'food', 'equipment', 'other')
    ),
    description TEXT,                                    -- Описание услуги
    price DECIMAL(8,2) NOT NULL,                        -- Цена
    currency VARCHAR(3) DEFAULT 'RUB',
    duration_minutes INTEGER,                            -- Продолжительность (если применимо)
    is_available BOOLEAN DEFAULT TRUE,                  -- Доступна ли услуга
    requires_booking BOOLEAN DEFAULT TRUE,              -- Требуется ли бронирование
    max_per_day INTEGER,                                -- Максимум в день (для ограничения)
    
    -- Для веб-сайта
    icon_class VARCHAR(100),                            -- Класс иконки
    display_order INTEGER DEFAULT 0,                    -- Порядок отображения
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Заказ услуг к бронированию
CREATE TABLE booking_service (
    booking_service_id SERIAL PRIMARY KEY,
    booking_id INTEGER NOT NULL REFERENCES booking(booking_id) ON DELETE CASCADE,
    service_id INTEGER NOT NULL REFERENCES service(service_id),
    quantity INTEGER DEFAULT 1,
    unit_price DECIMAL(8,2) NOT NULL,                   -- Цена на момент заказа
    total_price DECIMAL(10,2) NOT NULL,                 -- Итоговая цена (quantity * unit_price)
    scheduled_date DATE,                                -- Дата оказания услуги
    scheduled_time TIME,                                -- Время оказания
    status VARCHAR(20) DEFAULT 'pending' CHECK (        -- Статус услуги
        status IN ('pending', 'confirmed', 'in_progress', 'completed', 'cancelled')
    ),
    notes TEXT,
    provider_id INTEGER REFERENCES employee(employee_id), -- Кто оказал услугу
    completed_at TIMESTAMP WITH TIME ZONE,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    UNIQUE(booking_id, service_id, scheduled_date)      -- Чтобы не дублировались
);
CREATE TABLE site_setting (
    setting_id SERIAL PRIMARY KEY,
    setting_key VARCHAR(100) UNIQUE NOT NULL,           -- Ключ настройки
    setting_value TEXT,                                 -- Значение настройки
    setting_type VARCHAR(50) DEFAULT 'string' CHECK (   -- Тип значения
        setting_type IN ('string', 'integer', 'boolean', 'json', 'text')
    ),
    category VARCHAR(50) DEFAULT 'general',             -- Категория: general, booking, payment, etc.
    description TEXT,                                   -- Описание настройки
    is_public BOOLEAN DEFAULT FALSE,                   -- Публичная ли настройка (для API)
    min_value VARCHAR(100),                             -- Минимальное значение (для валидации)
    max_value VARCHAR(100),                             -- Максимальное значение
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_by INTEGER REFERENCES users(user_id)
);
CREATE TABLE promo_code (
    promo_id SERIAL PRIMARY KEY,
    code VARCHAR(50) UNIQUE NOT NULL,                   -- Код промокода (например: SUMMER2024)
    description TEXT,                                   -- Описание промокода
    discount_type VARCHAR(20) NOT NULL CHECK (          -- Тип скидки
        discount_type IN ('percentage', 'fixed', 'nights')
    ),
    discount_value DECIMAL(10,2) NOT NULL,              -- Значение скидки
    min_booking_amount DECIMAL(10,2) DEFAULT 0,         -- Минимальная сумма бронирования
    max_discount_amount DECIMAL(10,2),                  -- Максимальная сумма скидки
    valid_from DATE NOT NULL,                           -- Действует с
    valid_to DATE NOT NULL,                             -- Действует до
    usage_limit INTEGER,                                -- Лимит использований (NULL = безлимит)
    used_count INTEGER DEFAULT 0,                       -- Сколько раз использован
    per_user_limit INTEGER DEFAULT 1,                   -- Лимит использований на пользователя
    is_active BOOLEAN DEFAULT TRUE,
    
    -- Ограничения
    only_for_properties INTEGER[],                      -- Только для определенных объектов
    only_for_plans INTEGER[],                           -- Только для определенных тарифов
    only_for_users INTEGER[],                           -- Только для определенных пользователей
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_by INTEGER REFERENCES users(user_id)
);

-- История использования промокодов
CREATE TABLE promo_code_usage (
    usage_id SERIAL PRIMARY KEY,
    promo_id INTEGER NOT NULL REFERENCES promo_code(promo_id),
    booking_id INTEGER NOT NULL REFERENCES booking(booking_id),
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    discount_applied DECIMAL(10,2) NOT NULL,            -- Примененная скидка
    booking_amount DECIMAL(12,2) NOT NULL,              -- Сумма бронирования до скидки
    used_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE inventory_category (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,                -- Категория: техника, мебель, текстиль
    description TEXT
);

CREATE TABLE inventory_item (
    item_id SERIAL PRIMARY KEY,
    property_id INTEGER NOT NULL REFERENCES property(property_id) ON DELETE CASCADE,
    category_id INTEGER REFERENCES inventory_category(category_id),
    item_name VARCHAR(200) NOT NULL,                    -- Название предмета: Холодильник Samsung
    description TEXT,
    serial_number VARCHAR(100),                         -- Серийный номер
    purchase_date DATE,                                 -- Дата покупки
    purchase_price DECIMAL(10,2),                       -- Цена покупки
    current_value DECIMAL(10,2),                        -- Текущая стоимость
    status VARCHAR(20) DEFAULT 'good' CHECK (           -- Состояние
        status IN ('good', 'needs_repair', 'broken', 'lost')
    ),
    location_in_property VARCHAR(100),                  -- Где находится в объекте
    
    -- Для отслеживания
    last_check_date DATE,                               -- Дата последней проверки
    next_check_date DATE,                               -- Дата следующей проверки
    notes TEXT,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Проверки инвентаря при заезде/выезде
CREATE TABLE inventory_check (
    check_id SERIAL PRIMARY KEY,
    booking_id INTEGER NOT NULL REFERENCES booking(booking_id),
    check_type VARCHAR(20) NOT NULL CHECK (             -- Тип проверки
        check_type IN ('check_in', 'check_out', 'periodic')
    ),
    checked_by INTEGER REFERENCES employee(employee_id), -- Кто проверил
    check_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    photos JSONB DEFAULT '[]',                          -- Фотографии при проверке
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Состояние каждого предмета при проверке
CREATE TABLE inventory_check_item (
    check_item_id SERIAL PRIMARY KEY,
    check_id INTEGER NOT NULL REFERENCES inventory_check(check_id) ON DELETE CASCADE,
    item_id INTEGER NOT NULL REFERENCES inventory_item(item_id) ON DELETE CASCADE,
    condition VARCHAR(20) NOT NULL CHECK (               -- Состояние при проверке
        condition IN ('present_ok', 'present_damaged', 'missing', 'replaced')
    ),
    damage_description TEXT,                             -- Описание повреждений
    estimated_repair_cost DECIMAL(8,2),                  -- Ориентировочная стоимость ремонта
    photo_url TEXT,                                      -- Фото повреждения
    action_taken TEXT,                                   -- Какие меры приняты
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
Особенности реализации:

    Использование SERIAL для автоинкремента

    Триггеры для автоматического обновления updated_at

    Генерация уникальных номеров бронирований

    Проверочные ограничения для статусов
    5.2. Создание запросов.
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
    5.3. Разработка интерфейса.
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
Основные возможности интерфейса:

    Аутентификация и авторизация

    Просмотр и управление таблицами БД

    Выполнение SQL-запросов (для администраторов)

    Панель статистики

    Адаптивный дизайн для мобильных устройств

    Ролевой доступ (гость, сотрудник, администратор)
    5.4. Назначение прав доступа.
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
    5.5. Создание индексов.
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

Автоматизация через cron:
text

# Ежедневно в 2:00
0 2 * * * /backup/scripts/backup_daily.sh

# По воскресеньям в 3:00
0 3 * * 0 /backup/scripts/backup_weekly.sh

# Ежемесячно 1-го числа в 4:00
0 4 1 * * /backup/scripts/backup_monthly.sh

Заключение

В ходе курсовой работы была разработана полноценная информационная система управления арендой квартир, включающая:

    Проектирование БД - создана нормализованная структура из 27 таблиц

    Реализация на PostgreSQL - использованы современные возможности СУБД (JSONB, триггеры, индексы)

    Веб-интерфейс - разработан интуитивно понятный интерфейс на PHP/HTML/CSS

    Система безопасности - реализована многоуровневая аутентификация и авторизация

    Оптимизация - созданы индексы для критически важных запросов

    Стратегия резервного копирования - разработан план сохранности данных

Система готова к использованию в реальных условиях работы агентства аренды недвижимости и может быть
масштабирована для поддержки тысяч объектов и десятков тысяч пользователей.

Руководитель работы И. В. Пунгин

Задание принял к исполнению Кочанов А.М.
