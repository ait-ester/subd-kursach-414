    -- Таблица пользователей
    CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(128),
    role VARCHAR(20) DEFAULT 'employee',
    is_active BOOLEAN DEFAULT TRUE,
    is_login_allowed BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );

    -- Таблица ячеек склада
    CREATE TABLE cell (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    capacity INTEGER
    );

    -- Таблица товаров
    CREATE TABLE product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    quantity INTEGER DEFAULT 0,
    price FLOAT,
    purchase_price FLOAT,
    cell_id INTEGER,
    arrival_date DATE,
    searcher_id INTEGER,
    buyer_id INTEGER,
    FOREIGN KEY (cell_id) REFERENCES cell (id),
    FOREIGN KEY (searcher_id) REFERENCES user (id),
    FOREIGN KEY (buyer_id) REFERENCES user (id)
    );

    -- Таблица продаж
    CREATE TABLE sale (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sale_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    product_name VARCHAR(200),
    product_id INTEGER,
    quantity INTEGER DEFAULT 1,
    unit_price FLOAT DEFAULT 0.0,
    total_amount FLOAT DEFAULT 0.0,
    seller_id INTEGER,
    status VARCHAR(20) DEFAULT 'completed',
    return_reason TEXT,
    return_date DATETIME,
    FOREIGN KEY (product_id) REFERENCES product (id),
    FOREIGN KEY (seller_id) REFERENCES user (id)
    );

    -- Таблица закупок
    CREATE TABLE purchase (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_date DATE DEFAULT CURRENT_DATE,
    product_name VARCHAR(200) NOT NULL,
    quantity INTEGER DEFAULT 0 NOT NULL,
    unit_price FLOAT DEFAULT 0.0 NOT NULL,
    total_amount FLOAT DEFAULT 0.0 NOT NULL,
    cell_name VARCHAR(10),
    searcher_id INTEGER,
    buyer_id INTEGER,
    FOREIGN KEY (searcher_id) REFERENCES user (id),
    FOREIGN KEY (buyer_id) REFERENCES user (id)
    );

    -- Таблица списаний
    CREATE TABLE writeoff (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    reason TEXT NOT NULL,
    writeoff_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (product_id) REFERENCES product (id)
    );

    -- Таблица заявок на ремонт
    CREATE TABLE repair_request (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_number VARCHAR(20) UNIQUE NOT NULL,
    created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    completed_date DATETIME,
    status VARCHAR(20) DEFAULT 'new',
    client_full_name VARCHAR(200) NOT NULL,
    client_phone VARCHAR(20) NOT NULL,
    receiver_id INTEGER NOT NULL,
    performer_id INTEGER,
    equipment_name VARCHAR(200) NOT NULL,
    equipment_model VARCHAR(100),
    serial_number VARCHAR(100),
    problem_description TEXT NOT NULL,
    completed_work TEXT,
    parts_cost FLOAT DEFAULT 0.0,
    work_cost FLOAT DEFAULT 0.0,
    total_cost FLOAT DEFAULT 0.0,
    notes TEXT,
    is_archived BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (receiver_id) REFERENCES user (id),
    FOREIGN KEY (performer_id) REFERENCES user (id)
    );
