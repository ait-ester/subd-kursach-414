Моя тема БД агентства по аренде квартир. За сегоднешние пары я создал титульный лист, прочитал основные положения и госты, дальше нахожусь в руздумье с чего начать курсовую.
Сегодня я разрабатывал саму базу данных которая вклюяаетв себя аренду квартир на посуточно и долгосрочно, так же с вызовом клининга на посуточную после каждого съезда человека и по желанию долгосрочным жителям.
Сегодня я снес по полной свою базу данных и сделал новую на 27 таблиц, так же сделал отдельный сайт, следующие пары буду проверять на нормальную работоспособность и делать в письменном виде уже.
Моя база данных выглядит так. 
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

-- Индексы для быстрого поиска
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role ON users(role);
CREATE INDEX idx_users_last_login ON users(last_login);

-- Триггер для обновления updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_users_updated_at BEFORE UPDATE
    ON users FOR EACH ROW EXECUTE FUNCTION 
    update_updated_at_column();
    
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

-- Заполняем примеры сотрудников (5 записей)
INSERT INTO users (email, password_hash, role, phone) VALUES
('admin@rental-agency.ru', '$2a$12$Hq3p5Q5bQ3p5Q5bQ3p5Q5u', 'admin', '+79161234567'),  -- Администратор
('manager@rental-agency.ru', '$2a$12$Hq3p5Q5bQ3p5Q5bQ3p5Q5u', 'employee', '+79161234568'),  -- Менеджер
('realtor1@rental-agency.ru', '$2a$12$Hq3p5Q5bQ3p5Q5bQ3p5Q5u', 'employee', '+79161234569'),  -- Риелтор
('cleaner1@rental-agency.ru', '$2a$12$Hq3p5Q5bQ3p5Q5bQ3p5Q5u', 'cleaner', '+79161234570'),  -- Уборщик
('support@rental-agency.ru', '$2a$12$Hq3p5Q5bQ3p5Q5bQ3p5Q5u', 'employee', '+79161234571'); -- Поддержка

INSERT INTO employee (user_id, first_name, last_name, position, hire_date, salary, department) VALUES
(1, 'Александр', 'Иванов', 'Генеральный директор', '2020-01-15', 150000, 'management'),
(2, 'Екатерина', 'Петрова', 'Менеджер по аренде', '2021-03-10', 90000, 'sales'),
(3, 'Дмитрий', 'Сидоров', 'Старший риелтор', '2021-06-22', 120000, 'sales'),
(4, 'Ольга', 'Кузнецова', 'Клининг-менеджер', '2022-01-30', 65000, 'cleaning'),
(5, 'Мария', 'Смирнова', 'Специалист поддержки', '2022-05-15', 70000, 'support');

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

-- Триггер для обновления updated_at
CREATE TRIGGER update_guest_updated_at BEFORE UPDATE
    ON guest FOR EACH ROW EXECUTE FUNCTION 
    update_updated_at_column();

-- Заполняем примеры гостей
INSERT INTO users (email, password_hash, role, phone) VALUES
('guest1@gmail.com', '$2a$12$Hq3p5Q5bQ3p5Q5bQ3p5Q5u', 'guest', '+79161111111'),
('guest2@gmail.com', '$2a$12$Hq3p5Q5bQ3p5Q5bQ3p5Q5u', 'guest', '+79162222222'),
('guest3@gmail.com', '$2a$12$Hq3p5Q5bQ3p5Q5bQ3p5Q5u', 'guest', '+79163333333'),
('guest4@gmail.com', '$2a$12$Hq3p5Q5bQ3p5Q5bQ3p5Q5u', 'guest', '+79164444444'),
('guest5@gmail.com', '$2a$12$Hq3p5Q5bQ3p5Q5bQ3p5Q5u', 'guest', '+79165555555');

INSERT INTO guest (user_id, first_name, last_name, email, phone, passport_number, date_of_birth, verified, rating) VALUES
(6, 'Иван', 'Козлов', 'guest1@gmail.com', '+79161111111', '4510 123456', '1985-03-15', TRUE, 4.8),
(7, 'Анна', 'Новикова', 'guest2@gmail.com', '+79162222222', '4510 234567', '1990-07-22', TRUE, 4.9),
(8, 'Сергей', 'Морозов', 'guest3@gmail.com', '+79163333333', '4510 345678', '1988-11-30', FALSE, 3.5),
(9, 'Елена', 'Волкова', 'guest4@gmail.com', '+79164444444', '4510 456789', '1995-05-18', TRUE, 4.2),
(10, 'Павел', 'Захаров', 'guest5@gmail.com', '+79165555555', '4510 567890', '1992-09-10', TRUE, 5.0);

-- Типы объектов для фильтрации на сайте
CREATE TABLE property_type (
    type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE,    -- Название типа
    icon_class VARCHAR(100),                   -- Класс иконки для сайта
    description TEXT                           -- Описание типа
);

-- Категории объектов (для поиска и фильтрации)
CREATE TABLE property_category (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL UNIQUE, -- Название категории
    slug VARCHAR(50) UNIQUE NOT NULL,         -- ЧПУ для URL
    sort_order INTEGER DEFAULT 0              -- Порядок отображения
);

-- Основная таблица объектов недвижимости
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

-- Триггер для updated_at
CREATE TRIGGER update_property_updated_at BEFORE UPDATE
    ON property FOR EACH ROW EXECUTE FUNCTION 
    update_updated_at_column();

-- Фотографии объектов (для галереи на сайте)
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

-- Заполняем типы и категории
INSERT INTO property_type (type_name, icon_class, description) VALUES
('Квартира', 'apartment', 'Полная квартира со всеми удобствами'),
('Апартаменты', 'apartments', 'Апартаменты с услугами отеля'),
('Студия', 'studio', 'Компактная студия для 1-2 гостей'),
('Лофт', 'loft', 'Стильный лофт в бывшем промышленном здании'),
('Пентхаус', 'penthouse', 'Люкс на последнем этаже с видом');

INSERT INTO property_category (category_name, slug, sort_order) VALUES
('Посуточная аренда', 'daily', 1),
('Долгосрочная аренда', 'long-term', 2),
('Премиум', 'premium', 3),
('Эконом', 'budget', 4),
('Для бизнеса', 'business', 5);

-- Заполняем объекты недвижимости
INSERT INTO property (owner_name, property_type_id, category_id, title, slug, address, city, district, metro_station, latitude, longitude, floor, floors_in_building, area_sq_m, rooms, max_guests, beds, description, short_description, is_active, featured) VALUES
('ООО "РентХаус"', 1, 1, 'Уютная квартира в центре Москвы', 'uyutnaya-kvartira-v-tsentre-moskvy', 'ул. Тверская, д. 15, кв. 42', 'Москва', 'Центральный', 'Тверская', 55.761590, 37.609466, 5, 9, 45.5, 2, 4, 2, 'Прекрасная двухкомнатная квартира в самом центре Москвы. Ремонт 2023 года. Все необходимое для комфортного проживания.', 'Уютная двушка у метро', TRUE, TRUE),

('ИП Сидоров А.А.', 2, 3, 'Апартаменты с видом на Кремль', 'apartments-with-kremlin-view', 'ул. Большая Дмитровка, д. 10', 'Москва', 'Центральный', 'Охотный ряд', 55.757973, 37.617664, 12, 15, 65.0, 3, 6, 3, 'Роскошные апартаменты с панорамным видом на Кремль. Полностью оборудованная кухня, джакузи, консьерж.', 'Люкс с видом на Кремль', TRUE, TRUE),

('ООО "Комфорт+"', 3, 4, 'Студия у метро в спальном районе', 'studiya-u-metro', 'ул. Профсоюзная, д. 25, кв. 17', 'Москва', 'ЮЗАО', 'Калужская', 55.657566, 37.541302, 3, 12, 32.0, 1, 2, 1, 'Компактная студия для бюджетного проживания. Идеально для командировок или временного проживания.', 'Эконом-вариант у метро', TRUE, FALSE),

('АО "ЭлитНедвижимость"', 5, 3, 'Пентхаус на Патриарших', 'penthouse-on-patriarch', 'Патриарший пер., д. 8', 'Москва', 'ЦАО', 'Маяковская', 55.769137, 37.595069, 14, 14, 120.0, 4, 8, 4, 'Эксклюзивный пентхаус с террасой и панорамным видом. Два санузла, камин, система "умный дом".', 'Элитный пентхаус в центре', TRUE, TRUE),

('Смирнова Е.В.', 4, 2, 'Лофт в бывшем заводе', 'loft-in-factory', 'ул. Береговая, д. 14', 'Москва', 'ВАО', 'Электрозаводская', 55.782369, 37.703415, 2, 4, 85.0, 2, 6, 3, 'Стильный лофт в отреставрированном здании фабрики. Высокие потолки, кирпичные стены, современный дизайн.', 'Стильный лофт для творческих людей', TRUE, FALSE);

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

-- Заполняем тарифы
INSERT INTO rental_plan (plan_name, rental_type, min_nights, max_nights, base_price_per_night, monthly_discount_percent, features) VALUES
('Стандарт', 'daily', 1, 30, 3500.00, 0, '["Wi-Fi", "TV", "Кухня"]'),
('Премиум', 'daily', 2, 60, 6500.00, 0, '["Кондиционер", "Парковка", "Джакузи"]'),
('Долгосрочная (месяц)', 'monthly', 30, 365, 0, 20.00, '["Уборка раз в неделю", "Замена постельного белья"]'),
('Бизнес', 'daily', 1, 90, 4500.00, 15.00, '["Рабочее место", "Принтер", "Кофемашина"]'),
('Эконом', 'daily', 3, 14, 2000.00, 0, '["Базовые удобства"]');

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

-- Триггер для генерации номера брони
CREATE OR REPLACE FUNCTION generate_booking_number()
RETURNS TRIGGER AS $$
BEGIN
    NEW.booking_number := 'BKG-' || 
                         EXTRACT(YEAR FROM CURRENT_DATE) || '-' || 
                         LPAD(NEXTVAL('booking_number_seq')::TEXT, 6, '0');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE SEQUENCE booking_number_seq START 100001;
CREATE TRIGGER set_booking_number BEFORE INSERT ON booking
FOR EACH ROW EXECUTE FUNCTION generate_booking_number();

-- Триггер для updated_at
CREATE TRIGGER update_booking_updated_at BEFORE UPDATE ON booking
FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Заполняем примеры бронирований
INSERT INTO booking (property_id, guest_id, plan_id, employee_id, status, check_in_date, check_out_date, nights, adults, children, base_price, cleaning_fee, total_price, paid_amount) VALUES
(1, 1, 1, 3, 'completed', '2024-01-15', '2024-01-20', 5, 2, 0, 17500.00, 1000.00, 18500.00, 18500.00),
(2, 2, 2, 3, 'active', '2024-03-01', '2024-03-10', 9, 4, 2, 58500.00, 1500.00, 60000.00, 60000.00),
(3, 3, 5, 2, 'confirmed', '2024-04-01', '2024-04-05', 4, 1, 0, 8000.00, 800.00, 8800.00, 8800.00),
(4, 4, 3, 2, 'pending', '2024-05-01', '2024-06-01', 31, 2, 0, 0, 2000.00, 155000.00, 0),
(5, 5, 4, 3, 'cancelled', '2024-02-01', '2024-02-07', 6, 3, 0, 27000.00, 1200.00, 28200.00, 0);

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

-- Заполняем задачи на уборку
INSERT INTO cleaning_task (booking_id, property_id, cleaner_id, task_type, scheduled_date, scheduled_time, estimated_duration, status, cleaning_cost) VALUES
(1, 1, 4, 'checkout', '2024-01-20', '12:30', 120, 'completed', 1200.00),
(2, 2, 4, 'checkout', '2024-03-10', '11:00', 180, 'scheduled', 1500.00),
(3, 3, NULL, 'checkout', '2024-04-05', '13:00', 90, 'scheduled', 800.00),
(4, 4, NULL, 'deep', '2024-04-25', '10:00', 240, 'scheduled', 2500.00),
(5, 5, 4, 'checkout', '2024-02-07', '14:00', 120, 'cancelled', 1200.00);

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

-- Заполняем отзывы
INSERT INTO review (booking_id, guest_id, property_id, cleanliness_rating, location_rating, value_rating, service_rating, overall_rating, title, comment, is_approved, would_recommend) VALUES
(1, 1, 1, 5, 5, 4, 5, 4.8, 'Отличная квартира!', 'Все понравилось, чисто, уютно, хорошее расположение.', TRUE, TRUE),
(2, 2, 2, 5, 5, 5, 5, 5.0, 'Прекрасные апартаменты!', 'Вид потрясающий, все продумано до мелочей. Обязательно вернемся!', TRUE, TRUE);

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

-- Заполняем черный список
INSERT INTO blacklist (guest_id, banned_phone, reason, risk_level, added_by_employee_id, is_active) VALUES
(3, '+79163333333', 'Нарушение правил дома, шумные вечеринки', 'medium', 2, TRUE),
(NULL, '+79167777777', 'Порча имущества в другом объекте', 'high', 1, TRUE);

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

-- Критически важные индексы для быстрой работы сайта
CREATE INDEX idx_property_city ON property(city);
CREATE INDEX idx_property_dates ON property(is_active, featured);
CREATE INDEX idx_booking_dates ON booking(check_in_date, check_out_date, status);
CREATE INDEX idx_booking_guest ON booking(guest_id, status);
CREATE INDEX idx_price_calendar_search ON price_calendar(property_id, date);
CREATE INDEX idx_review_property ON review(property_id, is_approved);
CREATE INDEX idx_blacklist_search ON blacklist(banned_phone, banned_passport, is_active);
CREATE INDEX idx_users_token ON user_sessions(token, expires_at);

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

-- Индексы для оптимизации
CREATE INDEX idx_payment_booking ON payment(booking_id);
CREATE INDEX idx_payment_user ON payment(user_id);
CREATE INDEX idx_payment_status ON payment(payment_status);
CREATE INDEX idx_payment_created ON payment(created_at);
CREATE INDEX idx_payment_transaction ON payment(transaction_id);

-- Триггер для updated_at
CREATE TRIGGER update_payment_updated_at BEFORE UPDATE ON payment
FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

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

-- Индексы
CREATE INDEX idx_notification_user ON notification(user_id, is_read);
CREATE INDEX idx_notification_created ON notification(created_at DESC);
CREATE INDEX idx_notification_type ON notification(notification_type);
CREATE INDEX idx_notification_scheduled ON notification(scheduled_for) 
WHERE scheduled_for IS NOT NULL;

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

-- Индексы для чата
CREATE INDEX idx_message_thread ON message(thread_id, created_at DESC);
CREATE INDEX idx_message_sender ON message(sender_id, created_at DESC);
CREATE INDEX idx_message_receiver ON message(receiver_id, is_read, created_at DESC);
CREATE INDEX idx_message_booking ON message(booking_id);

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

-- Индексы
CREATE INDEX idx_booking_service_booking ON booking_service(booking_id);
CREATE INDEX idx_booking_service_status ON booking_service(status);
CREATE INDEX idx_service_type ON service(service_type, is_available);

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

-- Наполняем базовые настройки
INSERT INTO site_setting (setting_key, setting_value, setting_type, category, description) VALUES
('site_name', 'Агентство аренды квартир "Комфорт"', 'string', 'general', 'Название сайта'),
('site_email', 'info@comfort-rental.ru', 'string', 'general', 'Основной email сайта'),
('site_phone', '+7 (495) 123-45-67', 'string', 'general', 'Основной телефон'),
('booking_min_nights', '1', 'integer', 'booking', 'Минимальное количество ночей'),
('booking_max_nights', '90', 'integer', 'booking', 'Максимальное количество ночей'),
('cancellation_free_hours', '48', 'integer', 'booking', 'Часов до заезда для бесплатной отмены'),
('deposit_percent', '20', 'integer', 'payment', 'Процент депозита от стоимости'),
('check_in_time', '14:00', 'string', 'booking', 'Стандартное время заезда'),
('check_out_time', '12:00', 'string', 'booking', 'Стандартное время выезда'),
('currency', 'RUB', 'string', 'payment', 'Основная валюта'),
('tax_percent', '0', 'integer', 'payment', 'Процент налога'),
('enable_reviews', 'true', 'boolean', 'general', 'Включить систему отзывов'),
('enable_online_payment', 'true', 'boolean', 'payment', 'Включить онлайн-оплату'),
('maintenance_mode', 'false', 'boolean', 'general', 'Режим технического обслуживания');

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

-- Индексы
CREATE INDEX idx_promo_code_valid ON promo_code(code, is_active, valid_from, valid_to);
CREATE INDEX idx_promo_code_usage ON promo_code_usage(promo_id, user_id);
CREATE INDEX idx_promo_code_booking ON promo_code_usage(booking_id);

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

-- Индексы
CREATE INDEX idx_inventory_property ON inventory_item(property_id, status);
CREATE INDEX idx_inventory_check_booking ON inventory_check(booking_id, check_type);
CREATE INDEX idx_inventory_check_item ON inventory_check_item(check_id, item_id);









Добавление данных в таблицы 
-- 1. Таблица пользователей (users) - уже есть 10 записей (5 сотрудников + 5 гостей)
-- Добавим еще 5 разных пользователей
INSERT INTO users (email, password_hash, role, phone, avatar_url) VALUES
('owner1@example.com', '$2a$12$Hq3p5Q5bQ3p5Q5bQ3p5Q5u', 'guest', '+79166666666', 'https://example.com/avatars/1.jpg'),
('owner2@example.com', '$2a$12$Hq3p5Q5bQ3p5Q5bQ3p5Q5u', 'guest', '+79167777777', 'https://example.com/avatars/2.jpg'),
('realtor2@agency.ru', '$2a$12$Hq3p5Q5bQ3p5Q5bQ3p5Q5u', 'employee', '+79168888888', 'https://example.com/avatars/3.jpg'),
('cleaner2@agency.ru', '$2a$12$Hq3p5Q5bQ3p5Q5bQ3p5Q5u', 'cleaner', '+79169999999', 'https://example.com/avatars/4.jpg'),
('guest6@gmail.com', '$2a$12$Hq3p5Q5bQ3p5Q5bQ3p5Q5u', 'guest', '+79160000000', 'https://example.com/avatars/5.jpg');

-- 2. Таблица сотрудников (employee) - уже есть 5 записей, добавим еще 5
INSERT INTO employee (user_id, first_name, last_name, position, hire_date, salary, department) VALUES
(11, 'Андрей', 'Федоров', 'Риелтор', '2022-08-15', 85000, 'sales'),
(12, 'Татьяна', 'Михайлова', 'Бухгалтер', '2020-11-10', 95000, 'finance'),
(13, 'Игорь', 'Николаев', 'Старший клинер', '2022-02-20', 75000, 'cleaning'),
(14, 'Светлана', 'Васильева', 'Менеджер поддержки', '2023-01-15', 65000, 'support'),
(15, 'Алексей', 'Павлов', 'Технический специалист', '2021-09-05', 80000, 'maintenance');

-- 3. Таблица гостей (guest) - уже есть 5 записей, добавим еще 5
INSERT INTO guest (user_id, first_name, last_name, email, phone, passport_number, date_of_birth, verified, rating, total_bookings) VALUES
(16, 'Максим', 'Григорьев', 'owner1@example.com', '+79166666666', '4510 678901', '1980-12-05', TRUE, 4.7, 3),
(17, 'Наталья', 'Семенова', 'owner2@example.com', '+79167777777', '4510 789012', '1975-04-22', TRUE, 4.9, 7),
(18, 'Артем', 'Лебедев', 'guest6@gmail.com', '+79160000000', '4510 890123', '1993-08-30', FALSE, 0, 0),
(19, 'Виктория', 'Козлова', 'guest7@mail.ru', '+79161111112', '4510 901234', '1991-03-14', TRUE, 4.5, 2),
(20, 'Роман', 'Соловьев', 'guest8@yandex.ru', '+79162222223', '4510 012345', '1987-11-08', TRUE, 4.8, 5);

-- 4. Типы объектов (property_type) - уже есть 5 записей
-- 5. Категории объектов (property_category) - уже есть 5 записей
-- 6. Объекты недвижимости (property) - уже есть 5 записей, добавим еще 5
INSERT INTO property (owner_name, property_type_id, category_id, title, slug, address, city, district, metro_station, floor, floors_in_building, area_sq_m, rooms, max_guests, beds, description, short_description, is_active, featured, managed_by_employee_id) VALUES
('ИП Петров П.П.', 1, 1, 'Квартира на Арбате', 'kvartira-na-arbate', 'ул. Арбат, д. 25, кв. 10', 'Москва', 'ЦАО', 'Арбатская', 4, 7, 55.0, 2, 4, 2, 'Просторная двухкомнатная квартира на старом Арбате. Исторический район.', 'Квартира в историческом центре', TRUE, FALSE, 3),

('ООО "СтоличнаяНедвижимость"', 2, 3, 'Апартаменты в Сити', 'apartamenti-v-siti', 'Пресненская наб., д. 12', 'Москва', 'ЦАО', 'Деловой центр', 15, 25, 75.0, 3, 6, 3, 'Современные апартаменты с видом на Москва-Сити. Для бизнес-поездок.', 'Апартаменты в деловом центре', TRUE, TRUE, 3),

('Семенов С.С.', 3, 4, 'Студия у парка', 'studiya-u-parka', 'ул. Крылатская, д. 15, кв. 32', 'Москва', 'ЗАО', 'Крылатское', 2, 9, 28.0, 1, 2, 1, 'Уютная студия рядом с парком. Тихий район, хорошая экология.', 'Бюджетный вариант у парка', TRUE, FALSE, 2),

('ООО "ЭлитСтрой"', 5, 3, 'Пентхаус на Рублевке', 'penthouse-na-rublevke', 'Рублево-Успенское ш., д. 45', 'Москва', 'ЗАО', 'Крылатское', 3, 3, 200.0, 5, 10, 6, 'Элитный пентхаус в закрытом поселке. Собственный бассейн, сауна, охраняемая территория.', 'Элитная недвижимость на Рублевке', TRUE, TRUE, 1),

('Иванова М.И.', 4, 2, 'Лофт в центре', 'loft-v-tsentre', 'ул. Пятницкая, д. 18', 'Москва', 'ЦАО', 'Новокузнецкая', 2, 4, 95.0, 2, 6, 3, 'Стильный лофт в отреставрированном здании 19 века. Сохранены исторические элементы.', 'Исторический лофт в центре', TRUE, FALSE, 3);

-- 7. Фотографии объектов (property_photo) - добавим по 2 фото на каждый объект
INSERT INTO property_photo (property_id, photo_url, photo_thumb_url, caption, sort_order, is_main) VALUES
-- Для property_id 1 (первая квартира)
(1, 'https://example.com/photos/prop1_1.jpg', 'https://example.com/thumbs/prop1_1_t.jpg', 'Гостиная', 1, TRUE),
(1, 'https://example.com/photos/prop1_2.jpg', 'https://example.com/thumbs/prop1_2_t.jpg', 'Кухня', 2, FALSE),

-- Для property_id 2
(2, 'https://example.com/photos/prop2_1.jpg', 'https://example.com/thumbs/prop2_1_t.jpg', 'Вид из окна', 1, TRUE),
(2, 'https://example.com/photos/prop2_2.jpg', 'https://example.com/thumbs/prop2_2_t.jpg', 'Спальня', 2, FALSE),

-- Для property_id 3
(3, 'https://example.com/photos/prop3_1.jpg', 'https://example.com/thumbs/prop3_1_t.jpg', 'Общий вид', 1, TRUE),
(3, 'https://example.com/photos/prop3_2.jpg', 'https://example.com/thumbs/prop3_2_t.jpg', 'Ванная комната', 2, FALSE),

-- Для property_id 4
(4, 'https://example.com/photos/prop4_1.jpg', 'https://example.com/thumbs/prop4_1_t.jpg', 'Терраса', 1, TRUE),
(4, 'https://example.com/photos/prop4_2.jpg', 'https://example.com/thumbs/prop4_2_t.jpg', 'Бассейн', 2, FALSE),

-- Для property_id 5
(5, 'https://example.com/photos/prop5_1.jpg', 'https://example.com/thumbs/prop5_1_t.jpg', 'Интерьер', 1, TRUE),
(5, 'https://example.com/photos/prop5_2.jpg', 'https://example.com/thumbs/prop5_2_t.jpg', 'Кухня-гостиная', 2, FALSE);

-- 8. Тарифы (rental_plan) - уже есть 5 записей
-- 9. Календарь цен (price_calendar) - заполним на ближайший месяц
INSERT INTO price_calendar (property_id, date, price_per_night) VALUES
-- Для объекта 1 на ближайшие 5 дней
(1, CURRENT_DATE + 1, 4000.00),
(1, CURRENT_DATE + 2, 4000.00),
(1, CURRENT_DATE + 3, 4500.00), -- выходные дороже
(1, CURRENT_DATE + 4, 4500.00),
(1, CURRENT_DATE + 5, 4000.00),

-- Для объекта 2
(2, CURRENT_DATE + 1, 7000.00),
(2, CURRENT_DATE + 2, 7000.00),
(2, CURRENT_DATE + 3, 8000.00),
(2, CURRENT_DATE + 4, 8000.00),
(2, CURRENT_DATE + 5, 7000.00),

-- Для объекта 3
(3, CURRENT_DATE + 1, 2500.00),
(3, CURRENT_DATE + 2, 2500.00),
(3, CURRENT_DATE + 3, 3000.00),
(3, CURRENT_DATE + 4, 3000.00),
(3, CURRENT_DATE + 5, 2500.00),

-- Для объекта 4
(4, CURRENT_DATE + 1, 15000.00),
(4, CURRENT_DATE + 2, 15000.00),
(4, CURRENT_DATE + 3, 18000.00),
(4, CURRENT_DATE + 4, 18000.00),
(4, CURRENT_DATE + 5, 15000.00),

-- Для объекта 5
(5, CURRENT_DATE + 1, 6000.00),
(5, CURRENT_DATE + 2, 6000.00),
(5, CURRENT_DATE + 3, 7000.00),
(5, CURRENT_DATE + 4, 7000.00),
(5, CURRENT_DATE + 5, 6000.00);

-- 10. Бронирования (booking) - уже есть 5 записей, добавим еще 5
INSERT INTO booking (property_id, guest_id, plan_id, employee_id, status, check_in_date, check_out_date, nights, adults, children, base_price, cleaning_fee, total_price, paid_amount, contact_phone) VALUES
(6, 6, 1, 3, 'completed', '2024-02-10', '2024-02-15', 5, 2, 1, 20000.00, 1000.00, 21000.00, 21000.00, '+79161111111'),
(7, 7, 2, 3, 'active', CURRENT_DATE - 2, CURRENT_DATE + 5, 7, 3, 0, 56000.00, 1500.00, 57500.00, 57500.00, '+79162222222'),
(8, 8, 5, 2, 'confirmed', CURRENT_DATE + 7, CURRENT_DATE + 12, 5, 1, 0, 12500.00, 800.00, 13300.00, 13300.00, '+79163333333'),
(9, 9, 3, 2, 'pending', CURRENT_DATE + 15, CURRENT_DATE + 45, 30, 2, 1, 0, 2000.00, 180000.00, 50000.00, '+79164444444'),
(10, 10, 4, 3, 'cancelled', '2024-03-01', '2024-03-07', 6, 4, 0, 30000.00, 1200.00, 31200.00, 0, '+79165555555');

-- 11. Задачи на уборку (cleaning_task) - уже есть 5 записей, добавим еще 5
INSERT INTO cleaning_task (booking_id, property_id, cleaner_id, task_type, scheduled_date, scheduled_time, estimated_duration, status, cleaning_cost, extra_charges) VALUES
(6, 6, 13, 'checkout', '2024-02-15', '12:00', 120, 'completed', 1200.00, 0),
(7, 7, 8, 'checkout', CURRENT_DATE + 5, '11:00', 150, 'scheduled', 1500.00, 0),
(8, 8, NULL, 'checkout', CURRENT_DATE + 12, '13:00', 90, 'scheduled', 900.00, 0),
(9, 9, NULL, 'weekly', CURRENT_DATE + 22, '10:00', 180, 'scheduled', 1800.00, 500.00),
(10, 10, 8, 'checkout', '2024-03-07', '14:00', 120, 'cancelled', 1200.00, 0);

-- 12. Отзывы (review) - уже есть 2 записи, добавим еще 3
INSERT INTO review (booking_id, guest_id, property_id, cleanliness_rating, location_rating, value_rating, service_rating, overall_rating, title, comment, is_approved, would_recommend) VALUES
(6, 6, 6, 4, 5, 5, 4, 4.5, 'Отличное расположение', 'Квартира в самом центре, все достопримечательности рядом. Чисто, уютно.', TRUE, TRUE),
(7, 7, 7, 5, 5, 4, 5, 4.8, 'Идеально для бизнес-поездки', 'Все на высшем уровне. Быстрый интернет, удобное рабочее место.', TRUE, TRUE),
(8, 8, 8, 3, 4, 5, 3, 3.8, 'Неплохо за свои деньги', 'Студия маленькая, но для одного человека достаточно. Район тихий.', FALSE, TRUE);

-- 13. Черный список (blacklist) - уже есть 2 записи, добавим еще 3
INSERT INTO blacklist (guest_id, banned_phone, banned_email, reason, risk_level, added_by_employee_id, is_active, expires_at) VALUES
(9, '+79164444444', NULL, 'Неоднократные задержки оплаты', 'low', 2, TRUE, CURRENT_DATE + 365),
(NULL, '+79168888888', 'problem@mail.ru', 'Порча имущества', 'high', 1, TRUE, CURRENT_DATE + 730),
(10, '+79165555555', 'badguest@mail.ru', 'Нарушение правил дома', 'medium', 3, FALSE, CURRENT_DATE + 180); -- Неактивная запись

-- 14. Сессии пользователей (user_sessions) - 5 записей
INSERT INTO user_sessions (session_id, user_id, token, ip_address, user_agent, expires_at) VALUES
('sess_001', 1, 'token_abc123', '192.168.1.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', CURRENT_TIMESTAMP + INTERVAL '7 days'),
('sess_002', 2, 'token_def456', '192.168.1.2', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36', CURRENT_TIMESTAMP + INTERVAL '7 days'),
('sess_003', 6, 'token_ghi789', '192.168.1.3', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/537.36', CURRENT_TIMESTAMP + INTERVAL '3 days'),
('sess_004', 7, 'token_jkl012', '192.168.1.4', 'Mozilla/5.0 (Android 11; Mobile) AppleWebKit/537.36', CURRENT_TIMESTAMP + INTERVAL '1 day'),
('sess_005', 3, 'token_mno345', '192.168.1.5', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124', CURRENT_TIMESTAMP + INTERVAL '5 days');

-- 15. Логи аудита (audit_log) - 5 записей
INSERT INTO audit_log (user_id, action, entity_type, entity_id, old_values, new_values, ip_address, user_agent) VALUES
(1, 'login', 'user', 1, NULL, '{"last_login": "2024-01-01"}', '192.168.1.1', 'Mozilla/5.0'),
(2, 'booking_create', 'booking', 1, NULL, '{"status": "pending", "total_price": 18500}', '192.168.1.2', 'Mozilla/5.0'),
(3, 'property_update', 'property', 1, '{"price": 3500}', '{"price": 4000}', '192.168.1.3', 'Mozilla/5.0'),
(4, 'cleaning_complete', 'cleaning_task', 1, '{"status": "in_progress"}', '{"status": "completed"}', '192.168.1.4', 'Mozilla/5.0'),
(5, 'payment_received', 'payment', 1, '{"status": "pending"}', '{"status": "completed"}', '192.168.1.5', 'Mozilla/5.0');

-- 16. Платежи (payment) - 5 записей
INSERT INTO payment (booking_id, user_id, amount, payment_method, payment_gateway, transaction_id, payment_status, purpose, description) VALUES
(1, 6, 18500.00, 'card', 'yookassa', 'txn_001', 'completed', 'booking', 'Оплата бронирования #BKG-2024-100001'),
(2, 7, 60000.00, 'card', 'tinkoff', 'txn_002', 'completed', 'booking', 'Оплата бронирования #BKG-2024-100002'),
(3, 8, 8800.00, 'cash', NULL, NULL, 'completed', 'booking', 'Оплата наличными в офисе'),
(4, 9, 50000.00, 'transfer', NULL, 'bank_ref_001', 'completed', 'deposit', 'Депозит по бронированию #BKG-2024-100004'),
(5, 10, 10000.00, 'card', 'yookassa', 'txn_003', 'refunded', 'refund', 'Возврат отмененного бронирования');

-- 17. Уведомления (notification) - 5 записей
INSERT INTO notification (user_id, notification_type, title, message, is_read, is_email_sent, priority, related_entity_type, related_entity_id) VALUES
(6, 'booking_confirmed', 'Бронирование подтверждено', 'Ваше бронирование #BKG-2024-100001 подтверждено.', TRUE, TRUE, 'normal', 'booking', 1),
(7, 'payment_received', 'Платеж получен', 'Получен платеж на сумму 60 000 ₽ по бронированию #BKG-2024-100002.', TRUE, TRUE, 'normal', 'payment', 2),
(8, 'checkin_reminder', 'Напоминание о заезде', 'Через 2 дня заезд в квартиру. Не забудьте документы!', FALSE, FALSE, 'normal', 'booking', 3),
(9, 'review_request', 'Оставьте отзыв', 'Пожалуйста, оставьте отзыв о вашем пребывании.', FALSE, TRUE, 'low', 'booking', 4),
(2, 'new_booking', 'Новое бронирование', 'Поступило новое бронирование #BKG-2024-100003.', TRUE, FALSE, 'high', 'booking', 3);

-- 18. Сообщения (message) - 5 записей
INSERT INTO message (thread_id, sender_id, receiver_id, message_text, attachments, is_read, booking_id) VALUES
('user_6_employee_3', 6, 3, 'Здравствуйте! Можно ли заехать пораньше?', '[]', TRUE, 1),
('user_6_employee_3', 3, 6, 'Да, можно с 12:00. Нужен ли трансфер?', '[]', TRUE, 1),
('user_7_employee_3', 7, 3, 'Сломался кондиционер, можно починить?', '[]', FALSE, 2),
('user_8_employee_2', 8, 2, 'Спасибо за отличный сервис!', '[]', TRUE, 3),
('user_2_employee_4', 2, 4, 'Не забудьте про уборку в 401 кв.', '[]', TRUE, NULL);

-- 19. Услуги (service) - 5 записей
INSERT INTO service (service_name, service_type, description, price, duration_minutes, is_available, requires_booking, icon_class) VALUES
('Трансфер из аэропорта', 'transfer', 'Встреча в аэропорту с табличкой', 2500.00, 60, TRUE, TRUE, 'fas fa-car'),
('Завтрак в номер', 'food', 'Континентальный завтрак', 800.00, NULL, TRUE, FALSE, 'fas fa-coffee'),
('Химчистка дивана', 'cleaning', 'Глубокая химчистка мягкой мебели', 3500.00, 120, TRUE, TRUE, 'fas fa-soap'),
('Аренда велосипеда', 'equipment', 'На сутки, шлем в комплекте', 500.00, 1440, TRUE, FALSE, 'fas fa-bicycle'),
('Консьерж-сервис', 'other', 'Помощь с билетами, ресторанами и т.д.', 1000.00, NULL, TRUE, FALSE, 'fas fa-concierge-bell');

-- 20. Заказы услуг (booking_service) - 5 записей
INSERT INTO booking_service (booking_id, service_id, quantity, unit_price, total_price, scheduled_date, scheduled_time, status) VALUES
(1, 1, 1, 2500.00, 2500.00, '2024-01-15', '10:00', 'completed'),
(2, 2, 2, 800.00, 1600.00, '2024-03-02', '08:00', 'completed'),
(3, 4, 1, 500.00, 500.00, '2024-04-02', '09:00', 'pending'),
(4, 5, 1, 1000.00, 1000.00, '2024-05-01', NULL, 'confirmed'),
(5, 3, 1, 3500.00, 3500.00, '2024-02-02', '14:00', 'cancelled');

-- 21. Настройки сайта (site_setting) - уже есть 14 записей
-- 22. Промокоды (promo_code) - 5 записей
INSERT INTO promo_code (code, description, discount_type, discount_value, valid_from, valid_to, usage_limit, is_active) VALUES
('WELCOME2024', 'Скидка для новых клиентов', 'percentage', 10.00, '2024-01-01', '2024-12-31', 100, TRUE),
('SUMMER15', 'Летняя скидка', 'percentage', 15.00, '2024-06-01', '2024-08-31', NULL, TRUE),
('LONGSTAY', 'Для долгосрочной аренды', 'fixed', 5000.00, '2024-01-01', '2024-12-31', 50, TRUE),
('BUSINESS10', 'Для бизнес-клиентов', 'percentage', 10.00, '2024-01-01', '2024-12-31', NULL, TRUE),
('TEST5', 'Тестовый промокод', 'fixed', 1000.00, '2024-01-01', '2024-01-31', 5, FALSE);

-- 23. Использование промокодов (promo_code_usage) - 5 записей
INSERT INTO promo_code_usage (promo_id, booking_id, user_id, discount_applied, booking_amount) VALUES
(1, 1, 6, 1850.00, 18500.00),
(2, 2, 7, 9000.00, 60000.00),
(3, 4, 9, 5000.00, 180000.00),
(1, 3, 8, 1330.00, 13300.00),
(4, 6, 16, 2100.00, 21000.00);

-- 24. Категории инвентаря (inventory_category) - создадим 5 категорий
INSERT INTO inventory_category (category_name, description) VALUES
('Техника', 'Бытовая техника и электроника'),
('Мебель', 'Мебель и предметы интерьера'),
('Текстиль', 'Постельное белье, полотенца, шторы'),
('Кухонная утварь', 'Посуда, столовые приборы, техника для кухни'),
('Сантехника', 'Ванна, душевая кабина, смесители');

-- 25. Предметы инвентаря (inventory_item) - 5 записей для первого объекта
INSERT INTO inventory_item (property_id, category_id, item_name, description, serial_number, purchase_date, purchase_price, current_value, status, location_in_property) VALUES
(1, 1, 'Холодильник Samsung', 'Двухкамерный холодильник с No Frost', 'SN-SAMS12345', '2023-01-15', 45000.00, 40000.00, 'good', 'Кухня'),
(1, 2, 'Диван угловой', 'Угловой диван с механизмом раскладывания', 'SN-SOFA001', '2023-01-15', 35000.00, 30000.00, 'needs_repair', 'Гостиная'),
(1, 3, 'Комплект постельного белья', 'Хлопковое постельное белье, 4 предмета', NULL, '2023-06-10', 5000.00, 4500.00, 'good', 'Спальня'),
(1, 4, 'Кофемашина DeLonghi', 'Автоматическая кофемашина с капучинатором', 'SN-DEL456', '2023-03-20', 25000.00, 22000.00, 'good', 'Кухня'),
(1, 5, 'Смеситель Grohe', 'Смеситель для раковины с термостатом', 'SN-GRO789', '2023-01-15', 15000.00, 14000.00, 'good', 'Ванная комната');

-- 26. Проверки инвентаря (inventory_check) - 5 записей
INSERT INTO inventory_check (booking_id, check_type, checked_by, check_date, notes) VALUES
(1, 'check_in', 2, '2024-01-15 14:00:00', 'Все предметы на месте, состояние хорошее'),
(1, 'check_out', 2, '2024-01-20 12:00:00', 'Обнаружено повреждение дивана'),
(2, 'check_in', 3, '2024-03-01 15:00:00', 'Полная проверка, все ок'),
(3, 'check_in', 2, CURRENT_DATE + 7, 'Предварительная проверка'),
(4, 'periodic', 12, '2024-04-10 10:00:00', 'Плановая ежемесячная проверка');

-- 27. Состояние предметов при проверке (inventory_check_item) - 5 записей
INSERT INTO inventory_check_item (check_id, item_id, condition, damage_description, estimated_repair_cost) VALUES
(1, 1, 'present_ok', NULL, NULL),
(1, 2, 'present_ok', NULL, NULL),
(2, 1, 'present_ok', NULL, NULL),
(2, 2, 'present_damaged', 'Порез на обивке длиной 10 см', 5000.00),
(3, 3, 'present_ok', NULL, NULL);

-- Обновим счетчики на основе реальных данных
UPDATE property SET 
    rating = 4.8,
    views_count = 150
WHERE property_id = 1;

UPDATE property SET 
    rating = 4.9,
    views_count = 230
WHERE property_id = 2;

UPDATE property SET 
    rating = 4.2,
    views_count = 85
WHERE property_id = 3;

UPDATE property SET 
    rating = 4.7,
    views_count = 120
WHERE property_id = 4;

UPDATE property SET 
    rating = 4.5,
    views_count = 95
WHERE property_id = 5;

-- Обновим последний логин у пользователей
UPDATE users SET last_login = CURRENT_TIMESTAMP - INTERVAL '1 day' WHERE user_id = 1;
UPDATE users SET last_login = CURRENT_TIMESTAMP - INTERVAL '3 hours' WHERE user_id = 2;
UPDATE users SET last_login = CURRENT_TIMESTAMP - INTERVAL '2 days' WHERE user_id = 6;
UPDATE users SET last_login = CURRENT_TIMESTAMP - INTERVAL '1 week' WHERE user_id = 7;
UPDATE users SET last_login = CURRENT_TIMESTAMP - INTERVAL '5 days' WHERE user_id = 3;

-- Увеличим счетчики бронирований у гостей
UPDATE guest SET total_bookings = 3 WHERE guest_id = 1;
UPDATE guest SET total_bookings = 5 WHERE guest_id = 2;
UPDATE guest SET total_bookings = 2 WHERE guest_id = 4;
UPDATE guest SET total_bookings = 8 WHERE guest_id = 5;
UPDATE guest SET total_bookings = 4 WHERE guest_id = 6;

-- Увеличим счетчики использований промокодов
UPDATE promo_code SET used_count = 2 WHERE promo_id = 1;
UPDATE promo_code SET used_count = 1 WHERE promo_id = 2;
UPDATE promo_code SET used_count = 1 WHERE promo_id = 3;
UPDATE promo_code SET used_count = 1 WHERE promo_id = 4;

Пояснение какая таблица за что отвечает
1. Аутентификация и пользователи (users, user_sessions, audit_log)

    users - центральная таблица пользователей:

        Хранение учетных данных (email, хеш пароля)

        Роли и права доступа (guest, employee, admin, cleaner)

        Контактная информация и статус аккаунта

        Триггер для автоматического обновления updated_at

    user_sessions - сессии пользователей:

        Хранение токенов авторизации

        Управление временем жизни сессий

        Отслеживание устройства и IP пользователя

    audit_log - журнал аудита:

        Логирование всех действий пользователей

        Хранение "до" и "после" изменений (для отката/расследований)

        Для compliance и безопасности

2. Люди и команда (employee, guest, blacklist)

    employee - сотрудники агентства:

        Персональные данные сотрудников

        Должности, зарплаты, отделы

        Связь с учетной записью пользователя

    guest - клиенты/гости:

        Личные данные для договоров (паспорт, контакты)

        История и рейтинг как клиента

        Предпочтения и настройки

    blacklist - черный список:

        Блокировка проблемных клиентов

        Автоматическая проверка новых бронирований

        Многоуровневая система рисков

3. Недвижимость и каталог (property, property_type, property_category, property_photo)

    property - основные объекты аренды:

        Полное техническое описание (площадь, комнаты, этаж)

        Удобства и оборудование (Wi-Fi, кондиционер и т.д.)

        Локация (адрес, координаты, метро)

        Статус и видимость на сайте

    property_type / property_category - классификация:

        Типы: квартира, апартаменты, студия, лофт, пентхаус

        Категории: посуточная, долгосрочная, премиум, эконом

        Для фильтрации и поиска на сайте

    property_photo - медиаконтент:

        Галерея фотографий каждого объекта

        Главное фото и порядок отображения

        Миниатюры для быстрой загрузки

4. Бронирование и цены (booking, rental_plan, price_calendar, booking_service)

    booking - бронирования:

        Основная транзакционная таблица

        Даты проживания, количество гостей

        Статусы жизненного цикла (pending → confirmed → active → completed)

        Автоматическая генерация номеров бронирований

    rental_plan - тарифные планы:

        Типы аренды (daily, monthly)

        Минимальное/максимальное количество ночей

        Базовая цена и скидки

        Особенности каждого тарифа

    price_calendar - динамическое ценообразование:

        Цена за каждую конкретную дату

        Блокировка дат (недоступность)

        Сезонное ценообразование и акции

    booking_service - дополнительные услуги:

        Привязка услуг к бронированию

        Расписание оказания услуг

        Статус выполнения и стоимость

5. Финансы и платежи (payment, promo_code, promo_code_usage)

    payment - финансовые транзакции:

        Все платежи по бронированиям

        Поддержка разных способов оплаты (карта, наличные, перевод)

        Интеграция с платежными системами

        Возвраты и депозиты

    promo_code - система скидок:

        Создание промокодов с гибкими условиями

        Ограничения по времени, количеству, пользователям

        Процентные и фиксированные скидки

    promo_code_usage - история использования:

        Отслеживание эффективности промо-акций

        Ограничение повторного использования

6. Операции и обслуживание (cleaning_task, service, inventory_item, inventory_check)

    cleaning_task - управление уборкой:

        Планирование уборок (checkout, weekly, deep)

        Назначение клинеров

        Контроль качества и оценка работы

        Расчет стоимости уборки

    service - дополнительные услуги:

        Каталог платных услуг (трансфер, завтрак, химчистка)

        Цены и доступность

        Для up-sell и увеличения среднего чека

    inventory_item - учет имущества:

        Инвентаризация всех предметов в объектах

        Стоимость, состояние, местоположение

        Для страховки и амортизации

    inventory_check - проверки инвентаря:

        Контроль состояния имущества при заезде/выезде

        Фиксация повреждений с фото

        Расчет компенсаций за повреждения

7. Обратная связь и коммуникация (review, notification, message)

    review - отзывы клиентов:

        Оценки по категориям (чистота, расположение, ценность)

        Модерация отзывов перед публикацией

        Ответы от менеджеров

        Для SEO и доверия новых клиентов

    notification - система уведомлений:

        Автоматические уведомления о событиях

        Мультиканальность (email, push, in-app)

        Приоритеты и отложенная отправка

        Отслеживание доставки и прочтения

    message - внутренняя переписка:

        Чат между клиентами и менеджерами

        Привязка к конкретному бронированию

        История общения для службы поддержки

8. Конфигурация и настройки (site_setting)

    site_setting - гибкие настройки системы:

        Без переписывания кода можно менять:

            Время заезда/выезда

            Минимальное количество ночей

            Процент депозита

            Включение/отключение функций

        Разделение на категории для удобства управления

        Поддержка разных типов данных (boolean, integer, json)
