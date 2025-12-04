разработка бд для риэлторского агенства

Таблица сотрудников (агенты и администраторы)
id|full_name|phone| email |position| commission_rate| is_active| created_at 
INSERT INTO employees (full_name, phone, email, position, commission_rate) VALUES
('Иванов Александр Сергеевич', '+79161234567', 'ivanov@agency.ru', 'agent', 3.5),
('Петрова Мария Владимировна', '+79162345678', 'petrova@agency.ru', 'agent', 4.0),
('Сидоров Дмитрий Алексеевич', '+79163456789', 'sidorov@agency.ru', 'agent', 3.0),
('Козлова Анна Игоревна', '+79164567890', 'kozlova@agency.ru', 'manager', 2.5),
('Васильев Олег Петрович', '+79165678901', 'vasilev@agency.ru', 'agent', 3.2),
('Николаева Екатерина Дмитриевна', '+79166789012', 'nikolaeva@agency.ru', 'admin', NULL);

Таблица клиентов
id | full_name |phone email|  passport_data| notes|  created_at T
INSERT INTO clients (full_name, phone, email, passport_data, notes) VALUES
('Смирнов Алексей Борисович', '+79167777777', 'smirnov@mail.ru', '4510 123456, МВД по Республике Коми', 'Ищет 3-комнатную квартиру для семьи'),
('Волкова Ирина Сергеевна', '+79168888888', 'volkova@gmail.com', '4511 654321, МВД по Республике Коми', 'Продает квартиру в центре'),
('Федоров Павел Николаевич', '+79169999999', 'fedorov@yandex.ru', '4512 789012, МВД по Республике Коми', 'Инвестор, ищет коммерческую недвижимость'),
('Морозова Ольга Викторовна', '+79161010101', 'morozova@mail.ru', '4513 345678, МВД по Республике Коми', 'Семейная пара с ребенком'),
('Белов Артем Константинович', '+79161111111', 'belov@gmail.com', '4514 567890, МВД по Республике Коми', 'Молодой специалист, первый взнос от родителей'),
('Григорьева Татьяна Михайловна', '+79161212121', 'grigorieva@yandex.ru', '4515 098765, МВД по Республике Коми', 'Сдает квартиру в аренду'),
('Елесов Михаил Игоревич', '+79121826784','elesov666@gmail.com','4516 675266, МВД по Республике Коми','Одинокий, ищет квартиру');

Таблица объектов недвижимости
id| address| city| district |property_type| rooms| total_area| floor| total_floors| price| description| owner_id| agent_id| status| created_at| updated_at|
INSERT INTO properties (address, city, district, property_type, rooms, total_area, floor, total_floors, price, description, owner_id, agent_id, status) VALUES
('ул. Пермская, д. 10, кв. 25', 'Сыктывкар', 'Лесозавод', 'apartment', 2, 65.5, 5, 9, 7000000, 'Евроремонт с мебелью и техникой', 2, 1, 'active'),
('ул. Мира, д. 45, кв. 12', 'Сыктывкар', 'Эжва', 'apartment', 3, 85.0, 3, 12, 18000000, 'Требуется косметический ремонт, солнечная сторона', 2, 2, 'active'),
('ул. Красноборская, д. 15', 'Сыктывкар', 'пгт.Верхняя Максаковка', 'house', 5, 150.0, NULL, 2, 45000000, 'Частный дом с участком 6 соток, гараж', 6, 3, 'active'),
('ул. Первомайская, д. 72, офис 305', 'Сыктывкар', 'Центральный', 'commercial', NULL, 120.0, 3, 5, 3500000, 'Офисное помещение в бизнес-центре, ремонт', 3, 1, 'active'),
('ул. Петрозаводская, д. 33, кв. 78', 'Сыктывкар', 'Орбита', 'apartment', 1, 40.5, 7, 9, 8500000, 'Квартира-студия, свежий ремонт, балкон', 2, 2, 'sold'),
('ул. Корабельная, д. 19', 'Сыктывкар', 'пгт.Краснозатонский', 'land', NULL, 150.0, NULL, NULL, 12000000, 'Земельный участок под ИЖС, коммуникации', 3, 3, 'active');

Таблица заявок от клиентов
id| client_id| agent_id|request_type| property_type| min_price| max_price| min_rooms| district |status| notes |created_at 
INSERT INTO requests (client_id, agent_id, request_type, property_type, min_price, max_price, min_rooms, districts, status, notes) VALUES
(1, 1, 'buy', 'apartment', 15000000, 22000000, 3, ARRAY['Центральный', 'Орбита', 'Строитель'], 'active', 'Для семьи с двумя детьми, рядом школа'),
(4, 2, 'buy', 'apartment', 7000000, 12000000, 2, ARRAY['Юго-Западный', 'Давпон', 'Лесозавод'], 'active', 'Ипотека от Сбербанка, первый взнос 20%'),
(3, 1, 'buy', 'commercial', 20000000, 40000000, NULL, ARRAY['Центральный', 'Октябрьский'], 'completed', 'Под офис IT-компании'),
(5, 3, 'rent', 'apartment', 30000, 50000, 1, ARRAY['Центральный'], 'active', 'На 1 год, для работы в центре'),
(1, 2, 'sell', 'apartment', NULL, NULL, 2, ARRAY['Центральный'], 'cancelled', 'Продажа старой квартиры, но передумали'),
(4, 1, 'buy', 'house', 35000000, 50000000, 4, ARRAY['пгт.Верхняя Максаковка', 'пгт.Краснозатонский'], 'active', 'Загородный дом для постоянного проживания');

Таблица сделок
id| deal_number| property_id| buyer_id| seller_id| agent_id| deal_type| deal_date| deal_amount| commission_amount| contract_number| status| created_at
INSERT INTO deals (deal_number, property_id, buyer_id, seller_id, agent_id, deal_type, deal_date, deal_amount, commission_amount, contract_number, status) VALUES
('D-2024-00001', 5, 5, 2, 2, 'sale', '2024-01-15', 8200000, 246000, 'ДКП-2024-001', 'completed'),
('D-2024-00002', 1, 1, 2, 1, 'sale', '2024-02-20', 2450000, 85750, 'ДКП-2024-002', 'in_process'),
('D-2024-00003', 3, 4, 6, 3, 'sale', '2024-03-10', 4400000, 132000, 'ДКП-2024-003', 'completed'),
('D-2024-00004', 2, NULL, 2, 2, 'rent', '2024-01-25', 60000, 1800, 'ДА-2024-001', 'completed'),
('D-2024-00005', 4, 3, 3, 1, 'sale', '2024-03-01', 3400000, 119000, 'ДКП-2024-004', 'in_process'),
('D-2024-00006', 6, 4, 3, 3, 'sale', '2024-02-28', 1180000, 35400, 'ДКП-2024-005', 'cancelled');

Таблица просмотров объектов
id |property_id| client_id| agent_id| viewing_date| duration_minutes| client_feedback| created_at 
INSERT INTO view (property_id, client_id, agent_id, viewing_date, duration_minutes, client_feedback) VALUES
(1, 1, 1, '2024-02-15 14:00:00', 45, 'Нравится ремонт, но цена высокая, будем торговаться'),
(1, 4, 1, '2024-02-16 11:30:00', 30, 'Мало места для детской, ищем дальше'),
(2, 5, 2, '2024-01-20 16:00:00', 25, 'Требует ремонта, но локация хорошая'),
(3, 4, 3, '2024-03-05 12:00:00', 60, 'Идеально для нашей семьи, оформляем сделку'),
(4, 3, 1, '2024-02-25 15:00:00', 40, 'Подходит для офиса, обсуждаем с партнерами'),
(5, 5, 2, '2024-01-10 13:00:00', 20, 'Берем, устраивает все, особенно цена');

Таблица задач
id |title| description| assigned_to| due_date| priority| status| related_deal_id |created_at 
INSERT INTO tasks (title, description, assigned_to, due_date, priority, status, related_deal_id) VALUES
('Подготовить документы для сделки ДКП-2024-002', 'Собрать паспорта, выписки из ЕГРН, подготовить договор', 1, '2024-03-25', 'high', 'in_progress', 2),
('Организовать просмотр квартиры на Пермской для новых клиентов', 'Клиенты из Ухты, хотят посмотреть в субботу', 2, '2024-03-23', 'medium', 'pending', NULL),
('Согласовать сумму комиссии по сделке ДКП-2024-004', 'Клиент торгуется, нужно убедить в нашей комиссии', 1, '2024-03-20', 'high', 'completed', 5),
('Найти 3-комнатную квартиру для семьи Смирновых', 'Бюджет до 22 млн, районы: Центральный, Орбита', 1, '2024-04-10', 'medium', 'in_progress', NULL),
('Провести встречу с клиентом Волковой по продаже квартиры', 'Обсудить стратегию продаж, цену и рекламу', 2, '2024-03-22', 'medium', 'pending', NULL),
('Отправить отчет по сделкам за март', 'Сформировать Excel-таблицу со всеми завершенными сделками', 6, '2024-04-05', 'low', 'pending', NULL);
