    service_center/
    │
    ├── service_center.db          # Файл базы данных SQLite
    ├── requirements.txt           # Зависимости Python
    ├── run.py                     # Главный файл запуска
    ├── fix_db.py                  # Файл для исправления базы
    │
    ├── app/                       # Основное приложение
    │   ├── __init__.py            # Инициализация Flask
    │   ├── models.py              # Модели базы данных
    │   ├── extensions.py          # Расширения Flask
    │   ├── routes.py              # Все маршруты
    │   │
    │   └── templates/             # HTML шаблоны
    │       ├── base.html          # Базовый шаблон
    │       ├── auth/              # Аутентификация
    │       │   └── login.html
    │       ├── dashboard/         # Главная панель
    │       │   ├── index.html
    │       │   ├── users.html
    │       │   ├── add_user.html
    │       │   ├── edit_user.html
    │       │   └── profile.html
    │       ├── warehouse/         # Склад
    │       │   ├── products.html
    │       │   └── cells.html
    │       ├── sales/             # Продажи
    │       │   ├── sales.html
    │       │   ├── add_sale.html
    │       │   └── return_sale.html
    │       ├── purchases/         # Закупки
    │       │   ├── purchases.html
    │       │   └── add_purchase.html
    │       ├── writeoff/          # Списание
    │       │   ├── write_offs.html
    │       │   └── add_write_off.html
    │       ├── repair/            # Ремонт
    │       │   ├── requests_list.html
    │       │   ├── archived_requests.html
    │       │   ├── request_detail.html
    │       │   ├── create_request.html
    │       │   ├── complete_request.html
    │       │   ├── return_unrepaired.html
    │       │   ├── print_template.html
    │       │   └── completion_print.html
    │       ├── reports/           # Отчеты
    │       │   └── monthly.html
    │       └── services/          # Услуги
    │           └── services.html
    │
    └── static/                    # Статические файлы (CSS, JS, изображения)
    └── css/
        └── styles.css
