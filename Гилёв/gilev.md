разработка бд для риэлторского агенства

CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Таблица агентов (риэлторов)
CREATE TABLE agents (
    agent_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    license_number VARCHAR(50) UNIQUE,
    hire_date DATE DEFAULT CURRENT_DATE,
    is_active BOOLEAN DEFAULT TRUE,
    commission_rate DECIMAL(5,2) DEFAULT 2.5, -- процент комиссии
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Таблица продавцов/арендодателей
CREATE TABLE sellers (
    seller_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Таблица объектов недвижимости
CREATE TABLE properties (
    property_id SERIAL PRIMARY KEY,
    seller_id INT REFERENCES sellers(seller_id) ON DELETE SET NULL,
    agent_id INT REFERENCES agents(agent_id) ON DELETE SET NULL,
    address TEXT NOT NULL,
    city VARCHAR(100) NOT NULL,
    district VARCHAR(100),
    property_type VARCHAR(50) NOT NULL CHECK (property_type IN ('apartment', 'house', 'commercial', 'land', 'villa')),
    transaction_type VARCHAR(20) NOT NULL CHECK (transaction_type IN ('sale', 'rent')),
    price DECIMAL(12,2) NOT NULL,
    area DECIMAL(8,2) NOT NULL, -- площадь в кв.м
    bedrooms INT,
    bathrooms INT,
    description TEXT,
    status VARCHAR(20) DEFAULT 'available' CHECK (status IN ('available', 'reserved', 'sold', 'rented', 'withdrawn')),
    list_date DATE DEFAULT CURRENT_DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 5. Таблица просмотров объектов (voz - viewings)
CREATE TABLE voz (
    viewing_id SERIAL PRIMARY KEY,
    property_id INT NOT NULL REFERENCES properties(property_id) ON DELETE CASCADE,
    client_id INT NOT NULL REFERENCES clients(client_id) ON DELETE CASCADE,
    agent_id INT REFERENCES agents(agent_id) ON DELETE SET NULL,
    viewing_date DATE NOT NULL,
    viewing_time TIME NOT NULL,
    status VARCHAR(20) DEFAULT 'scheduled' CHECK (status IN ('scheduled', 'completed', 'cancelled', 'no_show')),
    client_feedback TEXT,
    agent_notes TEXT,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
-- 6. Таблица сделок
CREATE TABLE deals (
    deal_id SERIAL PRIMARY KEY,
    property_id INT NOT NULL REFERENCES properties(property_id) ON DELETE RESTRICT,
    buyer_client_id INT NOT NULL REFERENCES clients(client_id) ON DELETE RESTRICT,
    seller_client_id INT NOT NULL REFERENCES clients(client_id) ON DELETE RESTRICT,
    agent_id INT NOT NULL REFERENCES agents(agent_id) ON DELETE RESTRICT,
    deal_date DATE DEFAULT CURRENT_DATE,
    final_price DECIMAL(12,2) NOT NULL,
    commission DECIMAL(10,2) NOT NULL,
    deal_type VARCHAR(20) CHECK (deal_type IN ('sale', 'rent')),
    contract_number VARCHAR(50) UNIQUE,
    status VARCHAR(20) DEFAULT 'in_progress' CHECK (status IN ('in_progress', 'completed', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 7. Таблица платежей по сделкам
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    deal_id INT NOT NULL REFERENCES deals(deal_id) ON DELETE CASCADE,
    amount DECIMAL(10,2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_type VARCHAR(20) CHECK (payment_type IN ('deposit', 'installment', 'final', 'commission')),
    payment_method VARCHAR(30) CHECK (payment_method IN ('cash', 'bank_transfer', 'card', 'check')),
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'completed', 'failed')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

заполнение данными
-- 1. Заполняем таблицу агентов (сыктывкарские агенты с коми именами)
INSERT INTO agents (first_name, last_name, phone, email, license_number, commission_rate, hire_date) VALUES
('Анна', 'Трофимова', '+78212210001', 'anna.trofimova@nedvizhimost-syktyvkar.ru', 'LIC-SYKT-001', 2.5, '2020-03-15'),
('Дмитрий', 'Вурдов', '+78212210002', 'dmitry.vurdov@nedvizhimost-syktyvkar.ru', 'LIC-SYKT-002', 3.0, '2019-07-22'),
('Ольга', 'Попова', '+78212210003', 'olga.popova@nedvizhimost-syktyvkar.ru', 'LIC-SYKT-003', 2.8, '2021-01-10'),
('Игорь', 'Рассыхаев', '+78212210004', 'igor.rassyhaev@nedvizhimost-syktyvkar.ru', 'LIC-SYKT-004', 2.5, '2022-05-30'),
('Екатерина', 'Юрьева', '+78212210005', 'ekaterina.yureva@nedvizhimost-syktyvkar.ru', 'LIC-SYKT-005', 3.2, '2020-11-18');

-- 2. Заполняем таблицу продавцов/арендодателей
INSERT INTO sellers (first_name, last_name, phone, email, address) VALUES
('Александр', 'Журавлев', '+79121112233', 'zhuravlev@mail.ru', 'г. Сыктывкар, ул. Карла Маркса, д. 120'),
('Светлана', 'Мишарина', '+79122223344', 'misharina.s@yandex.ru', 'г. Сыктывкар, Эжвинский район, ул. Мира, д. 15'),
('Михаил', 'Выборов', '+79123334455', 'viborov.m@gmail.com', 'г. Сыктывкар, ул. Коммунистическая, д. 45'),
('Наталья', 'Тимушева', '+79124445566', 'timusheva.n@bk.ru', 'г. Сыктывкар, Октябрьский пр-т, д. 167'),
('Андрей', 'Тентюков', '+79125556677', 'tentyukov@mail.ru', 'г. Сыктывкар, ул. Первомайская, д. 62'),
('Людмила', 'Каракчиева', '+79126667788', 'karakchieva@yandex.ru', 'г. Сыктывкар, ул. Димитрова, д. 33'),
('Павел', 'Сидоров', '+79127778899', 'sidorov.pavel@gmail.com', 'г. Сыктывкар, ул. Советская, д. 28'),
('Галина', 'Оплеснина', '+79128889900', 'oplesnina.g@mail.ru', 'г. Сыктывкар, ул. Горького, д. 14');

-- 3. Заполняем таблицу клиентов (покупателей/арендаторов)
INSERT INTO clients (first_name, last_name, phone, email) VALUES
('Артем', 'Козлов', '+79130001122', 'kozlov.artem@mail.ru'),
('Юлия', 'Захарова', '+79131112233', 'zaharova.yu@gmail.com'),
('Владимир', 'Игушев', '+79132223344', 'igushev@yandex.ru'),
('Татьяна', 'Поздеева', '+79133334455', 'pozdteeva.t@bk.ru'),
('Роман', 'Бобрецов', '+79134445566', 'bobretsov@mail.ru'),
('Алина', 'Турьева', '+79135556677', 'tureva.alina@yandex.ru'),
('Константин', 'Носков', '+79136667788', 'noskov.k@gmail.com'),
('Елена', 'Волкова', '+79137778899', 'volkova.e@mail.ru'),
('Сергей', 'Демидов', '+79138889900', 'demidov.sergey@yandex.ru'),
('Мария', 'Костина', '+79139990011', 'kostina.maria@gmail.com'),
('Алексей', 'Панюков', '+79131001010', 'panyukov@mail.ru'),
('Ирина', 'Филиппова', '+79132112121', 'filippova.irina@yandex.ru');

-- 4. Заполняем таблицу объектов недвижимости в Сыктывкаре
INSERT INTO properties (seller_id, agent_id, address, city, district, property_type, transaction_type, price, area, bedrooms, bathrooms, description, status, list_date) VALUES
-- Квартиры на продажу в Центральном районе
(1, 1, 'ул. Карла Маркса, д. 120, кв. 45', 'Сыктывкар', 'Центральный', 'apartment', 'sale', 4200000, 56.3, 2, 1, 'Квартира с евроремонтом, пластиковые окна, новая сантехника. Вид на Стефановскую площадь.', 'available', '2024-01-15'),
(3, 2, 'ул. Коммунистическая, д. 45, кв. 12', 'Сыктывкар', 'Центральный', 'apartment', 'sale', 3800000, 48.7, 1, 1, 'Квартира в кирпичном доме, тихий двор, балкон застеклен. Рядом школа и детский сад.', 'available', '2024-02-10'),
(5, 3, 'ул. Первомайская, д. 62, кв. 38', 'Сыктывкар', 'Центральный', 'apartment', 'sale', 5100000, 67.8, 3, 1, 'Просторная трешка в панельном доме, раздельный санузел, лоджия 6 кв.м.', 'available', '2024-01-28'),
(2, 4, 'Эжвинский район, ул. Мира, д. 15, кв. 24', 'Сыктывкар', 'Эжвинский', 'apartment', 'rent', 22000, 42.5, 1, 1, 'Свежий ремонт, вся необходимая техника, интернет. Рядом ЛЦК "Шудлун".', 'available', '2024-02-05'),
(6, 1, 'ул. Димитрова, д. 33, кв. 18', 'Сыктывкар', 'Эжвинский', 'apartment', 'rent', 18000, 38.2, 1, 1, 'Уютная квартира для 1-2 человек. Меблирована, холодильник, стиральная машина.', 'available', '2024-02-12'),
(4, 2, 'Октябрьский пр-т, д. 167', 'Сыктывкар', 'Октябрьский', 'house', 'sale', 8500000, 98.5, 4, 2, 'Кирпичный дом с участком 6 соток, гараж, баня. Все коммуникации центральные.', 'available', '2024-01-20'),
(7, 3, 'ул. Советская, д. 28', 'Сыктывкар', 'Центральный', 'house', 'sale', 12500000, 145.0, 5, 2, 'Дом в историческом центре, капитальный ремонт 2022 года, камин, охраняемая территория.', 'available', '2024-02-01'),
(8, 5, 'ул. Горького, д. 14', 'Сыктывкар', 'Центральный', 'commercial', 'rent', 55000, 85.0, NULL, 2, 'Помещение свободного назначения 85 кв.м на 1 этаже. Высокие потолки, отдельный вход.', 'available', '2024-02-08'),
(1, 4, 'ул. Карла Маркса, д. 156', 'Сыктывкар', 'Центральный', 'commercial', 'sale', 15000000, 120.5, NULL, 3, 'Торговое помещение в центре города, пешеходный трафик, готовый бизнес-план кафе.', 'available', '2024-02-14'),
(3, 5, 'пос. Краснозатонский, ул. Лесная', 'Сыктывкар', 'Краснозатонский', 'land', 'sale', 1200000, 800.0, NULL, NULL, 'Участок ИЖС 8 соток, все коммуникации по границе, лесной массив рядом.', 'available', '2024-01-25'),
(2, 2, 'ул. Орджоникидзе, д. 23, кв. 56', 'Сыктывкар', 'Центральный', 'apartment', 'sale', 4600000, 58.4, 2, 1, 'Квартира с видом на реку Сысолу, панорамные окна.', 'reserved', '2024-01-18'),
(5, 1, 'Эжвинский район, ул. Славы, д. 8, кв. 32', 'Сыктывкар', 'Эжвинский', 'apartment', 'rent', 25000, 47.3, 2, 1, 'Современный ремонт, кондиционер, техника Bosch.', 'rented', '2024-01-30');

-- 5. Заполняем таблицу просмотров (voz) на ближайшие даты
INSERT INTO voz (property_id, client_id, agent_id, viewing_date, viewing_time, status, client_feedback, agent_notes, rating) VALUES
(1, 1, 1, '2024-03-15', '10:00', 'scheduled', NULL, 'Клиент хочет посмотреть состояние ремонта', NULL),
(1, 2, 1, '2024-03-15', '14:00', 'scheduled', NULL, 'Молодая семья с ребенком', NULL),
(3, 3, 3, '2024-03-15', '11:30', 'scheduled', NULL, 'Клиент переезжает из Воркуты', NULL),
(4, 4, 4, '2024-03-16', '12:00', 'scheduled', NULL, 'Студентка Коми пединститута', NULL),
(2, 5, 2, '2024-03-10', '15:00', 'completed', 'Квартира понравилась, но маленькая кухня', 'Клиент просит скидку 100 тыс.', 4),
(5, 6, 1, '2024-03-11', '16:30', 'completed', 'Хорошая квартира, устраивает цена', 'Готовы заключить договор аренды', 5),
(6, 7, 2, '2024-03-12', '13:00', 'completed', 'Дом требует ремонта, цена завышена', 'Отправить коммерческое предложение со скидкой', 3),
(7, 8, 3, '2024-03-13', '17:00', 'completed', 'Отличный дом, но не по карману', 'Клиент ищет варианты дешевле', 5),
(1, 9, 1, '2024-03-14', '10:00', 'cancelled', 'Передумали смотреть', 'Клиент нашел другой вариант', NULL),
(3, 10, 3, '2024-03-14', '12:00', 'cancelled', 'Сорвался приезд в город', 'Перенести на следующую неделю', NULL),
(4, 11, 4, '2024-03-13', '14:00', 'no_show', NULL, 'Клиент не пришел, не предупредил', NULL);

-- 6. Заполняем таблицу сделок (примеры завершенных сделок)
INSERT INTO deals (property_id, buyer_client_id, seller_client_id, agent_id, deal_date, final_price, commission, deal_type, contract_number, status) VALUES
(12, 5, 2, 2, '2024-02-20', 4550000, 136500, 'sale', 'ДКП-024-2024', 'completed'),
(7, 6, 5, 1, '2024-02-25', 24000, 720, 'rent', 'ДА-018-2024', 'completed'),
(7, 7, 4, 2, '2024-03-01', 8300000, 249000, 'sale', 'ДКП-027-2024', 'in_progress'),
(9, 8, 1, 5, '2024-03-05', 52000, 1664, 'rent', 'ДА-022-2024', 'in_progress');

-- 7. Заполняем таблицу платежей
INSERT INTO payments (deal_id, amount, payment_date, payment_type, payment_method, status, notes) VALUES
(5, 455000, '2024-02-20', 'deposit', 'bank_transfer', 'completed', 'Задаток 10%'),
(5, 4095000, '2024-02-28', 'final', 'bank_transfer', 'completed', 'Окончательный расчет')
(6, 24000, '2024-02-25', 'deposit', 'cash', 'completed', 'Оплата за первый месяц + залог'),
(6, 24000, '2024-03-25', 'installment', 'bank_transfer', 'pending', 'Оплата за второй месяц'),
(7, 2490000, '2024-03-01', 'deposit', 'bank_transfer', 'completed', 'Аванс 30%'),
(7, 249000, '2024-03-01', 'commission', 'bank_transfer', 'completed', 'Комиссия агентству'),
(8, 52000, '2024-03-05', 'deposit', 'bank_transfer', 'completed', 'Аренда за март'),
(8, 52000, '2024-03-05', 'commission', 'bank_transfer', 'completed', 'Комиссия за оформление');
