# Пояснительная записка к проекту БД «Склад автотоваров»

### 1. Введение и постановка задачи
Моей задачей была разработка структуры базы данных для автоматизации работы склада автозапчастей. В отличие от обычного магазина, склад работает не с розничными покупателями, а с контрагентами (поставщиками и оптовыми клиентами), а также требует строгого учета мест хранения товаров.

В качестве СУБД я выбрал **PostgreSQL**. Этот выбор обусловлен тем, что Postgres отлично справляется с высокими нагрузками, поддерживает сложные транзакции (ACID) и имеет мощный механизм триггеров, который я использовал для автоматического пересчета остатков.

### 2. Проектирование схемы данных (Анализ предметной области)
Перед написанием кода я изучил, как работает реальный склад. Я выделил следующие ключевые требования:
1.  **Товары**: Нужны не только название и цена, но и **Артикул** (Part Number), так как в автобизнесе это основной идентификатор.
2.  **Адресное хранение**: Кладовщик не должен искать деталь по всему складу. У каждого товара должен быть адрес (Ряд-Стеллаж-Полка).
3.  **Единый реестр контрагентов**: Нет смысла делить таблицы на «Поставщиков» и «Клиентов», так как иногда мы можем вернуть товар поставщику (он становится получателем). Я создал единую сущность `contractors`.
4.  **Движение товара**: Вместо «Продаж» на складе существуют «Движения» (Приход и Расход).

Я спроектировал базу данных в **3-й нормальной форме (3NF)**, чтобы избежать дублирования данных.

### 3. Реализация структуры БД (SQL-код)

Вот скрипт инициализации, который я написал.

```sql
-- Очистка (на случай перезапуска скрипта)
DROP TABLE IF EXISTS movement_items CASCADE;
DROP TABLE IF EXISTS stock_movements CASCADE;
DROP TABLE IF EXISTS products CASCADE;
DROP TABLE IF EXISTS contractors CASCADE;
DROP TABLE IF EXISTS manufacturers CASCADE;
DROP TABLE IF EXISTS categories CASCADE;

-- 1. Справочник категорий (Двигатель, Кузов, Электрика)
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

-- 2. Справочник производителей (Bosch, VAG, Toyota)
CREATE TABLE manufacturers (
    manufacturer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    country VARCHAR(50)
);

-- 3. Основная таблица товаров
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    part_number VARCHAR(50) NOT NULL,       -- Артикул (уникальный в рамках бренда, но разные бренды могут иметь одинаковые)
    name VARCHAR(255) NOT NULL,             -- Название детали
    
    -- Адресное хранение: Зона-Ряд-Полка (например, "A-12-04")
    location_code VARCHAR(20) DEFAULT 'RECEPTION', 
    
    -- Учетная цена (может быть средней закупочной)
    price NUMERIC(10, 2) NOT NULL CHECK (price >= 0),
    
    -- Текущий остаток. Мы будем менять его автоматически, но защита от минуса обязательна
    stock_quantity INTEGER NOT NULL DEFAULT 0 CHECK (stock_quantity >= 0),
    
    category_id INTEGER REFERENCES categories(category_id) ON DELETE SET NULL,
    manufacturer_id INTEGER REFERENCES manufacturers(manufacturer_id) ON DELETE SET NULL,
    
    description TEXT
);

-- 4. Таблица Контрагентов (Поставщики и Клиенты)
CREATE TABLE contractors (
    contractor_id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,  -- Название фирмы или ИП
    type VARCHAR(20) NOT NULL CHECK (type IN ('supplier', 'client')), -- Кто это?
    phone VARCHAR(20),
    email VARCHAR(100),
    address TEXT
);

-- 5. Журнал складских операций (Шапка накладной)
CREATE TABLE stock_movements (
    movement_id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Тип операции: 'in' (Приход на склад), 'out' (Расход/Отгрузка)
    operation_type VARCHAR(10) NOT NULL CHECK (operation_type IN ('in', 'out')),
    
    contractor_id INTEGER REFERENCES contractors(contractor_id) ON DELETE SET NULL,
    comments TEXT
);

-- 6. Состав накладной (Какие товары и сколько двигаем)
CREATE TABLE movement_items (
    item_id SERIAL PRIMARY KEY,
    movement_id INTEGER REFERENCES stock_movements(movement_id) ON DELETE CASCADE,
    product_id INTEGER REFERENCES products(product_id) ON DELETE RESTRICT,
    
    quantity INTEGER NOT NULL CHECK (quantity > 0), -- Только положительные числа
    price NUMERIC(10, 2) NOT NULL -- Цена именно в этой накладной (может отличаться от базовой)
);
```

---

### 4. Автоматизация (Триггеры)
*Это важная часть курсовой. Я не просто создал таблицы, я переложил логику на базу данных.*

**Проблема:** При оформлении накладной остаток товара в таблице `products` должен меняться сам. Если делать это через Python, можно допустить ошибку (рассинхрон).
**Решение:** Я написал триггер на PL/pgSQL.

```sql
-- Функция, которая будет вызываться при добавлении строки в накладную
CREATE OR REPLACE FUNCTION update_stock_on_movement()
RETURNS TRIGGER AS $$
BEGIN
    -- Сначала узнаем тип операции (приход или расход) из шапки накладной
    DECLARE
        op_type VARCHAR(10);
    BEGIN
        SELECT operation_type INTO op_type 
        FROM stock_movements 
        WHERE movement_id = NEW.movement_id;

        -- Если Приход ('in') -> Плюсуем товар
        IF op_type = 'in' THEN
            UPDATE products 
            SET stock_quantity = stock_quantity + NEW.quantity
            WHERE product_id = NEW.product_id;
            
        -- Если Расход ('out') -> Минусуем товар
        ELSIF op_type = 'out' THEN
            -- Проверка: хватает ли товара? (Хотя у нас есть CHECK, лучше проверить явно)
            IF (SELECT stock_quantity FROM products WHERE product_id = NEW.product_id) < NEW.quantity THEN
                RAISE EXCEPTION 'Ошибка: Недостаточно товара на складе для отгрузки!';
            END IF;

            UPDATE products 
            SET stock_quantity = stock_quantity - NEW.quantity
            WHERE product_id = NEW.product_id;
        END IF;
    END;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Сам триггер
CREATE TRIGGER trg_update_stock
AFTER INSERT ON movement_items
FOR EACH ROW
EXECUTE FUNCTION update_stock_on_movement();
```

### 5. Представления (Views) для удобства
Чтобы в будущем в Python-программе не писать сложные запросы, я заранее подготовил "Витрины" данных.

```sql
-- 1. Представление текущих остатков с понятными названиями
CREATE OR REPLACE VIEW v_warehouse_stock AS
SELECT 
    p.part_number AS Артикул,
    p.name AS Товар,
    m.name AS Бренд,
    p.location_code AS Ячейка,
    p.stock_quantity AS Остаток,
    p.price AS Учетная_Цена,
    (p.stock_quantity * p.price) AS Сумма_Остатка -- Сколько денег заморожено в товаре
FROM products p
LEFT JOIN manufacturers m ON p.manufacturer_id = m.manufacturer_id;

-- 2. Представление истории движения
CREATE OR REPLACE VIEW v_movement_history AS
SELECT 
    m.created_at AS Дата,
    CASE 
        WHEN m.operation_type = 'in' THEN 'Приход'
        WHEN m.operation_type = 'out' THEN 'Расход' 
    END AS Операция,
    c.name AS Контрагент,
    p.name AS Товар,
    mi.quantity AS Кол_во,
    mi.price AS Цена_операции
FROM movement_items mi
JOIN stock_movements m ON mi.movement_id = m.movement_id
JOIN products p ON mi.product_id = p.product_id
JOIN contractors c ON m.contractor_id = c.contractor_id
ORDER BY m.created_at DESC;
```

---

### 6. Пример работы (Тестирование)
Я провел тестирование базы данных, выполнив следующие операции:

```sql
-- 1. Заполним справочники
INSERT INTO categories (name) VALUES ('Масла'), ('Ходовая');
INSERT INTO manufacturers (name) VALUES ('Shell'), ('Kayaba');
INSERT INTO contractors (name, type) VALUES ('ООО Поставщик-1', 'supplier'), ('ИП Клиент-Авто', 'client');

-- 2. Создадим карточку товара (Изначально остаток 0)
INSERT INTO products (part_number, name, location_code, price, category_id, manufacturer_id)
VALUES ('5W40-4L', 'Масло Shell Helix Ultra 4л', 'Z-01-05', 4000.00, 1, 1);

-- 3. Оформляем ПРИХОД (Покупаем у поставщика 10 канистр)
INSERT INTO stock_movements (operation_type, contractor_id) VALUES ('in', 1); -- id=1
INSERT INTO movement_items (movement_id, product_id, quantity, price) VALUES (1, 1, 10, 3800.00);

-- В этот момент сработал триггер! Остаток товара стал 10.

-- 4. Оформляем РАСХОД (Продаем клиенту 2 канистры)
INSERT INTO stock_movements (operation_type, contractor_id) VALUES ('out', 2); -- id=2
INSERT INTO movement_items (movement_id, product_id, quantity, price) VALUES (2, 1, 2, 4500.00);

-- Триггер снова сработал. Остаток стал 8.
```


Данная архитектура является масштабируемой и позволяет в будущем добавить, например, инвентаризацию или резервирование товара.
