import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import psycopg2
from psycopg2 import sql
from datetime import datetime, date
import sys

class RealEstateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("РИЭЛТОРСКОЕ АГЕНТСТВО СЫКТЫВКАР")
        self.root.geometry("1200x700")
        
        # Настройка стилей
        style = ttk.Style()
        style.theme_use('clam')
        
        # Цветовая схема
        self.colors = {
            'bg': '#f0f0f0',
            'header': '#2c3e50',
            'button': '#3498db',
            'button_hover': '#2980b9',
            'success': '#27ae60',
            'warning': '#e74c3c'
        }
        
        self.root.configure(bg=self.colors['bg'])
        
        # Подключение к БД
        self.db_connection = self.connect_to_db()
        
        # Создание интерфейса
        self.create_widgets()
        
        # Загрузка начальных данных
        self.load_initial_data()
        
    def connect_to_db(self):
        """Подключение к PostgreSQL базе данных"""
        try:
            conn = psycopg2.connect(
                host="localhost",
                database="gillop",
                user="gillop",
                password="22081921",  # Замените на ваш пароль
                port="5432"
            )
            return conn
        except Exception as e:
            messagebox.showerror("Ошибка подключения", f"Не удалось подключиться к БД:\n{str(e)}")
            sys.exit(1)
    
    def create_widgets(self):
        """Создание элементов интерфейса"""
        # Создание вкладок
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Вкладки
        self.create_properties_tab()
        self.create_viewings_tab()
        self.create_clients_tab()
        self.create_agents_tab()
        self.create_deals_tab()
        self.create_reports_tab()
        
        # Статус бар
        self.status_bar = tk.Label(
            self.root,
            text="Готово",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg='white'
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def create_properties_tab(self):
        """Вкладка объектов недвижимости"""
        self.tab_properties = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_properties, text="Объекты")
        
        # Панель управления
        control_frame = tk.Frame(self.tab_properties, bg=self.colors['bg'])
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(control_frame, text="Фильтры:", bg=self.colors['bg']).pack(side=tk.LEFT, padx=5)
        
        # Фильтры
        self.filter_type = ttk.Combobox(control_frame, values=['Все', 'apartment', 'house', 'commercial', 'land'], width=15)
        self.filter_type.pack(side=tk.LEFT, padx=5)
        self.filter_type.set('Все')
        
        self.filter_status = ttk.Combobox(control_frame, values=['Все', 'available', 'reserved', 'sold', 'rented'], width=15)
        self.filter_status.pack(side=tk.LEFT, padx=5)
        self.filter_status.set('available')
        
        ttk.Button(control_frame, text="Применить фильтры", command=self.load_properties).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Добавить объект", command=self.add_property_dialog).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Редактировать", command=self.edit_property_dialog).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Обновить", command=self.load_properties).pack(side=tk.LEFT, padx=5)
        
        # Таблица объектов
        columns = ('ID', 'Адрес', 'Район', 'Тип', 'Сделка', 'Цена', 'Площадь', 'Комнат', 'Статус', 'Агент')
        self.tree_properties = ttk.Treeview(self.tab_properties, columns=columns, show='headings', height=20)
        
        # Настройка колонок
        col_widths = [50, 250, 100, 80, 80, 100, 70, 70, 100, 150]
        for col, width in zip(columns, col_widths):
            self.tree_properties.heading(col, text=col)
            self.tree_properties.column(col, width=width, anchor='center')
        
        # Скроллбар
        scrollbar = ttk.Scrollbar(self.tab_properties, orient=tk.VERTICAL, command=self.tree_properties.yview)
        self.tree_properties.configure(yscrollcommand=scrollbar.set)
        
        # Упаковка
        self.tree_properties.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=10)
        
        # Контекстное меню
        self.context_menu_properties = tk.Menu(self.tree_properties, tearoff=0)
        self.context_menu_properties.add_command(label="Просмотреть детали", command=self.view_property_details)
        self.context_menu_properties.add_command(label="Редактировать", command=self.edit_property_dialog)
        self.context_menu_properties.add_command(label="Изменить статус", command=self.change_property_status)
        self.context_menu_properties.add_separator()
        self.context_menu_properties.add_command(label="Создать сделку", command=self.create_deal_from_property)
        self.context_menu_properties.add_command(label="Запланировать просмотр", command=self.schedule_viewing_from_property)
        self.context_menu_properties.add_separator()
        self.context_menu_properties.add_command(label="Удалить", command=self.delete_property)
        
        self.tree_properties.bind("<Button-3>", self.show_context_menu_properties)
        self.tree_properties.bind("<Double-Button-1>", lambda e: self.view_property_details())
    
    def create_viewings_tab(self):
        """Вкладка просмотров"""
        self.tab_viewings = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_viewings, text="Просмотры")
        
        # Панель управления
        control_frame = tk.Frame(self.tab_viewings, bg=self.colors['bg'])
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(control_frame, text="Статус:", bg=self.colors['bg']).pack(side=tk.LEFT, padx=5)
        
        self.filter_viewing_status = ttk.Combobox(control_frame, 
                                                  values=['Все', 'scheduled', 'completed', 'cancelled', 'no_show'], 
                                                  width=15)
        self.filter_viewing_status.pack(side=tk.LEFT, padx=5)
        self.filter_viewing_status.set('scheduled')
        
        ttk.Button(control_frame, text="Сегодня", 
                  command=lambda: self.load_viewings('today')).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Неделя", 
                  command=lambda: self.load_viewings('week')).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Все", 
                  command=lambda: self.load_viewings('all')).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Добавить просмотр", 
                  command=self.add_viewing_dialog).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Редактировать", 
                  command=self.edit_viewing_dialog).pack(side=tk.LEFT, padx=5)
        
        # Таблица просмотров
        columns = ('ID', 'Дата', 'Время', 'Объект', 'Клиент', 'Агент', 'Статус', 'Оценка')
        self.tree_viewings = ttk.Treeview(self.tab_viewings, columns=columns, show='headings', height=20)
        
        col_widths = [50, 100, 80, 200, 150, 150, 100, 70]
        for col, width in zip(columns, col_widths):
            self.tree_viewings.heading(col, text=col)
            self.tree_viewings.column(col, width=width, anchor='center')
        
        # Скроллбар
        scrollbar = ttk.Scrollbar(self.tab_viewings, orient=tk.VERTICAL, command=self.tree_viewings.yview)
        self.tree_viewings.configure(yscrollcommand=scrollbar.set)
        
        self.tree_viewings.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=10)
        
        # Контекстное меню
        self.context_menu_viewings = tk.Menu(self.tree_viewings, tearoff=0)
        self.context_menu_viewings.add_command(label="Отметить как завершенный", 
                                              command=lambda: self.update_viewing_status('completed'))
        self.context_menu_viewings.add_command(label="Отменить просмотр", 
                                              command=lambda: self.update_viewing_status('cancelled'))
        self.context_menu_viewings.add_command(label="Неявка", 
                                              command=lambda: self.update_viewing_status('no_show'))
        self.context_menu_viewings.add_separator()
        self.context_menu_viewings.add_command(label="Редактировать", 
                                              command=self.edit_viewing_dialog)
        self.context_menu_viewings.add_command(label="Добавить отзыв", 
                                              command=self.add_viewing_feedback)
        self.context_menu_viewings.add_separator()
        self.context_menu_viewings.add_command(label="Создать сделку", 
                                              command=self.create_deal_from_viewing)
        self.context_menu_viewings.add_separator()
        self.context_menu_viewings.add_command(label="Удалить", 
                                              command=self.delete_viewing)
        
        self.tree_viewings.bind("<Button-3>", self.show_context_menu_viewings)
        self.tree_viewings.bind("<Double-Button-1>", lambda e: self.edit_viewing_dialog())
    
    def create_clients_tab(self):
        """Вкладка клиентов"""
        self.tab_clients = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_clients, text="Клиенты")
        
        # Панель управления
        control_frame = tk.Frame(self.tab_clients, bg=self.colors['bg'])
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(control_frame, text="Поиск:", bg=self.colors['bg']).pack(side=tk.LEFT, padx=5)
        
        self.search_client = tk.Entry(control_frame, width=30)
        self.search_client.pack(side=tk.LEFT, padx=5)
        self.search_client.bind('<KeyRelease>', self.search_clients)
        
        ttk.Button(control_frame, text="Добавить клиента", 
                  command=self.add_client_dialog).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Редактировать", 
                  command=self.edit_client_dialog).pack(side=tk.LEFT, padx=5)
        
        # Таблица клиентов
        columns = ('ID', 'Фамилия', 'Имя', 'Телефон', 'Email', 'Дата регистрации')
        self.tree_clients = ttk.Treeview(self.tab_clients, columns=columns, show='headings', height=20)
        
        col_widths = [50, 120, 100, 120, 200, 120]
        for col, width in zip(columns, col_widths):
            self.tree_clients.heading(col, text=col)
            self.tree_clients.column(col, width=width, anchor='center')
        
        scrollbar = ttk.Scrollbar(self.tab_clients, orient=tk.VERTICAL, command=self.tree_clients.yview)
        self.tree_clients.configure(yscrollcommand=scrollbar.set)
        
        self.tree_clients.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=10)
        
        # Контекстное меню
        self.context_menu_clients = tk.Menu(self.tree_clients, tearoff=0)
        self.context_menu_clients.add_command(label="История просмотров", 
                                             command=self.show_client_viewings)
        self.context_menu_clients.add_command(label="История сделок", 
                                             command=self.show_client_deals)
        self.context_menu_clients.add_command(label="Редактировать", 
                                             command=self.edit_client_dialog)
        self.context_menu_clients.add_separator()
        self.context_menu_clients.add_command(label="Удалить", 
                                             command=self.delete_client)
        
        self.tree_clients.bind("<Button-3>", self.show_context_menu_clients)
        self.tree_clients.bind("<Double-Button-1>", lambda e: self.edit_client_dialog())
    
    def create_agents_tab(self):
        """Вкладка агентов"""
        self.tab_agents = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_agents, text="Агенты")
        
        # Панель управления
        control_frame = tk.Frame(self.tab_agents, bg=self.colors['bg'])
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(control_frame, text="Добавить агента", 
                  command=self.add_agent_dialog).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Редактировать", 
                  command=self.edit_agent_dialog).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Обновить статистику", 
                  command=self.load_agents).pack(side=tk.LEFT, padx=5)
        
        # Таблица агентов
        columns = ('ID', 'Фамилия', 'Имя', 'Телефон', 'Email', 'Лицензия', 'Комиссия %', 'Активен')
        self.tree_agents = ttk.Treeview(self.tab_agents, columns=columns, show='headings', height=20)
        
        col_widths = [50, 120, 100, 120, 200, 100, 80, 70]
        for col, width in zip(columns, col_widths):
            self.tree_agents.heading(col, text=col)
            self.tree_agents.column(col, width=width, anchor='center')
        
        scrollbar = ttk.Scrollbar(self.tab_agents, orient=tk.VERTICAL, command=self.tree_agents.yview)
        self.tree_agents.configure(yscrollcommand=scrollbar.set)
        
        self.tree_agents.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=10)
        
        # Статистика агента
        
    
    def create_deals_tab(self):
        """Вкладка сделок"""
        self.tab_deals = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_deals, text="Сделки")
        
        # Панель управления
        control_frame = tk.Frame(self.tab_deals, bg=self.colors['bg'])
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(control_frame, text="Статус:", bg=self.colors['bg']).pack(side=tk.LEFT, padx=5)
        
        self.filter_deal_status = ttk.Combobox(control_frame, 
                                               values=['Все', 'in_progress', 'completed', 'cancelled'], 
                                               width=15)
        self.filter_deal_status.pack(side=tk.LEFT, padx=5)
        self.filter_deal_status.set('in_progress')
        
        ttk.Button(control_frame, text="Применить", 
                  command=self.load_deals).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Новая сделка", 
                  command=self.add_deal_dialog).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Редактировать", 
                  command=self.edit_deal_dialog).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Добавить платеж", 
                  command=self.add_payment_dialog).pack(side=tk.LEFT, padx=5)
        
        # Таблица сделок
        columns = ('ID', 'Дата', 'Объект', 'Покупатель', 'Продавец', 'Агент', 'Сумма', 'Комиссия', 'Статус')
        self.tree_deals = ttk.Treeview(self.tab_deals, columns=columns, show='headings', height=15)
        
        col_widths = [50, 100, 150, 120, 120, 120, 100, 100, 100]
        for col, width in zip(columns, col_widths):
            self.tree_deals.heading(col, text=col)
            self.tree_deals.column(col, width=width, anchor='center')
        
        scrollbar = ttk.Scrollbar(self.tab_deals, orient=tk.VERTICAL, command=self.tree_deals.yview)
        self.tree_deals.configure(yscrollcommand=scrollbar.set)
        
        self.tree_deals.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=10)
        
        # Таблица платежей
        payment_frame = tk.LabelFrame(self.tab_deals, text="Платежи по сделке", bg=self.colors['bg'])
        payment_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Панель управления платежами
        payment_control = tk.Frame(payment_frame, bg=self.colors['bg'])
        payment_control.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(payment_control, text="Редактировать платеж", 
                  command=self.edit_payment_dialog).pack(side=tk.LEFT, padx=5)
        ttk.Button(payment_control, text="Удалить платеж", 
                  command=self.delete_payment).pack(side=tk.LEFT, padx=5)
        
        columns_payments = ('ID', 'Дата', 'Сумма', 'Тип', 'Метод', 'Статус', 'Примечания')
        self.tree_payments = ttk.Treeview(payment_frame, columns=columns_payments, show='headings', height=8)
        
        col_widths_payments = [50, 100, 100, 100, 100, 100, 150]
        for col, width in zip(columns_payments, col_widths_payments):
            self.tree_payments.heading(col, text=col)
            self.tree_payments.column(col, width=width, anchor='center')
        
        scrollbar_payments = ttk.Scrollbar(payment_frame, orient=tk.VERTICAL, command=self.tree_payments.yview)
        self.tree_payments.configure(yscrollcommand=scrollbar_payments.set)
        
        self.tree_payments.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=10)
        scrollbar_payments.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=10)
        
        self.tree_deals.bind('<<TreeviewSelect>>', self.show_deal_payments)
        self.tree_deals.bind("<Double-Button-1>", lambda e: self.edit_deal_dialog())
        
        # Контекстное меню для сделок
        self.context_menu_deals = tk.Menu(self.tree_deals, tearoff=0)
        self.context_menu_deals.add_command(label="Редактировать", command=self.edit_deal_dialog)
        self.context_menu_deals.add_command(label="Изменить статус", command=self.change_deal_status)
        self.context_menu_deals.add_separator()
        self.context_menu_deals.add_command(label="Добавить платеж", command=self.add_payment_dialog)
        self.context_menu_deals.add_separator()
        self.context_menu_deals.add_command(label="Удалить", command=self.delete_deal)
        
        self.tree_deals.bind("<Button-3>", self.show_context_menu_deals)
    
    def create_reports_tab(self):
        """Вкладка отчетов"""
        self.tab_reports = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_reports, text="Отчеты")
        
        # Панель управления отчетами
        control_frame = tk.Frame(self.tab_reports, bg=self.colors['bg'])
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        reports = [
            ("Статистика по месяцам", self.generate_monthly_stats),
            ("Топ агентов", self.generate_top_agents),
            ("Популярные районы", self.generate_popular_districts),
            ("Средние цены", self.generate_avg_prices),
            ("Активные клиенты", self.generate_active_clients),
            ("Финансовый отчет", self.generate_financial_report)
        ]
        
        for text, command in reports:
            ttk.Button(control_frame, text=text, command=command).pack(side=tk.LEFT, padx=5)
        
        # Поле для отчетов
        self.report_text = scrolledtext.ScrolledText(self.tab_reports, wrap=tk.WORD, width=100, height=30)
        self.report_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Кнопки экспорта
        export_frame = tk.Frame(self.tab_reports, bg=self.colors['bg'])
        export_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(export_frame, text="Сохранить отчет", 
                  command=self.save_report).pack(side=tk.LEFT, padx=5)
        ttk.Button(export_frame, text="Очистить", 
                  command=lambda: self.report_text.delete(1.0, tk.END)).pack(side=tk.LEFT, padx=5)
    
    # ========== МЕТОДЫ ЗАГРУЗКИ ДАННЫХ ==========
    
    def load_initial_data(self):
        """Загрузка начальных данных"""
        self.load_properties()
        self.load_viewings('today')
        self.load_clients()
        self.load_agents()
        self.load_deals()
        self.update_status("Данные загружены")
    
    def load_properties(self):
        """Загрузка объектов недвижимости"""
        try:
            self.tree_properties.delete(*self.tree_properties.get_children())
            
            cursor = self.db_connection.cursor()
            
            # Формирование запроса с фильтрами
            query = """
            SELECT p.property_id, p.address, p.district, p.property_type, 
                   p.transaction_type, p.price, p.area, p.bedrooms, p.status,
                   CONCAT(a.first_name, ' ', a.last_name) as agent_name
            FROM properties p
            LEFT JOIN agents a ON p.agent_id = a.agent_id
            WHERE 1=1
            """
            
            params = []
            
            # Применение фильтров
            if self.filter_type.get() != 'Все':
                query += " AND p.property_type = %s"
                params.append(self.filter_type.get())
            
            if self.filter_status.get() != 'Все':
                query += " AND p.status = %s"
                params.append(self.filter_status.get())
            
            query += " ORDER BY p.property_id"
            
            cursor.execute(query, params)
            properties = cursor.fetchall()
            
            for prop in properties:
                # Форматирование цены
                price = f"{prop[5]:,.0f} ₽" if prop[5] else "0 ₽"
                
                self.tree_properties.insert('', tk.END, values=(
                    prop[0], prop[1], prop[2] or '', prop[3], prop[4],
                    price, f"{prop[6]} м²", prop[7] or '', prop[8], prop[9] or ''
                ))
            
            cursor.close()
            self.update_status(f"Загружено объектов: {len(properties)}")
            
        except Exception as e:
            self.update_status(f"Ошибка загрузки: {str(e)}", error=True)
            messagebox.showerror("Ошибка", f"Не удалось загрузить объекты:\n{str(e)}")
    
    def load_viewings(self, period='today'):
        """Загрузка просмотров"""
        try:
            self.tree_viewings.delete(*self.tree_viewings.get_children())
            
            cursor = self.db_connection.cursor()
            
            query = """
            SELECT v.viewing_id, v.viewing_date, v.viewing_time,
                   p.address, 
                   CONCAT(c.first_name, ' ', c.last_name) as client_name,
                   CONCAT(a.first_name, ' ', a.last_name) as agent_name,
                   v.status, v.rating
            FROM voz v
            JOIN properties p ON v.property_id = p.property_id
            JOIN clients c ON v.client_id = c.client_id
            LEFT JOIN agents a ON v.agent_id = a.agent_id
            WHERE 1=1
            """
            
            params = []
            
            # Фильтр по статусу
            status_filter = self.filter_viewing_status.get()
            if status_filter != 'Все':
                query += " AND v.status = %s"
                params.append(status_filter)
            
            # Фильтр по периоду
            if period == 'today':
                query += " AND v.viewing_date = CURRENT_DATE"
            elif period == 'week':
                query += " AND v.viewing_date BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '7 days'"
            
            query += " ORDER BY v.viewing_date, v.viewing_time"
            
            cursor.execute(query, params)
            viewings = cursor.fetchall()
            
            for viewing in viewings:
                rating = viewing[7] if viewing[7] else '—'
                self.tree_viewings.insert('', tk.END, values=(
                    viewing[0], viewing[1], viewing[2],
                    viewing[3][:50] + '...' if len(viewing[3]) > 50 else viewing[3],
                    viewing[4], viewing[5] or '—', viewing[6], rating
                ))
            
            cursor.close()
            self.update_status(f"Загружено просмотров: {len(viewings)}")
            
        except Exception as e:
            self.update_status(f"Ошибка загрузки: {str(e)}", error=True)
    
    def load_clients(self):
        """Загрузка клиентов"""
        try:
            self.tree_clients.delete(*self.tree_clients.get_children())
            
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT client_id, last_name, first_name, phone, email, 
                       TO_CHAR(created_at, 'DD.MM.YYYY')
                FROM clients 
                ORDER BY last_name, first_name
            """)
            clients = cursor.fetchall()
            
            for client in clients:
                self.tree_clients.insert('', tk.END, values=client)
            
            cursor.close()
            self.update_status(f"Загружено клиентов: {len(clients)}")
            
        except Exception as e:
            self.update_status(f"Ошибка загрузки: {str(e)}", error=True)
    
    def search_clients(self, event=None):
        """Поиск клиентов"""
        search_term = self.search_client.get()
        
        try:
            self.tree_clients.delete(*self.tree_clients.get_children())
            
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT client_id, last_name, first_name, phone, email, 
                       TO_CHAR(created_at, 'DD.MM.YYYY')
                FROM clients 
                WHERE last_name ILIKE %s OR first_name ILIKE %s OR phone ILIKE %s
                ORDER BY last_name, first_name
            """, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
            
            clients = cursor.fetchall()
            
            for client in clients:
                self.tree_clients.insert('', tk.END, values=client)
            
            cursor.close()
            
        except Exception as e:
            self.update_status(f"Ошибка поиска: {str(e)}", error=True)
    
    def load_agents(self):
        """Загрузка агентов"""
        try:
            self.tree_agents.delete(*self.tree_agents.get_children())
            
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT agent_id, last_name, first_name, phone, email, 
                       license_number, commission_rate, 
                       CASE WHEN is_active THEN 'Да' ELSE 'Нет' END
                FROM agents 
                ORDER BY last_name, first_name
            """)
            agents = cursor.fetchall()
            
            for agent in agents:
                self.tree_agents.insert('', tk.END, values=agent)
            
            cursor.close()
            self.update_status(f"Загружено агентов: {len(agents)}")
            
        except Exception as e:
            self.update_status(f"Ошибка загрузки: {str(e)}", error=True)
    
    def load_deals(self):
        """Загрузка сделок"""
        try:
            self.tree_deals.delete(*self.tree_deals.get_children())
            
            cursor = self.db_connection.cursor()
            
            query = """
            SELECT d.deal_id, d.deal_date, p.address,
                   CONCAT(b.first_name, ' ', b.last_name) as buyer,
                   CONCAT(s.first_name, ' ', s.last_name) as seller,
                   CONCAT(a.first_name, ' ', a.last_name) as agent,
                   d.final_price, d.commission, d.status
            FROM deals d
            JOIN properties p ON d.property_id = p.property_id
            JOIN clients b ON d.buyer_client_id = b.client_id
            JOIN clients s ON d.seller_client_id = s.client_id
            JOIN agents a ON d.agent_id = a.agent_id
            WHERE 1=1
            """
            
            params = []
            
            # Фильтр по статусу
            status_filter = self.filter_deal_status.get()
            if status_filter != 'Все':
                query += " AND d.status = %s"
                params.append(status_filter)
            
            query += " ORDER BY d.deal_date DESC"
            
            cursor.execute(query, params)
            deals = cursor.fetchall()
            
            for deal in deals:
                self.tree_deals.insert('', tk.END, values=(
                    deal[0], deal[1], deal[2][:40] + '...' if len(deal[2]) > 40 else deal[2],
                    deal[3], deal[4], deal[5], 
                    f"{deal[6]:,.0f} ₽", f"{deal[7]:,.0f} ₽", deal[8]
                ))
            
            cursor.close()
            self.update_status(f"Загружено сделок: {len(deals)}")
            
        except Exception as e:
            self.update_status(f"Ошибка загрузки: {str(e)}", error=True)
    
    def show_deal_payments(self, event):
        """Показать платежи по выбранной сделке"""
        selection = self.tree_deals.selection()
        if not selection:
            return
        
        item = self.tree_deals.item(selection[0])
        deal_id = item['values'][0]
        
        try:
            self.tree_payments.delete(*self.tree_payments.get_children())
            
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT payment_id, payment_date, amount, payment_type, 
                       payment_method, status, notes
                FROM payments 
                WHERE deal_id = %s
                ORDER BY payment_date
            """, (deal_id,))
            
            payments = cursor.fetchall()
            
            for payment in payments:
                notes = payment[6][:30] + '...' if payment[6] and len(payment[6]) > 30 else payment[6]
                self.tree_payments.insert('', tk.END, values=(
                    payment[0], payment[1], f"{payment[2]:,.0f} ₽", 
                    payment[3], payment[4], payment[5], notes or ''
                ))
            
            cursor.close()
            
        except Exception as e:
            self.update_status(f"Ошибка загрузки платежей: {str(e)}", error=True)
    
    def show_agent_stats(self, event):
        """Показать статистику агента"""
        selection = self.tree_agents.selection()
        if not selection:
            return
        
        item = self.tree_agents.item(selection[0])
        agent_id = item['values'][0]
        
        try:
            cursor = self.db_connection.cursor()
            
            # Получаем статистику
            cursor.execute("""
                SELECT 
                    COUNT(DISTINCT p.property_id) as total_properties,
                    COUNT(DISTINCT v.viewing_id) as total_viewings,
                    COUNT(DISTINCT d.deal_id) as total_deals,
                    COALESCE(SUM(d.commission), 0) as total_commission,
                    AVG(v.rating) as avg_rating
                FROM agents a
                LEFT JOIN properties p ON a.agent_id = p.agent_id
                LEFT JOIN voz v ON a.agent_id = v.agent_id
                LEFT JOIN deals d ON a.agent_id = d.agent_id
                WHERE a.agent_id = %s
                GROUP BY a.agent_id
            """, (agent_id,))
            
            stats = cursor.fetchone()
            
            if stats:
                self.agent_stats_text.delete(1.0, tk.END)
                stats_text = f"""СТАТИСТИКА АГЕНТА:
────────────────────
Всего объектов: {stats[0]}
Всего просмотров: {stats[1]}
Всего сделок: {stats[2]}
Общая комиссия: {stats[3]:,.0f} ₽
Средняя оценка: {stats[4]:.1f if stats[4] else 'Н/Д'}/5

АКТИВНЫЕ ОБЪЕКТЫ:
────────────────────
"""
                
                # Активные объекты
                cursor.execute("""
                    SELECT p.address, p.price, p.status
                    FROM properties p
                    WHERE p.agent_id = %s AND p.status IN ('available', 'reserved')
                    ORDER BY p.status
                """, (agent_id,))
                
                properties = cursor.fetchall()
                
                for prop in properties:
                    stats_text += f"• {prop[0][:40]}...\n"
                    stats_text += f"  Цена: {prop[1]:,.0f} ₽ | Статус: {prop[2]}\n\n"
                
                self.agent_stats_text.insert(1.0, stats_text)
            
            cursor.close()
            
        except Exception as e:
            self.agent_stats_text.delete(1.0, tk.END)
            
    
    # ========== ДИАЛОГОВЫЕ ОКНА ДЛЯ ДОБАВЛЕНИЯ ==========
    
    def add_property_dialog(self):
        """Диалог добавления объекта"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Добавить объект недвижимости")
        dialog.geometry("500x600")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Получаем список агентов и продавцов
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT agent_id, first_name || ' ' || last_name FROM agents ORDER BY last_name")
        agents = cursor.fetchall()
        
        cursor.execute("SELECT seller_id, first_name || ' ' || last_name FROM sellers ORDER BY last_name")
        sellers = cursor.fetchall()
        
        cursor.close()
        
        # Поля формы
        fields = [
            ("Адрес:", tk.Entry(dialog, width=40)),
            ("Город:", tk.Entry(dialog, width=40)),
            ("Район:", ttk.Combobox(dialog, values=['Центральный', 'Эжвинский', 'Октябрьский', 'Краснозатонский', 'Другой'], width=37)),
            ("Тип:", ttk.Combobox(dialog, values=['apartment', 'house', 'commercial', 'land'], width=37)),
            ("Тип сделки:", ttk.Combobox(dialog, values=['sale', 'rent'], width=37)),
            ("Цена (₽):", tk.Entry(dialog, width=40)),
            ("Площадь (м²):", tk.Entry(dialog, width=40)),
            ("Комнат:", tk.Entry(dialog, width=40)),
            ("Санузлов:", tk.Entry(dialog, width=40)),
            ("Продавец:", ttk.Combobox(dialog, values=[f"{s[0]} - {s[1]}" for s in sellers], width=37)),
            ("Агент:", ttk.Combobox(dialog, values=[f"{a[0]} - {a[1]}" for a in agents], width=37)),
            ("Статус:", ttk.Combobox(dialog, values=['available', 'reserved'], width=37))
        ]
        
        # Описание
        tk.Label(dialog, text="Описание:").grid(row=len(fields), column=0, sticky='nw', padx=10, pady=5)
        description_text = scrolledtext.ScrolledText(dialog, width=50, height=5)
        description_text.grid(row=len(fields), column=1, columnspan=2, padx=10, pady=5)
        
        # Размещение полей
        for i, (label, widget) in enumerate(fields):
            tk.Label(dialog, text=label).grid(row=i, column=0, sticky='w', padx=10, pady=5)
            widget.grid(row=i, column=1, columnspan=2, padx=10, pady=5, sticky='ew')
        
        # Установка значений по умолчанию
        fields[1][1].insert(0, "Сыктывкар")
        fields[5][1].insert(0, "0")
        fields[6][1].insert(0, "0")
        fields[11][1].set('available')
        
        # Кнопки
        button_frame = tk.Frame(dialog)
        button_frame.grid(row=len(fields)+1, column=0, columnspan=3, pady=20)
        
        def save_property():
            try:
                # Получение значений
                seller_id = int(fields[9][1].get().split(' - ')[0]) if fields[9][1].get() else None
                agent_id = int(fields[10][1].get().split(' - ')[0]) if fields[10][1].get() else None
                
                cursor = self.db_connection.cursor()
                cursor.execute("""
                    INSERT INTO properties 
                    (seller_id, agent_id, address, city, district, property_type, 
                     transaction_type, price, area, bedrooms, bathrooms, 
                     description, status, list_date)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURRENT_DATE)
                """, (
                    seller_id, agent_id,
                    fields[0][1].get(), fields[1][1].get(), fields[2][1].get(),
                    fields[3][1].get(), fields[4][1].get(),
                    float(fields[5][1].get() or 0),
                    float(fields[6][1].get() or 0),
                    int(fields[7][1].get() or 0) if fields[7][1].get() else None,
                    int(fields[8][1].get() or 0) if fields[8][1].get() else None,
                    description_text.get(1.0, tk.END).strip(),
                    fields[11][1].get()
                ))
                
                self.db_connection.commit()
                cursor.close()
                
                messagebox.showinfo("Успех", "Объект успешно добавлен!")
                self.load_properties()
                dialog.destroy()
                
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось добавить объект:\n{str(e)}")
        
        ttk.Button(button_frame, text="Сохранить", command=save_property).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="Отмена", command=dialog.destroy).pack(side=tk.LEFT, padx=10)
    
    def add_viewing_dialog(self):
        """Диалог добавления просмотра"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Запланировать просмотр")
        dialog.geometry("400x400")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Получаем данные
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT property_id, address FROM properties WHERE status = 'available'")
        properties = cursor.fetchall()
        
        cursor.execute("SELECT client_id, first_name || ' ' || last_name FROM clients ORDER BY last_name")
        clients = cursor.fetchall()
        
        cursor.execute("SELECT agent_id, first_name || ' ' || last_name FROM agents WHERE is_active = TRUE")
        agents = cursor.fetchall()
        
        cursor.close()
        
        # Поля формы
        fields = [
            ("Объект:", ttk.Combobox(dialog, values=[f"{p[0]} - {p[1][:50]}..." for p in properties], width=40)),
            ("Клиент:", ttk.Combobox(dialog, values=[f"{c[0]} - {c[1]}" for c in clients], width=40)),
            ("Агент:", ttk.Combobox(dialog, values=[f"{a[0]} - {a[1]}" for a in agents], width=40)),
            ("Дата:", tk.Entry(dialog, width=40)),
            ("Время:", ttk.Combobox(dialog, values=[
                "09:00", "10:00", "11:00", "12:00", "13:00", 
                "14:00", "15:00", "16:00", "17:00", "18:00"
            ], width=37))
        ]
        
        for i, (label, widget) in enumerate(fields):
            tk.Label(dialog, text=label).grid(row=i, column=0, sticky='w', padx=10, pady=10)
            widget.grid(row=i, column=1, padx=10, pady=10, sticky='ew')
        
        # Установка значений по умолчанию
        fields[3][1].insert(0, date.today().strftime("%Y-%m-%d"))
        fields[4][1].set("10:00")
        
        # Заметки
        tk.Label(dialog, text="Заметки:").grid(row=5, column=0, sticky='nw', padx=10, pady=10)
        notes_text = scrolledtext.ScrolledText(dialog, width=40, height=5)
        notes_text.grid(row=5, column=1, padx=10, pady=10)
        
        # Кнопки
        button_frame = tk.Frame(dialog)
        button_frame.grid(row=6, column=0, columnspan=2, pady=20)
        
        def save_viewing():
            try:
                property_id = int(fields[0][1].get().split(' - ')[0])
                client_id = int(fields[1][1].get().split(' - ')[0])
                agent_id = int(fields[2][1].get().split(' - ')[0]) if fields[2][1].get() else None
                
                cursor = self.db_connection.cursor()
                cursor.execute("""
                    INSERT INTO voz 
                    (property_id, client_id, agent_id, viewing_date, viewing_time, 
                     status, agent_notes)
                    VALUES (%s, %s, %s, %s, %s, 'scheduled', %s)
                """, (
                    property_id, client_id, agent_id,
                    fields[3][1].get(), fields[4][1].get(),
                    notes_text.get(1.0, tk.END).strip()
                ))
                
                self.db_connection.commit()
                cursor.close()
                
                messagebox.showinfo("Успех", "Просмотр успешно запланирован!")
                self.load_viewings('today')
                dialog.destroy()
                
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось запланировать просмотр:\n{str(e)}")
        
        ttk.Button(button_frame, text="Сохранить", command=save_viewing).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="Отмена", command=dialog.destroy).pack(side=tk.LEFT, padx=10)
    
    def add_client_dialog(self):
        """Диалог добавления клиента"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Добавить клиента")
        dialog.geometry("400x300")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Поля формы
        fields = [
            ("Фамилия:", tk.Entry(dialog, width=30)),
            ("Имя:", tk.Entry(dialog, width=30)),
            ("Телефон:", tk.Entry(dialog, width=30)),
            ("Email:", tk.Entry(dialog, width=30))
        ]
        
        # Размещение полей
        for i, (label, widget) in enumerate(fields):
            tk.Label(dialog, text=label).grid(row=i, column=0, sticky='w', padx=10, pady=10)
            widget.grid(row=i, column=1, padx=10, pady=10, sticky='ew')
        
        # Кнопки
        button_frame = tk.Frame(dialog)
        button_frame.grid(row=len(fields), column=0, columnspan=2, pady=20)
        
        def save_client():
            try:
                cursor = self.db_connection.cursor()
                cursor.execute("""
                    INSERT INTO clients (first_name, last_name, phone, email)
                    VALUES (%s, %s, %s, %s)
                """, (
                    fields[1][1].get(),
                    fields[0][1].get(),
                    fields[2][1].get(),
                    fields[3][1].get() or None
                ))
                
                self.db_connection.commit()
                cursor.close()
                
                messagebox.showinfo("Успех", "Клиент успешно добавлен!")
                self.load_clients()
                dialog.destroy()
                
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось добавить клиента:\n{str(e)}")
        
        ttk.Button(button_frame, text="Сохранить", command=save_client).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="Отмена", command=dialog.destroy).pack(side=tk.LEFT, padx=10)
    
    def add_agent_dialog(self):
        """Диалог добавления агента"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Добавить агента")
        dialog.geometry("400x350")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Поля формы
        fields = [
            ("Фамилия:", tk.Entry(dialog, width=30)),
            ("Имя:", tk.Entry(dialog, width=30)),
            ("Телефон:", tk.Entry(dialog, width=30)),
            ("Email:", tk.Entry(dialog, width=30)),
            ("Лицензия:", tk.Entry(dialog, width=30)),
            ("Комиссия %:", tk.Entry(dialog, width=30))
        ]
        
        # Активность
        tk.Label(dialog, text="Активен:").grid(row=len(fields), column=0, sticky='w', padx=10, pady=10)
        is_active_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(dialog, variable=is_active_var).grid(row=len(fields), column=1, sticky='w', padx=10, pady=10)
        
        # Размещение полей
        for i, (label, widget) in enumerate(fields):
            tk.Label(dialog, text=label).grid(row=i, column=0, sticky='w', padx=10, pady=10)
            widget.grid(row=i, column=1, padx=10, pady=10, sticky='ew')
        
        # Установка значений по умолчанию
        fields[5][1].insert(0, "2.5")
        
        # Кнопки
        button_frame = tk.Frame(dialog)
        button_frame.grid(row=len(fields)+1, column=0, columnspan=2, pady=20)
        
        def save_agent():
            try:
                cursor = self.db_connection.cursor()
                cursor.execute("""
                    INSERT INTO agents 
                    (first_name, last_name, phone, email, license_number, commission_rate, is_active, hire_date)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, CURRENT_DATE)
                """, (
                    fields[1][1].get(),
                    fields[0][1].get(),
                    fields[2][1].get(),
                    fields[3][1].get(),
                    fields[4][1].get() or None,
                    float(fields[5][1].get() or 2.5),
                    is_active_var.get()
                ))
                
                self.db_connection.commit()
                cursor.close()
                
                messagebox.showinfo("Успех", "Агент успешно добавлен!")
                self.load_agents()
                dialog.destroy()
                
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось добавить агента:\n{str(e)}")
        
        ttk.Button(button_frame, text="Сохранить", command=save_agent).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="Отмена", command=dialog.destroy).pack(side=tk.LEFT, padx=10)
    
    # ========== ДИАЛОГ ДОБАВЛЕНИЯ СДЕЛКИ ==========
    
    def add_deal_dialog(self, property_id=None, client_id=None):
        """Диалог добавления сделки"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Новая сделка")
        dialog.geometry("650x550")  # Увеличим размер окна
        dialog.transient(self.root)
        dialog.grab_set()
    
        try:
            cursor = self.db_connection.cursor()
        
            # Получаем данные для выпадающих списков
            cursor.execute("""
                SELECT p.property_id, p.address, p.price, p.transaction_type,
                    CONCAT(s.first_name, ' ', s.last_name) as seller_name,
                    s.seller_id, s.client_id as seller_client_id
                FROM properties p
                JOIN sellers s ON p.seller_id = s.seller_id
                WHERE p.status IN ('available', 'reserved')
            """)
            properties = cursor.fetchall()
        
            cursor.execute("SELECT client_id, first_name || ' ' || last_name FROM clients ORDER BY last_name")
            clients = cursor.fetchall()
        
            cursor.execute("SELECT agent_id, first_name || ' ' || last_name FROM agents WHERE is_active = TRUE")
            agents = cursor.fetchall()
        
            cursor.close()
        
            # Переменные для хранения значений
            self.deal_property_var = tk.StringVar()
            self.deal_buyer_var = tk.StringVar()
            self.deal_seller_client_var = tk.StringVar()  # Для выбора продавца-клиента
            self.deal_agent_var = tk.StringVar()
            self.deal_price_var = tk.StringVar()
            self.deal_commission_var = tk.StringVar()
        
            # Словарь для хранения продавцов и их клиентов
            self.sellers_dict = {}
            for prop in properties:
                self.sellers_dict[prop[0]] = {
                    'seller_id': prop[4],
                    'seller_name': prop[3],
                    'seller_client_id': prop[5]
                }
        
            # Функция обновления продавца при выборе объекта
            def update_seller_info(event=None):
                selected = self.deal_property_var.get()
                if selected:
                    try:
                        # Извлекаем ID объекта
                        prop_id = int(selected.split(' - ')[0])
                    
                        # Находим информацию о продавце
                        seller_info = self.sellers_dict.get(prop_id)
                        if seller_info:
                            # Если у продавца есть связанный клиент
                            if seller_info['seller_client_id']:
                                # Находим этого клиента в списке
                                for client in clients:
                                    if client[0] == seller_info['seller_client_id']:
                                        self.deal_seller_client_var.set(f"{client[0]} - {client[1]}")
                                        break
                                else:
                                    # Если не нашли, предлагаем выбрать
                                    self.deal_seller_client_var.set('')
                                    messagebox.showinfo("Информация", 
                                        f"Продавец: {seller_info['seller_name']}\n"
                                        f"Выберите соответствующего клиента из списка")
                            else:
                                # Если нет связанного клиента
                                self.deal_seller_client_var.set('')
                                messagebox.showinfo("Информация", 
                                    f"Продавец: {seller_info['seller_name']}\n"
                                    f"У продавца нет связанного клиента. Выберите или создайте нового.")
                        
                            # Устанавливаем цену из объекта
                            for prop in properties:
                                if prop[0] == prop_id:
                                    self.deal_price_var.set(str(prop[2]))
                                
                                    # Автоматически рассчитываем комиссию (3%)
                                    try:
                                        commission = float(prop[2]) * 0.03
                                        self.deal_commission_var.set(f"{commission:,.0f}")
                                    except:
                                        self.deal_commission_var.set("0")
                                    break
                                
                    except Exception as e:
                        print(f"Ошибка обновления продавца: {e}")
        
            # Функция расчета комиссии при изменении цены
            def calculate_commission(event=None):
                try:
                    price_str = self.deal_price_var.get().replace(' ', '').replace(',', '').replace('₽', '')
                    price = float(price_str)
                    commission = price * 0.03  # 3% по умолчанию
                    self.deal_commission_var.set(f"{commission:,.0f}")
                except:
                    self.deal_commission_var.set("0")
        
            # Поля формы
            tk.Label(dialog, text="Объект недвижимости *:").grid(row=0, column=0, sticky='w', padx=10, pady=10)
            property_combo = ttk.Combobox(dialog, textvariable=self.deal_property_var, 
                                        values=[f"{p[0]} - {p[1][:60]}... (Цена: {p[2]:,.0f} ₽)" for p in properties], 
                                        width=50)
            property_combo.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
            property_combo.bind('<<ComboboxSelected>>', update_seller_info)
        
            tk.Label(dialog, text="Покупатель *:").grid(row=1, column=0, sticky='w', padx=10, pady=10)
            buyer_combo = ttk.Combobox(dialog, textvariable=self.deal_buyer_var, 
                                    values=[f"{c[0]} - {c[1]}" for c in clients], 
                                    width=50)
            buyer_combo.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
        
            tk.Label(dialog, text="Продавец (клиент) *:").grid(row=2, column=0, sticky='w', padx=10, pady=10)
            seller_client_combo = ttk.Combobox(dialog, textvariable=self.deal_seller_client_var, 
                                            values=[f"{c[0]} - {c[1]}" for c in clients], 
                                            width=50)
            seller_client_combo.grid(row=2, column=1, padx=10, pady=10, sticky='ew')
        
            # Кнопка для создания нового клиента-продавца
            def create_new_seller_client():
                # Диалог быстрого создания клиента
                new_dialog = tk.Toplevel(dialog)
                new_dialog.title("Быстрое создание клиента-продавца")
                new_dialog.geometry("400x250")
                new_dialog.transient(dialog)
                new_dialog.grab_set()
            
                tk.Label(new_dialog, text="Фамилия:").grid(row=0, column=0, sticky='w', padx=10, pady=10)
                last_name_var = tk.StringVar()
                tk.Entry(new_dialog, textvariable=last_name_var, width=30).grid(row=0, column=1, padx=10, pady=10)
            
                tk.Label(new_dialog, text="Имя:").grid(row=1, column=0, sticky='w', padx=10, pady=10)
                first_name_var = tk.StringVar()
                tk.Entry(new_dialog, textvariable=first_name_var, width=30).grid(row=1, column=1, padx=10, pady=10)
            
                tk.Label(new_dialog, text="Телефон:").grid(row=2, column=0, sticky='w', padx=10, pady=10)
                phone_var = tk.StringVar()
                tk.Entry(new_dialog, textvariable=phone_var, width=30).grid(row=2, column=1, padx=10, pady=10)
            
                tk.Label(new_dialog, text="Email (опционально):").grid(row=3, column=0, sticky='w', padx=10, pady=10)
                email_var = tk.StringVar()
                tk.Entry(new_dialog, textvariable=email_var, width=30).grid(row=3, column=1, padx=10, pady=10)
            
                def save_new_client():
                    try:
                        if not all([last_name_var.get(), first_name_var.get(), phone_var.get()]):
                            messagebox.showerror("Ошибка", "Заполните обязательные поля: Фамилия, Имя, Телефон")
                            return
                    
                        cursor = self.db_connection.cursor()
                        cursor.execute("""
                            INSERT INTO clients (first_name, last_name, phone, email)
                            VALUES (%s, %s, %s, %s)
                            RETURNING client_id, first_name || ' ' || last_name as client_name
                        """, (
                            first_name_var.get(),
                            last_name_var.get(),
                            phone_var.get(),
                            email_var.get() or None
                        ))
                    
                        new_client = cursor.fetchone()
                    
                        # Если выбран объект, обновляем продавца
                        if self.deal_property_var.get():
                            prop_id = int(self.deal_property_var.get().split(' - ')[0])
                            seller_info = self.sellers_dict.get(prop_id)
                        
                            if seller_info:
                                # Обновляем связь продавца с клиентом
                                cursor.execute("""
                                    UPDATE sellers 
                                    SET client_id = %s
                                    WHERE seller_id = %s
                                """, (new_client[0], seller_info['seller_id']))
                    
                        self.db_connection.commit()
                        cursor.close()
                    
                        # Обновляем комбобокс
                        seller_client_combo['values'] = list(seller_client_combo['values']) + [f"{new_client[0]} - {new_client[1]}"]
                        seller_client_combo.set(f"{new_client[0]} - {new_client[1]}")
                    
                        messagebox.showinfo("Успех", "Клиент создан и связан с продавцом!")
                        new_dialog.destroy()
                    
                    except Exception as e:
                        messagebox.showerror("Ошибка", f"Не удалось создать клиента:\n{str(e)}")
            
                ttk.Button(new_dialog, text="Сохранить", command=save_new_client).grid(row=4, column=0, columnspan=2, pady=20)
        
            
        
            tk.Label(dialog, text="Агент *:").grid(row=4, column=0, sticky='w', padx=10, pady=10)
            agent_combo = ttk.Combobox(dialog, textvariable=self.deal_agent_var, 
                                    values=[f"{a[0]} - {a[1]}" for a in agents], 
                                    width=50)
            agent_combo.grid(row=4, column=1, padx=10, pady=10, sticky='ew')
        
            tk.Label(dialog, text="Тип сделки:").grid(row=5, column=0, sticky='w', padx=10, pady=10)
            self.deal_type_var = tk.StringVar(value='sale')
            ttk.Combobox(dialog, textvariable=self.deal_type_var, 
                        values=['sale', 'rent'], width=15, state='readonly').grid(row=5, column=1, sticky='w', padx=10, pady=10)
        
            tk.Label(dialog, text="Финальная цена (₽) *:").grid(row=6, column=0, sticky='w', padx=10, pady=10)
            price_entry = tk.Entry(dialog, textvariable=self.deal_price_var, width=30)
            price_entry.grid(row=6, column=1, sticky='w', padx=10, pady=10)
            price_entry.bind('<KeyRelease>', calculate_commission)
        
            tk.Label(dialog, text="Комиссия (₽) *:").grid(row=7, column=0, sticky='w', padx=10, pady=10)
            commission_entry = tk.Entry(dialog, textvariable=self.deal_commission_var, width=30)
            commission_entry.grid(row=7, column=1, sticky='w', padx=10, pady=10)
        
            tk.Label(dialog, text="Дата сделки:").grid(row=8, column=0, sticky='w', padx=10, pady=10)
            self.deal_date_var = tk.StringVar(value=date.today().strftime("%Y-%m-%d"))
            tk.Entry(dialog, textvariable=self.deal_date_var, width=30).grid(row=8, column=1, sticky='w', padx=10, pady=10)
        
            tk.Label(dialog, text="Номер договора:").grid(row=9, column=0, sticky='w', padx=10, pady=10)
            self.deal_contract_var = tk.StringVar()
            tk.Entry(dialog, textvariable=self.deal_contract_var, width=30).grid(row=9, column=1, sticky='w', padx=10, pady=10)
        
            tk.Label(dialog, text="Статус:").grid(row=10, column=0, sticky='w', padx=10, pady=10)
            self.deal_status_var = tk.StringVar(value='in_progress')
            ttk.Combobox(dialog, textvariable=self.deal_status_var, 
                        values=['in_progress', 'completed', 'cancelled'], width=15).grid(row=10, column=1, sticky='w', padx=10, pady=10)
        
            # Если переданы параметры, устанавливаем значения
            if property_id:
                for prop in properties:
                    if prop[0] == property_id:
                        property_combo.set(f"{prop[0]} - {prop[1][:60]}... (Цена: {prop[2]:,.0f} ₽)")
                        update_seller_info()
                        self.deal_type_var.set(prop[3])
                        break
        
            if client_id:
                for client in clients:
                    if client[0] == client_id:
                        buyer_combo.set(f"{client[0]} - {client[1]}")
                        break
        
            # Кнопки
            button_frame = tk.Frame(dialog)
            button_frame.grid(row=11, column=0, columnspan=2, pady=20)
        
            def save_deal():
                try:
                    # Проверка обязательных полей
                    if not all([self.deal_property_var.get(), self.deal_buyer_var.get(), 
                            self.deal_seller_client_var.get(), self.deal_agent_var.get(),
                            self.deal_price_var.get(), self.deal_commission_var.get()]):
                        messagebox.showerror("Ошибка", "Заполните все обязательные поля (*)")
                        return
                
                    # Извлекаем ID из строк
                    property_id = int(self.deal_property_var.get().split(' - ')[0])
                    buyer_id = int(self.deal_buyer_var.get().split(' - ')[0])
                    seller_client_id = int(self.deal_seller_client_var.get().split(' - ')[0])
                    agent_id = int(self.deal_agent_var.get().split(' - ')[0])
                
                    # Проверяем, что покупатель и продавец - разные люди
                    if buyer_id == seller_client_id:
                        messagebox.showerror("Ошибка", "Покупатель и продавец не могут быть одним и тем же человеком!")
                        return
                
                    # Преобразуем цену и комиссию
                    price_str = self.deal_price_var.get().replace(' ', '').replace(',', '').replace('₽', '')
                    commission_str = self.deal_commission_var.get().replace(' ', '').replace(',', '').replace('₽', '')
                
                    price = float(price_str)
                    commission = float(commission_str)
                
                    # Создаем сделку
                    cursor = self.db_connection.cursor()
                    cursor.execute("""
                        INSERT INTO deals 
                        (property_id, buyer_client_id, seller_client_id, agent_id, 
                        deal_date, final_price, commission, deal_type, 
                        contract_number, status)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (
                        property_id, buyer_id, seller_client_id, agent_id,
                        self.deal_date_var.get() or date.today(),
                        price, commission, self.deal_type_var.get(),
                        self.deal_contract_var.get() or None,
                        self.deal_status_var.get()
                    ))
                
                    # Обновляем статус объекта
                    new_status = 'sold' if self.deal_type_var.get() == 'sale' else 'rented'
                    cursor.execute("""
                        UPDATE properties 
                        SET status = %s, updated_at = CURRENT_TIMESTAMP
                        WHERE property_id = %s
                    """, (new_status, property_id))
                
                    self.db_connection.commit()
                    cursor.close()
                
                    messagebox.showinfo("Успех", "Сделка успешно добавлена!")
                    self.load_deals()
                    self.load_properties()
                    dialog.destroy()
                
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Не удалось создать сделку:\n{str(e)}")
        
            ttk.Button(button_frame, text="Сохранить", command=save_deal).pack(side=tk.LEFT, padx=10)
            ttk.Button(button_frame, text="Отмена", command=dialog.destroy).pack(side=tk.LEFT, padx=10)
        
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить данные:\n{str(e)}")
            dialog.destroy()
    # ========== ОСТАЛЬНЫЕ МЕТОДЫ ==========
    
    def view_property_details(self):
        """Просмотр деталей объекта"""
        selection = self.tree_properties.selection()
        if not selection:
            return
        
        item = self.tree_properties.item(selection[0])
        property_id = item['values'][0]
        
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT p.*, 
                       CONCAT(a.first_name, ' ', a.last_name) as agent_name,
                       CONCAT(s.first_name, ' ', s.last_name) as seller_name
                FROM properties p
                LEFT JOIN agents a ON p.agent_id = a.agent_id
                LEFT JOIN sellers s ON p.seller_id = s.seller_id
                WHERE p.property_id = %s
            """, (property_id,))
            
            prop = cursor.fetchone()
            cursor.close()
            
            if prop:
                details = f"""ДЕТАЛИ ОБЪЕКТА #{property_id}
────────────────────
Адрес: {prop[3]}
Город: {prop[4]}
Район: {prop[5]}
Тип: {prop[6]}
Сделка: {prop[7]}
Цена: {prop[8]:,.0f} ₽
Площадь: {prop[9]} м²
Комнат: {prop[10] or '—'}
Санузлов: {prop[11] or '—'}
Статус: {prop[12]}
Дата добавления: {prop[15].strftime('%d.%m.%Y') if prop[15] else '—'}

Агент: {prop[18] or '—'}
Продавец: {prop[19] or '—'}

Описание:
{prop[13] or 'Нет описания'}
"""
                
                messagebox.showinfo(f"Объект #{property_id}", details)
                
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить детали:\n{str(e)}")
    
    def schedule_viewing_from_property(self):
        """Запланировать просмотр для выбранного объекта"""
        selection = self.tree_properties.selection()
        if not selection:
            return
        
        item = self.tree_properties.item(selection[0])
        property_id = item['values'][0]
        
        # Открываем диалог добавления просмотра
        self.add_viewing_dialog()
    
    def show_context_menu_properties(self, event):
        """Показать контекстное меню для объектов"""
        item = self.tree_properties.identify_row(event.y)
        if item:
            self.tree_properties.selection_set(item)
            self.context_menu_properties.post(event.x_root, event.y_root)
    
    def show_context_menu_viewings(self, event):
        """Показать контекстное меню для просмотров"""
        item = self.tree_viewings.identify_row(event.y)
        if item:
            self.tree_viewings.selection_set(item)
            self.context_menu_viewings.post(event.x_root, event.y_root)
    
    def show_context_menu_clients(self, event):
        """Показать контекстное меню для клиентов"""
        item = self.tree_clients.identify_row(event.y)
        if item:
            self.tree_clients.selection_set(item)
            self.context_menu_clients.post(event.x_root, event.y_root)
    
    def show_context_menu_deals(self, event):
        """Показать контекстное меню для сделок"""
        item = self.tree_deals.identify_row(event.y)
        if item:
            self.tree_deals.selection_set(item)
            self.context_menu_deals.post(event.x_root, event.y_root)
    
    def update_viewing_status(self, status):
        """Обновить статус просмотра"""
        selection = self.tree_viewings.selection()
        if not selection:
            return
        
        item = self.tree_viewings.item(selection[0])
        viewing_id = item['values'][0]
        
        try:
            cursor = self.db_connection.cursor()
            
            if status == 'completed':
                # Запрашиваем отзыв и оценку
                dialog = tk.Toplevel(self.root)
                dialog.title("Завершить просмотр")
                dialog.geometry("300x200")
                dialog.transient(self.root)
                dialog.grab_set()
                
                tk.Label(dialog, text="Оценка (1-5):").pack(pady=5)
                rating_var = tk.StringVar()
                ttk.Combobox(dialog, textvariable=rating_var, values=['1', '2', '3', '4', '5'], width=10).pack(pady=5)
                
                tk.Label(dialog, text="Отзыв клиента:").pack(pady=5)
                feedback_text = scrolledtext.ScrolledText(dialog, width=40, height=4)
                feedback_text.pack(pady=5)
                
                def save_feedback():
                    try:
                        rating = int(rating_var.get()) if rating_var.get() else None
                        feedback = feedback_text.get(1.0, tk.END).strip()
                        
                        cursor.execute("""
                            UPDATE voz 
                            SET status = 'completed', rating = %s, client_feedback = %s,
                                updated_at = CURRENT_TIMESTAMP
                            WHERE viewing_id = %s
                        """, (rating, feedback, viewing_id))
                        
                        self.db_connection.commit()
                        dialog.destroy()
                        self.load_viewings('all')
                        messagebox.showinfo("Успех", "Просмотр отмечен как завершенный")
                        
                    except Exception as e:
                        messagebox.showerror("Ошибка", f"Не удалось сохранить:\n{str(e)}")
                
                ttk.Button(dialog, text="Сохранить", command=save_feedback).pack(pady=10)
                
            else:
                cursor.execute("""
                    UPDATE voz 
                    SET status = %s, updated_at = CURRENT_TIMESTAMP
                    WHERE viewing_id = %s
                """, (status, viewing_id))
                
                self.db_connection.commit()
                self.load_viewings('all')
                
                status_text = {
                    'cancelled': 'отменен',
                    'no_show': 'отмечен как неявка'
                }.get(status, 'обновлен')
                
                messagebox.showinfo("Успех", f"Просмотр {status_text}")
            
            cursor.close()
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось обновить статус:\n{str(e)}")
    
    def add_viewing_feedback(self):
        """Добавить отзыв к просмотру"""
        self.update_viewing_status('completed')
    
    # ========== МЕТОДЫ УДАЛЕНИЯ ==========
    
    def delete_property(self):
        """Удаление объекта"""
        if messagebox.askyesno("Подтверждение", "Удалить выбранный объект?\nВсе связанные просмотры также будут удалены."):
            selection = self.tree_properties.selection()
            if selection:
                property_id = self.tree_properties.item(selection[0])['values'][0]
                
                try:
                    cursor = self.db_connection.cursor()
                    cursor.execute("DELETE FROM properties WHERE property_id = %s", (property_id,))
                    self.db_connection.commit()
                    cursor.close()
                    
                    self.load_properties()
                    messagebox.showinfo("Успех", "Объект удален")
                    
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Не удалось удалить объект:\n{str(e)}")
    
    def delete_viewing(self):
        """Удаление просмотра"""
        if messagebox.askyesno("Подтверждение", "Удалить выбранный просмотр?"):
            selection = self.tree_viewings.selection()
            if selection:
                viewing_id = self.tree_viewings.item(selection[0])['values'][0]
                
                try:
                    cursor = self.db_connection.cursor()
                    cursor.execute("DELETE FROM voz WHERE viewing_id = %s", (viewing_id,))
                    self.db_connection.commit()
                    cursor.close()
                    
                    self.load_viewings('all')
                    messagebox.showinfo("Успех", "Просмотр удален")
                    
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Не удалось удалить просмотр:\n{str(e)}")
    
    def delete_client(self):
        """Удаление клиента"""
        if messagebox.askyesno("Подтверждение", "Удалить выбранного клиента?\nБудут также удалены все его просмотры."):
            selection = self.tree_clients.selection()
            if selection:
                client_id = self.tree_clients.item(selection[0])['values'][0]
                
                try:
                    cursor = self.db_connection.cursor()
                    cursor.execute("DELETE FROM clients WHERE client_id = %s", (client_id,))
                    self.db_connection.commit()
                    cursor.close()
                    
                    self.load_clients()
                    messagebox.showinfo("Успех", "Клиент удален")
                    
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Не удалось удалить клиента:\n{str(e)}")
    
    def delete_deal(self):
        """Удаление сделки"""
        selection = self.tree_deals.selection()
        if not selection:
            return
        
        if messagebox.askyesno("Подтверждение", "Удалить выбранную сделку?\nВсе связанные платежи также будут удалены."):
            deal_id = self.tree_deals.item(selection[0])['values'][0]
            
            try:
                cursor = self.db_connection.cursor()
                
                # Получаем property_id для обновления статуса
                cursor.execute("SELECT property_id FROM deals WHERE deal_id = %s", (deal_id,))
                property_data = cursor.fetchone()
                
                # Удаляем сделку (платежи удалятся каскадно)
                cursor.execute("DELETE FROM deals WHERE deal_id = %s", (deal_id,))
                
                # Обновляем статус объекта на available
                if property_data:
                    cursor.execute("""
                        UPDATE properties 
                        SET status = 'available', updated_at = CURRENT_TIMESTAMP
                        WHERE property_id = %s
                    """, (property_data[0],))
                
                self.db_connection.commit()
                cursor.close()
                
                self.load_deals()
                self.load_properties()
                messagebox.showinfo("Успех", "Сделка удалена")
                
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось удалить сделку:\n{str(e)}")
    
    # ========== МЕТОДЫ РЕДАКТИРОВАНИЯ ==========
    
    def edit_property_dialog(self):
        """Диалог редактирования объекта"""
        selection = self.tree_properties.selection()
        if not selection:
            messagebox.showwarning("Внимание", "Выберите объект для редактирования")
            return
        
        item = self.tree_properties.item(selection[0])
        property_id = item['values'][0]
        
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT * FROM properties WHERE property_id = %s
            """, (property_id,))
            
            property_data = cursor.fetchone()
            
            # Получаем списки для выпадающих списков
            cursor.execute("SELECT agent_id, first_name || ' ' || last_name FROM agents ORDER BY last_name")
            agents = cursor.fetchall()
            
            cursor.execute("SELECT seller_id, first_name || ' ' || last_name FROM sellers ORDER BY last_name")
            sellers = cursor.fetchall()
            
            cursor.close()
            
            if not property_data:
                messagebox.showerror("Ошибка", "Объект не найден")
                return
            
            dialog = tk.Toplevel(self.root)
            dialog.title(f"Редактирование объекта #{property_id}")
            dialog.geometry("500x600")
            dialog.transient(self.root)
            dialog.grab_set()
            
            # Поля формы
            fields = [
                ("Адрес:", tk.Entry(dialog, width=40)),
                ("Город:", tk.Entry(dialog, width=40)),
                ("Район:", ttk.Combobox(dialog, values=['Центральный', 'Эжвинский', 'Октябрьский', 'Краснозатонский', 'Другой'], width=37)),
                ("Тип:", ttk.Combobox(dialog, values=['apartment', 'house', 'commercial', 'land'], width=37)),
                ("Тип сделки:", ttk.Combobox(dialog, values=['sale', 'rent'], width=37)),
                ("Цена (₽):", tk.Entry(dialog, width=40)),
                ("Площадь (м²):", tk.Entry(dialog, width=40)),
                ("Комнат:", tk.Entry(dialog, width=40)),
                ("Санузлов:", tk.Entry(dialog, width=40)),
                ("Статус:", ttk.Combobox(dialog, values=['available', 'reserved', 'sold', 'rented', 'withdrawn'], width=37))
            ]
            
            # Описание
            tk.Label(dialog, text="Описание:").grid(row=len(fields), column=0, sticky='nw', padx=10, pady=5)
            description_text = scrolledtext.ScrolledText(dialog, width=50, height=5)
            description_text.grid(row=len(fields), column=1, columnspan=2, padx=10, pady=5)
            
            # Заполняем поля данными
            fields[0][1].insert(0, property_data[3])  # address
            fields[1][1].insert(0, property_data[4])  # city
            fields[2][1].set(property_data[5] or '')  # district
            fields[3][1].set(property_data[6])  # property_type
            fields[4][1].set(property_data[7])  # transaction_type
            fields[5][1].insert(0, str(property_data[8]))  # price
            fields[6][1].insert(0, str(property_data[9]))  # area
            fields[7][1].insert(0, str(property_data[10] or ''))  # bedrooms
            fields[8][1].insert(0, str(property_data[11] or ''))  # bathrooms
            fields[9][1].set(property_data[12])  # status
            description_text.insert(1.0, property_data[13] or '')  # description
            
            # Размещение полей
            for i, (label, widget) in enumerate(fields):
                tk.Label(dialog, text=label).grid(row=i, column=0, sticky='w', padx=10, pady=5)
                widget.grid(row=i, column=1, columnspan=2, padx=10, pady=5, sticky='ew')
            
            # Кнопки
            button_frame = tk.Frame(dialog)
            button_frame.grid(row=len(fields)+1, column=0, columnspan=3, pady=20)
            
            def save_changes():
                try:
                    cursor = self.db_connection.cursor()
                    
                    cursor.execute("""
                        UPDATE properties SET
                            address = %s,
                            city = %s,
                            district = %s,
                            property_type = %s,
                            transaction_type = %s,
                            price = %s,
                            area = %s,
                            bedrooms = %s,
                            bathrooms = %s,
                            status = %s,
                            description = %s,
                            updated_at = CURRENT_TIMESTAMP
                        WHERE property_id = %s
                    """, (
                        fields[0][1].get(),
                        fields[1][1].get(),
                        fields[2][1].get(),
                        fields[3][1].get(),
                        fields[4][1].get(),
                        float(fields[5][1].get() or 0),
                        float(fields[6][1].get() or 0),
                        int(fields[7][1].get() or 0) if fields[7][1].get() else None,
                        int(fields[8][1].get() or 0) if fields[8][1].get() else None,
                        fields[9][1].get(),
                        description_text.get(1.0, tk.END).strip(),
                        property_id
                    ))
                    
                    self.db_connection.commit()
                    cursor.close()
                    
                    messagebox.showinfo("Успех", "Изменения сохранены!")
                    self.load_properties()
                    dialog.destroy()
                    
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Не удалось сохранить изменения:\n{str(e)}")
            
            ttk.Button(button_frame, text="Сохранить", command=save_changes).pack(side=tk.LEFT, padx=10)
            ttk.Button(button_frame, text="Отмена", command=dialog.destroy).pack(side=tk.LEFT, padx=10)
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить данные объекта:\n{str(e)}")
    
    def edit_client_dialog(self):
        """Диалог редактирования клиента"""
        selection = self.tree_clients.selection()
        if not selection:
            messagebox.showwarning("Внимание", "Выберите клиента для редактирования")
            return
        
        item = self.tree_clients.item(selection[0])
        client_id = item['values'][0]
        
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT * FROM clients WHERE client_id = %s
            """, (client_id,))
            
            client_data = cursor.fetchone()
            cursor.close()
            
            if not client_data:
                messagebox.showerror("Ошибка", "Клиент не найден")
                return
            
            dialog = tk.Toplevel(self.root)
            dialog.title(f"Редактирование клиента #{client_id}")
            dialog.geometry("400x300")
            dialog.transient(self.root)
            dialog.grab_set()
            
            # Поля формы
            fields = [
                ("Фамилия:", tk.Entry(dialog, width=30)),
                ("Имя:", tk.Entry(dialog, width=30)),
                ("Телефон:", tk.Entry(dialog, width=30)),
                ("Email:", tk.Entry(dialog, width=30))
            ]
            
            # Заполняем поля данными
            fields[0][1].insert(0, client_data[2])  # last_name
            fields[1][1].insert(0, client_data[1])  # first_name
            fields[2][1].insert(0, client_data[3])  # phone
            fields[3][1].insert(0, client_data[4] or '')  # email
            
            # Размещение полей
            for i, (label, widget) in enumerate(fields):
                tk.Label(dialog, text=label).grid(row=i, column=0, sticky='w', padx=10, pady=10)
                widget.grid(row=i, column=1, padx=10, pady=10, sticky='ew')
            
            # Кнопки
            button_frame = tk.Frame(dialog)
            button_frame.grid(row=len(fields), column=0, columnspan=2, pady=20)
            
            def save_changes():
                try:
                    cursor = self.db_connection.cursor()
                    
                    cursor.execute("""
                        UPDATE clients SET
                            first_name = %s,
                            last_name = %s,
                            phone = %s,
                            email = %s,
                            updated_at = CURRENT_TIMESTAMP
                        WHERE client_id = %s
                    """, (
                        fields[1][1].get(),
                        fields[0][1].get(),
                        fields[2][1].get(),
                        fields[3][1].get() or None,
                        client_id
                    ))
                    
                    self.db_connection.commit()
                    cursor.close()
                    
                    messagebox.showinfo("Успех", "Изменения сохранены!")
                    self.load_clients()
                    dialog.destroy()
                    
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Не удалось сохранить изменения:\n{str(e)}")
            
            ttk.Button(button_frame, text="Сохранить", command=save_changes).pack(side=tk.LEFT, padx=10)
            ttk.Button(button_frame, text="Отмена", command=dialog.destroy).pack(side=tk.LEFT, padx=10)
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить данные клиента:\n{str(e)}")
    
    def edit_agent_dialog(self):
        """Диалог редактирования агента"""
        selection = self.tree_agents.selection()
        if not selection:
            messagebox.showwarning("Внимание", "Выберите агента для редактирования")
            return
        
        item = self.tree_agents.item(selection[0])
        agent_id = item['values'][0]
        
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT * FROM agents WHERE agent_id = %s
            """, (agent_id,))
            
            agent_data = cursor.fetchone()
            cursor.close()
            
            if not agent_data:
                messagebox.showerror("Ошибка", "Агент не найден")
                return
            
            dialog = tk.Toplevel(self.root)
            dialog.title(f"Редактирование агента #{agent_id}")
            dialog.geometry("400x400")
            dialog.transient(self.root)
            dialog.grab_set()
            
            # Поля формы
            fields = [
                ("Фамилия:", tk.Entry(dialog, width=30)),
                ("Имя:", tk.Entry(dialog, width=30)),
                ("Телефон:", tk.Entry(dialog, width=30)),
                ("Email:", tk.Entry(dialog, width=30)),
                ("Лицензия:", tk.Entry(dialog, width=30)),
                ("Комиссия %:", tk.Entry(dialog, width=30))
            ]
            
            # Активность
            tk.Label(dialog, text="Активен:").grid(row=len(fields), column=0, sticky='w', padx=10, pady=10)
            is_active_var = tk.BooleanVar(value=agent_data[8])
            ttk.Checkbutton(dialog, variable=is_active_var).grid(row=len(fields), column=1, sticky='w', padx=10, pady=10)
            
            # Заполняем поля данными
            fields[0][1].insert(0, agent_data[2])  # last_name
            fields[1][1].insert(0, agent_data[1])  # first_name
            fields[2][1].insert(0, agent_data[3])  # phone
            fields[3][1].insert(0, agent_data[4])  # email
            fields[4][1].insert(0, agent_data[5] or '')  # license_number
            fields[5][1].insert(0, str(agent_data[7]))  # commission_rate
            
            # Размещение полей
            for i, (label, widget) in enumerate(fields):
                tk.Label(dialog, text=label).grid(row=i, column=0, sticky='w', padx=10, pady=10)
                widget.grid(row=i, column=1, padx=10, pady=10, sticky='ew')
            
            # Кнопки
            button_frame = tk.Frame(dialog)
            button_frame.grid(row=len(fields)+1, column=0, columnspan=2, pady=20)
            
            def save_changes():
                try:
                    cursor = self.db_connection.cursor()
                    
                    cursor.execute("""
                        UPDATE agents SET
                            first_name = %s,
                            last_name = %s,
                            phone = %s,
                            email = %s,
                            license_number = %s,
                            commission_rate = %s,
                            is_active = %s
                        WHERE agent_id = %s
                    """, (
                        fields[1][1].get(),
                        fields[0][1].get(),
                        fields[2][1].get(),
                        fields[3][1].get(),
                        fields[4][1].get() or None,
                        float(fields[5][1].get() or 2.5),
                        is_active_var.get(),
                        agent_id
                    ))
                    
                    self.db_connection.commit()
                    cursor.close()
                    
                    messagebox.showinfo("Успех", "Изменения сохранены!")
                    self.load_agents()
                    dialog.destroy()
                    
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Не удалось сохранить изменения:\n{str(e)}")
            
            ttk.Button(button_frame, text="Сохранить", command=save_changes).pack(side=tk.LEFT, padx=10)
            ttk.Button(button_frame, text="Отмена", command=dialog.destroy).pack(side=tk.LEFT, padx=10)
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить данные агента:\n{str(e)}")
    
    def edit_viewing_dialog(self):
        """Диалог редактирования просмотра"""
        selection = self.tree_viewings.selection()
        if not selection:
            messagebox.showwarning("Внимание", "Выберите просмотр для редактирования")
            return
        
        item = self.tree_viewings.item(selection[0])
        viewing_id = item['values'][0]
        
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT * FROM voz WHERE viewing_id = %s
            """, (viewing_id,))
            
            viewing_data = cursor.fetchone()
            
            # Получаем списки для выпадающих списков
            cursor.execute("SELECT property_id, address FROM properties")
            properties = cursor.fetchall()
            
            cursor.execute("SELECT client_id, first_name || ' ' || last_name FROM clients ORDER BY last_name")
            clients = cursor.fetchall()
            
            cursor.execute("SELECT agent_id, first_name || ' ' || last_name FROM agents WHERE is_active = TRUE")
            agents = cursor.fetchall()
            
            cursor.close()
            
            if not viewing_data:
                messagebox.showerror("Ошибка", "Просмотр не найден")
                return
            
            dialog = tk.Toplevel(self.root)
            dialog.title(f"Редактирование просмотра #{viewing_id}")
            dialog.geometry("400x400")
            dialog.transient(self.root)
            dialog.grab_set()
            
            # Поля формы
            fields = [
                ("Объект:", ttk.Combobox(dialog, values=[f"{p[0]} - {p[1][:50]}..." for p in properties], width=40)),
                ("Клиент:", ttk.Combobox(dialog, values=[f"{c[0]} - {c[1]}" for c in clients], width=40)),
                ("Агент:", ttk.Combobox(dialog, values=[f"{a[0]} - {a[1]}" for a in agents], width=40)),
                ("Дата:", tk.Entry(dialog, width=40)),
                ("Время:", ttk.Combobox(dialog, values=[
                    "09:00", "10:00", "11:00", "12:00", "13:00", 
                    "14:00", "15:00", "16:00", "17:00", "18:00"
                ], width=37)),
                ("Статус:", ttk.Combobox(dialog, values=['scheduled', 'completed', 'cancelled', 'no_show'], width=37))
            ]
            
            # Находим текущие значения для выпадающих списков
            property_text = ""
            for prop in properties:
                if prop[0] == viewing_data[1]:
                    property_text = f"{prop[0]} - {prop[1][:50]}..."
                    break
            
            client_text = ""
            for client in clients:
                if client[0] == viewing_data[2]:
                    client_text = f"{client[0]} - {client[1]}"
                    break
            
            agent_text = ""
            if viewing_data[3]:
                for agent in agents:
                    if agent[0] == viewing_data[3]:
                        agent_text = f"{agent[0]} - {agent[1]}"
                        break
            
            # Устанавливаем значения
            fields[0][1].set(property_text)
            fields[1][1].set(client_text)
            fields[2][1].set(agent_text)
            fields[3][1].insert(0, str(viewing_data[4]))
            fields[4][1].set(str(viewing_data[5]))
            fields[5][1].set(viewing_data[6])
            
            # Рейтинг и отзыв
            tk.Label(dialog, text="Рейтинг (1-5):").grid(row=6, column=0, sticky='w', padx=10, pady=10)
            rating_var = tk.StringVar(value=str(viewing_data[9] or ''))
            ttk.Combobox(dialog, textvariable=rating_var, values=['1', '2', '3', '4', '5'], width=10).grid(row=6, column=1, sticky='w', padx=10, pady=10)
            
            tk.Label(dialog, text="Отзыв клиента:").grid(row=7, column=0, sticky='nw', padx=10, pady=10)
            feedback_text = scrolledtext.ScrolledText(dialog, width=40, height=4)
            feedback_text.grid(row=7, column=1, padx=10, pady=10)
            feedback_text.insert(1.0, viewing_data[7] or '')
            
            # Размещение полей
            for i, (label, widget) in enumerate(fields):
                tk.Label(dialog, text=label).grid(row=i, column=0, sticky='w', padx=10, pady=10)
                widget.grid(row=i, column=1, padx=10, pady=10, sticky='ew')
            
            # Кнопки
            button_frame = tk.Frame(dialog)
            button_frame.grid(row=8, column=0, columnspan=2, pady=20)
            
            def save_changes():
                try:
                    property_id = int(fields[0][1].get().split(' - ')[0])
                    client_id = int(fields[1][1].get().split(' - ')[0])
                    agent_id = int(fields[2][1].get().split(' - ')[0]) if fields[2][1].get() else None
                    rating = int(rating_var.get()) if rating_var.get() else None
                    
                    cursor = self.db_connection.cursor()
                    
                    cursor.execute("""
                        UPDATE voz SET
                            property_id = %s,
                            client_id = %s,
                            agent_id = %s,
                            viewing_date = %s,
                            viewing_time = %s,
                            status = %s,
                            client_feedback = %s,
                            rating = %s,
                            updated_at = CURRENT_TIMESTAMP
                        WHERE viewing_id = %s
                    """, (
                        property_id,
                        client_id,
                        agent_id,
                        fields[3][1].get(),
                        fields[4][1].get(),
                        fields[5][1].get(),
                        feedback_text.get(1.0, tk.END).strip(),
                        rating,
                        viewing_id
                    ))
                    
                    self.db_connection.commit()
                    cursor.close()
                    
                    messagebox.showinfo("Успех", "Изменения сохранены!")
                    self.load_viewings('all')
                    dialog.destroy()
                    
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Не удалось сохранить изменения:\n{str(e)}")
            
            ttk.Button(button_frame, text="Сохранить", command=save_changes).pack(side=tk.LEFT, padx=10)
            ttk.Button(button_frame, text="Отмена", command=dialog.destroy).pack(side=tk.LEFT, padx=10)
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить данные просмотра:\n{str(e)}")
    
    def edit_deal_dialog(self):
        """Диалог редактирования сделки"""
        selection = self.tree_deals.selection()
        if not selection:
            messagebox.showwarning("Внимание", "Выберите сделку для редактирования")
            return
        
        item = self.tree_deals.item(selection[0])
        deal_id = item['values'][0]
        
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT d.*, p.address,
                       CONCAT(b.first_name, ' ', b.last_name) as buyer_name,
                       CONCAT(s.first_name, ' ', s.last_name) as seller_name,
                       CONCAT(a.first_name, ' ', a.last_name) as agent_name
                FROM deals d
                JOIN properties p ON d.property_id = p.property_id
                JOIN clients b ON d.buyer_client_id = b.client_id
                JOIN clients s ON d.seller_client_id = s.client_id
                JOIN agents a ON d.agent_id = a.agent_id
                WHERE d.deal_id = %s
            """, (deal_id,))
            
            deal_data = cursor.fetchone()
            
            cursor.execute("SELECT agent_id, first_name || ' ' || last_name FROM agents WHERE is_active = TRUE")
            agents = cursor.fetchall()
            
            cursor.close()
            
            if not deal_data:
                messagebox.showerror("Ошибка", "Сделка не найден")
                return
            
            dialog = tk.Toplevel(self.root)
            dialog.title(f"Редактирование сделки #{deal_id}")
            dialog.geometry("500x400")
            dialog.transient(self.root)
            dialog.grab_set()
            
            # Информация о сделке (только для чтения)
            tk.Label(dialog, text="Объект:").grid(row=0, column=0, sticky='w', padx=10, pady=10)
            tk.Label(dialog, text=deal_data[11][:60] + "...").grid(row=0, column=1, sticky='w', padx=10, pady=10)
            
            tk.Label(dialog, text="Покупатель:").grid(row=1, column=0, sticky='w', padx=10, pady=10)
            tk.Label(dialog, text=deal_data[12]).grid(row=1, column=1, sticky='w', padx=10, pady=10)
            
            tk.Label(dialog, text="Продавец:").grid(row=2, column=0, sticky='w', padx=10, pady=10)
            tk.Label(dialog, text=deal_data[13]).grid(row=2, column=1, sticky='w', padx=10, pady=10)
            
            # Поля для редактирования
            tk.Label(dialog, text="Агент:").grid(row=3, column=0, sticky='w', padx=10, pady=10)
            agent_var = tk.StringVar(value=f"{deal_data[5]} - {deal_data[14]}")
            agent_combo = ttk.Combobox(dialog, textvariable=agent_var, 
                                      values=[f"{a[0]} - {a[1]}" for a in agents], 
                                      width=40)
            agent_combo.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
            
            tk.Label(dialog, text="Финальная цена (₽):").grid(row=4, column=0, sticky='w', padx=10, pady=10)
            price_var = tk.StringVar(value=str(deal_data[7]))
            tk.Entry(dialog, textvariable=price_var, width=30).grid(row=4, column=1, sticky='w', padx=10, pady=10)
            
            tk.Label(dialog, text="Комиссия (₽):").grid(row=5, column=0, sticky='w', padx=10, pady=10)
            commission_var = tk.StringVar(value=str(deal_data[8]))
            tk.Entry(dialog, textvariable=commission_var, width=30).grid(row=5, column=1, sticky='w', padx=10, pady=10)
            
            tk.Label(dialog, text="Тип сделки:").grid(row=6, column=0, sticky='w', padx=10, pady=10)
            type_var = tk.StringVar(value=deal_data[9])
            ttk.Combobox(dialog, textvariable=type_var, 
                        values=['sale', 'rent'], width=15).grid(row=6, column=1, sticky='w', padx=10, pady=10)
            
            tk.Label(dialog, text="Номер договора:").grid(row=7, column=0, sticky='w', padx=10, pady=10)
            contract_var = tk.StringVar(value=deal_data[10] or '')
            tk.Entry(dialog, textvariable=contract_var, width=30).grid(row=7, column=1, sticky='w', padx=10, pady=10)
            
            tk.Label(dialog, text="Статус:").grid(row=8, column=0, sticky='w', padx=10, pady=10)
            status_var = tk.StringVar(value=deal_data[11])
            ttk.Combobox(dialog, textvariable=status_var, 
                        values=['in_progress', 'completed', 'cancelled'], width=15).grid(row=8, column=1, sticky='w', padx=10, pady=10)
            
            # Кнопки
            button_frame = tk.Frame(dialog)
            button_frame.grid(row=9, column=0, columnspan=2, pady=20)
            
            def save_changes():
                try:
                    agent_id = int(agent_var.get().split(' - ')[0])
                    
                    cursor = self.db_connection.cursor()
                    cursor.execute("""
                        UPDATE deals SET
                            agent_id = %s,
                            final_price = %s,
                            commission = %s,
                            deal_type = %s,
                            contract_number = %s,
                            status = %s
                        WHERE deal_id = %s
                    """, (
                        agent_id,
                        float(price_var.get()),
                        float(commission_var.get()),
                        type_var.get(),
                        contract_var.get() or None,
                        status_var.get(),
                        deal_id
                    ))
                    
                    self.db_connection.commit()
                    cursor.close()
                    
                    messagebox.showinfo("Успех", "Изменения сохранены!")
                    self.load_deals()
                    dialog.destroy()
                    
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Не удалось сохранить изменения:\n{str(e)}")
            
            ttk.Button(button_frame, text="Сохранить", command=save_changes).pack(side=tk.LEFT, padx=10)
            ttk.Button(button_frame, text="Отмена", command=dialog.destroy).pack(side=tk.LEFT, padx=10)
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить данные сделки:\n{str(e)}")
    
    # ========== ДИАЛОГ ДЛЯ ПЛАТЕЖЕЙ ==========
    
    def add_payment_dialog(self):
        """Диалог добавления платежа"""
        selection = self.tree_deals.selection()
        if not selection:
            messagebox.showwarning("Внимание", "Выберите сделку для добавления платежа")
            return
        
        item = self.tree_deals.item(selection[0])
        deal_id = item['values'][0]
        
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Добавить платеж к сделке #{deal_id}")
        dialog.geometry("400x350")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Поля формы
        tk.Label(dialog, text="Сумма (₽) *:").grid(row=0, column=0, sticky='w', padx=10, pady=10)
        amount_var = tk.StringVar()
        tk.Entry(dialog, textvariable=amount_var, width=30).grid(row=0, column=1, sticky='w', padx=10, pady=10)
        
        tk.Label(dialog, text="Дата платежа:").grid(row=1, column=0, sticky='w', padx=10, pady=10)
        date_var = tk.StringVar(value=date.today().strftime("%Y-%m-%d"))
        tk.Entry(dialog, textvariable=date_var, width=30).grid(row=1, column=1, sticky='w', padx=10, pady=10)
        
        tk.Label(dialog, text="Тип платежа:").grid(row=2, column=0, sticky='w', padx=10, pady=10)
        type_var = tk.StringVar(value='deposit')
        ttk.Combobox(dialog, textvariable=type_var, 
                    values=['deposit', 'installment', 'final', 'commission'], width=15).grid(row=2, column=1, sticky='w', padx=10, pady=10)
        
        tk.Label(dialog, text="Метод оплаты:").grid(row=3, column=0, sticky='w', padx=10, pady=10)
        method_var = tk.StringVar(value='bank_transfer')
        ttk.Combobox(dialog, textvariable=method_var, 
                    values=['cash', 'bank_transfer', 'card', 'check'], width=15).grid(row=3, column=1, sticky='w', padx=10, pady=10)
        
        tk.Label(dialog, text="Статус:").grid(row=4, column=0, sticky='w', padx=10, pady=10)
        status_var = tk.StringVar(value='pending')
        ttk.Combobox(dialog, textvariable=status_var, 
                    values=['pending', 'completed', 'failed'], width=15).grid(row=4, column=1, sticky='w', padx=10, pady=10)
        
        tk.Label(dialog, text="Примечания:").grid(row=5, column=0, sticky='nw', padx=10, pady=10)
        notes_text = scrolledtext.ScrolledText(dialog, width=30, height=4)
        notes_text.grid(row=5, column=1, padx=10, pady=10)
        
        # Кнопки
        button_frame = tk.Frame(dialog)
        button_frame.grid(row=6, column=0, columnspan=2, pady=20)
        
        def save_payment():
            try:
                if not amount_var.get():
                    messagebox.showerror("Ошибка", "Введите сумму платежа")
                    return
                
                cursor = self.db_connection.cursor()
                cursor.execute("""
                    INSERT INTO payments 
                    (deal_id, amount, payment_date, payment_type, 
                     payment_method, status, notes)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (
                    deal_id,
                    float(amount_var.get()),
                    date_var.get(),
                    type_var.get(),
                    method_var.get(),
                    status_var.get(),
                    notes_text.get(1.0, tk.END).strip()
                ))
                
                self.db_connection.commit()
                cursor.close()
                
                messagebox.showinfo("Успех", "Платеж добавлен!")
                self.show_deal_payments(None)  # Обновляем таблицу платежей
                dialog.destroy()
                
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось добавить платеж:\n{str(e)}")
        
        ttk.Button(button_frame, text="Сохранить", command=save_payment).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="Отмена", command=dialog.destroy).pack(side=tk.LEFT, padx=10)
    
    def edit_payment_dialog(self):
        """Диалог редактирования платежа"""
        selection = self.tree_payments.selection()
        if not selection:
            messagebox.showwarning("Внимание", "Выберите платеж для редактирования")
            return
        
        item = self.tree_payments.item(selection[0])
        payment_id = item['values'][0]
        
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT * FROM payments WHERE payment_id = %s
            """, (payment_id,))
            
            payment_data = cursor.fetchone()
            cursor.close()
            
            if not payment_data:
                messagebox.showerror("Ошибка", "Платеж не найден")
                return
            
            dialog = tk.Toplevel(self.root)
            dialog.title(f"Редактирование платежа #{payment_id}")
            dialog.geometry("400x350")
            dialog.transient(self.root)
            dialog.grab_set()
            
            # Поля формы
            tk.Label(dialog, text="Сумма (₽):").grid(row=0, column=0, sticky='w', padx=10, pady=10)
            amount_var = tk.StringVar(value=str(payment_data[2]))
            tk.Entry(dialog, textvariable=amount_var, width=30).grid(row=0, column=1, sticky='w', padx=10, pady=10)
            
            tk.Label(dialog, text="Дата платежа:").grid(row=1, column=0, sticky='w', padx=10, pady=10)
            date_var = tk.StringVar(value=str(payment_data[3]))
            tk.Entry(dialog, textvariable=date_var, width=30).grid(row=1, column=1, sticky='w', padx=10, pady=10)
            
            tk.Label(dialog, text="Тип платежа:").grid(row=2, column=0, sticky='w', padx=10, pady=10)
            type_var = tk.StringVar(value=payment_data[4])
            ttk.Combobox(dialog, textvariable=type_var, 
                        values=['deposit', 'installment', 'final', 'commission'], width=15).grid(row=2, column=1, sticky='w', padx=10, pady=10)
            
            tk.Label(dialog, text="Метод оплаты:").grid(row=3, column=0, sticky='w', padx=10, pady=10)
            method_var = tk.StringVar(value=payment_data[5])
            ttk.Combobox(dialog, textvariable=method_var, 
                        values=['cash', 'bank_transfer', 'card', 'check'], width=15).grid(row=3, column=1, sticky='w', padx=10, pady=10)
            
            tk.Label(dialog, text="Статус:").grid(row=4, column=0, sticky='w', padx=10, pady=10)
            status_var = tk.StringVar(value=payment_data[6])
            ttk.Combobox(dialog, textvariable=status_var, 
                        values=['pending', 'completed', 'failed'], width=15).grid(row=4, column=1, sticky='w', padx=10, pady=10)
            
            tk.Label(dialog, text="Примечания:").grid(row=5, column=0, sticky='nw', padx=10, pady=10)
            notes_text = scrolledtext.ScrolledText(dialog, width=30, height=4)
            notes_text.grid(row=5, column=1, padx=10, pady=10)
            notes_text.insert(1.0, payment_data[7] or '')
            
            # Кнопки
            button_frame = tk.Frame(dialog)
            button_frame.grid(row=6, column=0, columnspan=2, pady=20)
            
            def save_changes():
                try:
                    cursor = self.db_connection.cursor()
                    cursor.execute("""
                        UPDATE payments SET
                            amount = %s,
                            payment_date = %s,
                            payment_type = %s,
                            payment_method = %s,
                            status = %s,
                            notes = %s
                        WHERE payment_id = %s
                    """, (
                        float(amount_var.get()),
                        date_var.get(),
                        type_var.get(),
                        method_var.get(),
                        status_var.get(),
                        notes_text.get(1.0, tk.END).strip(),
                        payment_id
                    ))
                    
                    self.db_connection.commit()
                    cursor.close()
                    
                    messagebox.showinfo("Успех", "Изменения сохранены!")
                    
                    # Обновляем таблицу платежей
                    deal_selection = self.tree_deals.selection()
                    if deal_selection:
                        self.show_deal_payments(None)
                    
                    dialog.destroy()
                    
                except Exception as e:
                    messagebox.showerror("Ошибка", f"Не удалось сохранить изменения:\n{str(e)}")
            
            ttk.Button(button_frame, text="Сохранить", command=save_changes).pack(side=tk.LEFT, padx=10)
            ttk.Button(button_frame, text="Отмена", command=dialog.destroy).pack(side=tk.LEFT, padx=10)
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить данные платежа:\n{str(e)}")
    
    def delete_payment(self):
        """Удаление платежа"""
        selection = self.tree_payments.selection()
        if not selection:
            messagebox.showwarning("Внимание", "Выберите платеж для удаления")
            return
        
        if messagebox.askyesno("Подтверждение", "Удалить выбранный платеж?"):
            payment_id = self.tree_payments.item(selection[0])['values'][0]
            
            try:
                cursor = self.db_connection.cursor()
                cursor.execute("DELETE FROM payments WHERE payment_id = %s", (payment_id,))
                self.db_connection.commit()
                cursor.close()
                
                # Обновляем таблицу платежей
                deal_selection = self.tree_deals.selection()
                if deal_selection:
                    self.show_deal_payments(None)
                
                messagebox.showinfo("Успех", "Платеж удален")
                
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось удалить платеж:\n{str(e)}")
    
    # ========== ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ ==========
    
    def create_deal_from_property(self):
        """Создать сделку из объекта"""
        selection = self.tree_properties.selection()
        if not selection:
            messagebox.showwarning("Внимание", "Выберите объект для создания сделки")
            return
        
        item = self.tree_properties.item(selection[0])
        property_id = item['values'][0]
        
        self.add_deal_dialog(property_id=property_id)
    
    def create_deal_from_viewing(self):
        """Создать сделку из просмотра"""
        selection = self.tree_viewings.selection()
        if not selection:
            messagebox.showwarning("Внимание", "Выберите просмотр для создания сделки")
            return
        
        item = self.tree_viewings.item(selection[0])
        viewing_id = item['values'][0]
        
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT property_id, client_id FROM voz WHERE viewing_id = %s
            """, (viewing_id,))
            
            viewing_data = cursor.fetchone()
            cursor.close()
            
            if viewing_data:
                self.add_deal_dialog(property_id=viewing_data[0], client_id=viewing_data[1])
            else:
                messagebox.showerror("Ошибка", "Не удалось получить данные просмотра")
                
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить данные:\n{str(e)}")
    
    def change_property_status(self):
        """Изменить статус объекта"""
        selection = self.tree_properties.selection()
        if not selection:
            messagebox.showwarning("Внимание", "Выберите объект")
            return
        
        item = self.tree_properties.item(selection[0])
        property_id = item['values'][0]
        current_status = item['values'][8]
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Изменить статус объекта")
        dialog.geometry("300x150")
        dialog.transient(self.root)
        dialog.grab_set()
        
        tk.Label(dialog, text=f"Объект #{property_id}").pack(pady=10)
        tk.Label(dialog, text=f"Текущий статус: {current_status}").pack(pady=5)
        
        tk.Label(dialog, text="Новый статус:").pack(pady=5)
        status_var = tk.StringVar(value=current_status)
        status_combo = ttk.Combobox(dialog, textvariable=status_var, 
                                   values=['available', 'reserved', 'sold', 'rented', 'withdrawn'])
        status_combo.pack(pady=5)
        
        def save_status():
            try:
                cursor = self.db_connection.cursor()
                cursor.execute("""
                    UPDATE properties 
                    SET status = %s, updated_at = CURRENT_TIMESTAMP
                    WHERE property_id = %s
                """, (status_var.get(), property_id))
                
                self.db_connection.commit()
                cursor.close()
                
                messagebox.showinfo("Успех", "Статус изменен")
                self.load_properties()
                dialog.destroy()
                
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось изменить статус:\n{str(e)}")
        
        ttk.Button(dialog, text="Сохранить", command=save_status).pack(pady=10)
    
    def change_deal_status(self):
        """Изменить статус сделки"""
        selection = self.tree_deals.selection()
        if not selection:
            messagebox.showwarning("Внимание", "Выберите сделку")
            return
        
        item = self.tree_deals.item(selection[0])
        deal_id = item['values'][0]
        current_status = item['values'][8]
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Изменить статус сделки")
        dialog.geometry("300x150")
        dialog.transient(self.root)
        dialog.grab_set()
        
        tk.Label(dialog, text=f"Сделка #{deal_id}").pack(pady=10)
        tk.Label(dialog, text=f"Текущий статус: {current_status}").pack(pady=5)
        
        tk.Label(dialog, text="Новый статус:").pack(pady=5)
        status_var = tk.StringVar(value=current_status)
        status_combo = ttk.Combobox(dialog, textvariable=status_var, 
                                   values=['in_progress', 'completed', 'cancelled'])
        status_combo.pack(pady=5)
        
        def save_status():
            try:
                cursor = self.db_connection.cursor()
                cursor.execute("""
                    UPDATE deals 
                    SET status = %s
                    WHERE deal_id = %s
                """, (status_var.get(), deal_id))
                
                self.db_connection.commit()
                cursor.close()
                
                messagebox.showinfo("Успех", "Статус изменен")
                self.load_deals()
                dialog.destroy()
                
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось изменить статус:\n{str(e)}")
        
        ttk.Button(dialog, text="Сохранить", command=save_status).pack(pady=10)
    
    def show_client_viewings(self):
        """Показать историю просмотров клиента"""
        selection = self.tree_clients.selection()
        if not selection:
            messagebox.showwarning("Внимание", "Выберите клиента")
            return
        
        item = self.tree_clients.item(selection[0])
        client_id = item['values'][0]
        client_name = f"{item['values'][2]} {item['values'][1]}"
        
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT v.viewing_date, v.viewing_time, p.address, 
                       v.status, v.rating, v.client_feedback
                FROM voz v
                JOIN properties p ON v.property_id = p.property_id
                WHERE v.client_id = %s
                ORDER BY v.viewing_date DESC
            """, (client_id,))
            
            viewings = cursor.fetchall()
            cursor.close()
            
            if viewings:
                history = f"ИСТОРИЯ ПРОСМОТРОВ: {client_name}\n"
                history += "=" * 50 + "\n\n"
                
                for viewing in viewings:
                    rating = viewing[4] if viewing[4] else '—'
                    history += f"Дата: {viewing[0]} {viewing[1]}\n"
                    history += f"Объект: {viewing[2][:60]}...\n"
                    history += f"Статус: {viewing[3]} | Оценка: {rating}/5\n"
                    
                    if viewing[5]:
                        history += f"Отзыв: {viewing[5][:100]}...\n"
                    
                    history += "-" * 50 + "\n"
                
                # Показать в отдельном окне
                text_window = tk.Toplevel(self.root)
                text_window.title(f"История просмотров: {client_name}")
                text_window.geometry("600x400")
                
                text_widget = scrolledtext.ScrolledText(text_window, wrap=tk.WORD, width=80, height=25)
                text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
                text_widget.insert(1.0, history)
                text_widget.config(state=tk.DISABLED)
                
            else:
                messagebox.showinfo("История", f"У клиента {client_name} нет истории просмотров")
                
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить историю:\n{str(e)}")
    
    def show_client_deals(self):
        """Показать историю сделок клиента"""
        selection = self.tree_clients.selection()
        if not selection:
            messagebox.showwarning("Внимание", "Выберите клиента")
            return
        
        item = self.tree_clients.item(selection[0])
        client_id = item['values'][0]
        client_name = f"{item['values'][2]} {item['values'][1]}"
        
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT d.deal_id, d.deal_date, p.address, 
                       d.final_price, d.commission, d.status,
                       CASE 
                           WHEN d.buyer_client_id = %s THEN 'Покупатель'
                           WHEN d.seller_client_id = %s THEN 'Продавец'
                       END as role
                FROM deals d
                JOIN properties p ON d.property_id = p.property_id
                WHERE d.buyer_client_id = %s OR d.seller_client_id = %s
                ORDER BY d.deal_date DESC
            """, (client_id, client_id, client_id, client_id))
            
            deals = cursor.fetchall()
            cursor.close()
            
            if deals:
                history = f"ИСТОРИЯ СДЕЛОК: {client_name}\n"
                history += "=" * 60 + "\n\n"
                
                for deal in deals:
                    history += f"Сделка #{deal[0]} ({deal[6]})\n"
                    history += f"Дата: {deal[1]}\n"
                    history += f"Объект: {deal[2][:60]}...\n"
                    history += f"Сумма: {deal[3]:,.0f} ₽ | Комиссия: {deal[4]:,.0f} ₽\n"
                    history += f"Статус: {deal[5]}\n"
                    history += "-" * 40 + "\n"
                
                # Показать в отдельном окне
                text_window = tk.Toplevel(self.root)
                text_window.title(f"История сделок: {client_name}")
                text_window.geometry("600x400")
                
                text_widget = scrolledtext.ScrolledText(text_window, wrap=tk.WORD, width=80, height=25)
                text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
                text_widget.insert(1.0, history)
                text_widget.config(state=tk.DISABLED)
                
            else:
                messagebox.showinfo("История", f"У клиента {client_name} нет истории сделок")
                
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить историю:\n{str(e)}")
    
    # ========== ОТЧЕТЫ ==========
    
    def generate_monthly_stats(self):
        """Генерация месячной статистики"""
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT 
                    TO_CHAR(deal_date, 'YYYY-MM') as month,
                    COUNT(*) as deals_count,
                    SUM(final_price) as total_sales,
                    SUM(commission) as total_commission
                FROM deals 
                WHERE status = 'completed'
                GROUP BY TO_CHAR(deal_date, 'YYYY-MM')
                ORDER BY month DESC
                LIMIT 12
            """)
            
            stats = cursor.fetchall()
            cursor.close()
            
            report = "МЕСЯЧНАЯ СТАТИСТИКА ПРОДАЖ\n"
            report += "=" * 60 + "\n\n"
            
            for stat in stats:
                report += f"Месяц: {stat[0]}\n"
                report += f"  Сделок: {stat[1]}\n"
                report += f"  Общая сумма: {stat[2]:,.0f} ₽\n"
                report += f"  Комиссия: {stat[3]:,.0f} ₽\n"
                report += "-" * 40 + "\n"
            
            self.show_report(report)
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сгенерировать отчет:\n{str(e)}")
    
    def generate_top_agents(self):
        """Генерация отчета по топ агентам"""
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT 
                    CONCAT(a.first_name, ' ', a.last_name) as agent_name,
                    COUNT(DISTINCT d.deal_id) as deals_count,
                    COALESCE(SUM(d.commission), 0) as total_commission,
                    AVG(v.rating) as avg_rating
                FROM agents a
                LEFT JOIN deals d ON a.agent_id = d.agent_id AND d.status = 'completed'
                LEFT JOIN voz v ON a.agent_id = v.agent_id AND v.status = 'completed'
                WHERE a.is_active = TRUE
                GROUP BY a.agent_id, a.first_name, a.last_name
                ORDER BY total_commission DESC
                LIMIT 10
            """)
            
            agents = cursor.fetchall()
            cursor.close()
            
            report = "ТОП АГЕНТОВ ПО КОМИССИИ\n"
            report += "=" * 70 + "\n\n"
            
            for i, agent in enumerate(agents, 1):
                rating = f"{agent[3]:.1f}" if agent[3] else "Н/Д"
                report += f"{i}. {agent[0]}\n"
                report += f"   Сделок: {agent[1]} | Комиссия: {agent[2]:,.0f} ₽ | Рейтинг: {rating}/5\n\n"
            
            self.show_report(report)
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сгенерировать отчет:\n{str(e)}")
    
    def generate_popular_districts(self):
        """Генерация отчета по популярным районам"""
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT 
                    p.district,
                    COUNT(*) as properties_count,
                    AVG(p.price) as avg_price,
                    COUNT(v.viewing_id) as viewings_count
                FROM properties p
                LEFT JOIN voz v ON p.property_id = v.property_id
                WHERE p.district IS NOT NULL
                GROUP BY p.district
                ORDER BY viewings_count DESC
            """)
            
            districts = cursor.fetchall()
            cursor.close()
            
            report = "ПОПУЛЯРНОСТЬ РАЙОНОВ\n"
            report += "=" * 70 + "\n\n"
            
            for district in districts:
                report += f"Район: {district[0] or 'Не указан'}\n"
                report += f"  Объектов: {district[1]}\n"
                report += f"  Средняя цена: {district[2]:,.0f} ₽\n"
                report += f"  Просмотров: {district[3]}\n"
                report += "-" * 40 + "\n"
            
            self.show_report(report)
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сгенерировать отчет:\n{str(e)}")
    
    def generate_avg_prices(self):
        """Генерация отчета по средним ценам"""
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT 
                    property_type,
                    transaction_type,
                    COUNT(*) as count,
                    AVG(price) as avg_price,
                    MIN(price) as min_price,
                    MAX(price) as max_price
                FROM properties
                WHERE status IN ('available', 'reserved')
                GROUP BY property_type, transaction_type
                ORDER BY property_type, transaction_type
            """)
            
            prices = cursor.fetchall()
            cursor.close()
            
            report = "СРЕДНИЕ ЦЕНЫ ПО ТИПАМ НЕДВИЖИМОСТИ\n"
            report += "=" * 70 + "\n\n"
            
            for price in prices:
                type_name = {
                    'apartment': 'Квартира',
                    'house': 'Дом',
                    'commercial': 'Коммерческая',
                    'land': 'Участок'
                }.get(price[0], price[0])
                
                deal_type = 'Продажа' if price[1] == 'sale' else 'Аренда'
                
                report += f"{type_name} ({deal_type}):\n"
                report += f"  Количество: {price[2]}\n"
                report += f"  Средняя: {price[3]:,.0f} ₽\n"
                report += f"  Минимальная: {price[4]:,.0f} ₽\n"
                report += f"  Максимальная: {price[5]:,.0f} ₽\n"
                report += "-" * 40 + "\n"
            
            self.show_report(report)
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сгенерировать отчет:\n{str(e)}")
    
    def generate_active_clients(self):
        """Генерация отчета по активным клиентам"""
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                SELECT 
                    CONCAT(c.first_name, ' ', c.last_name) as client_name,
                    c.phone,
                    COUNT(DISTINCT v.viewing_id) as viewings_count,
                    COUNT(DISTINCT d.deal_id) as deals_count,
                    MAX(v.viewing_date) as last_viewing
                FROM clients c
                LEFT JOIN voz v ON c.client_id = v.client_id
                LEFT JOIN deals d ON c.client_id = d.buyer_client_id
                GROUP BY c.client_id, c.first_name, c.last_name, c.phone
                HAVING COUNT(DISTINCT v.viewing_id) > 0
                ORDER BY viewings_count DESC
                LIMIT 20
            """)
            
            clients = cursor.fetchall()
            cursor.close()
            
            report = "САМЫЕ АКТИВНЫЕ КЛИЕНТЫ\n"
            report += "=" * 70 + "\n\n"
            
            for i, client in enumerate(clients, 1):
                last_viewing = client[4].strftime('%d.%m.%Y') if client[4] else 'Нет'
                report += f"{i}. {client[0]}\n"
                report += f"   Телефон: {client[1]}\n"
                report += f"   Просмотров: {client[2]} | Сделок: {client[3]} | Последний просмотр: {last_viewing}\n\n"
            
            self.show_report(report)
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сгенерировать отчет:\n{str(e)}")
    
    def generate_financial_report(self):
        """Генерация финансового отчета"""
        try:
            cursor = self.db_connection.cursor()
            
            # Общая статистика
            cursor.execute("""
                SELECT 
                    COUNT(*) as total_deals,
                    SUM(final_price) as total_sales,
                    SUM(commission) as total_commission,
                    AVG(commission) as avg_commission
                FROM deals 
                WHERE status = 'completed'
            """)
            total_stats = cursor.fetchone()
            
            # Статистика по месяцам
            cursor.execute("""
                SELECT 
                    TO_CHAR(deal_date, 'YYYY-MM') as month,
                    COUNT(*) as deals_count,
                    SUM(final_price) as total_sales,
                    SUM(commission) as total_commission
                FROM deals 
                WHERE status = 'completed'
                GROUP BY TO_CHAR(deal_date, 'YYYY-MM')
                ORDER BY month DESC
                LIMIT 6
            """)
            monthly_stats = cursor.fetchall()
            
            # Топ агентов
            cursor.execute("""
                SELECT 
                    CONCAT(a.first_name, ' ', a.last_name) as agent_name,
                    COUNT(*) as deals_count,
                    SUM(d.commission) as total_commission
                FROM deals d
                JOIN agents a ON d.agent_id = a.agent_id
                WHERE d.status = 'completed'
                GROUP BY a.agent_id, a.first_name, a.last_name
                ORDER BY total_commission DESC
                LIMIT 5
            """)
            top_agents = cursor.fetchall()
            
            cursor.close()
            
            report = "ФИНАНСОВЫЙ ОТЧЕТ\n"
            report += "=" * 70 + "\n\n"
            
            report += "ОБЩАЯ СТАТИСТИКА:\n"
            report += "-" * 40 + "\n"
            report += f"Всего завершенных сделок: {total_stats[0] or 0}\n"
            report += f"Общая сумма продаж: {total_stats[1] or 0:,.0f} ₽\n"
            report += f"Общая комиссия: {total_stats[2] or 0:,.0f} ₽\n"
            report += f"Средняя комиссия: {total_stats[3] or 0:,.0f} ₽\n\n"
            
            report += "СТАТИСТИКА ПО МЕСЯЦАМ (последние 6 месяцев):\n"
            report += "-" * 40 + "\n"
            for stat in monthly_stats:
                report += f"{stat[0]}: {stat[1]} сделок, {stat[2]:,.0f} ₽, комиссия: {stat[3]:,.0f} ₽\n"
            report += "\n"
            
            report += "ТОП АГЕНТОВ ПО КОМИССИИ:\n"
            report += "-" * 40 + "\n"
            for i, agent in enumerate(top_agents, 1):
                report += f"{i}. {agent[0]}: {agent[1]} сделок, комиссия: {agent[2]:,.0f} ₽\n"
            
            self.show_report(report)
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сгенерировать отчет:\n{str(e)}")
    
    def show_report(self, content):
        """Показать отчет в текстовом поле"""
        self.report_text.delete(1.0, tk.END)
        self.report_text.insert(1.0, content)
        self.update_status("Отчет сгенерирован")
    
    def save_report(self):
        """Сохранить отчет в файл"""
        content = self.report_text.get(1.0, tk.END)
        if not content.strip():
            messagebox.showwarning("Предупреждение", "Нет данных для сохранения")
            return
        
        from tkinter import filedialog
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                messagebox.showinfo("Успех", f"Отчет сохранен в:\n{filename}")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{str(e)}")
    
    def update_status(self, message, error=False):
        """Обновление статус бара"""
        color = self.colors['warning'] if error else 'black'
        self.status_bar.config(text=message, fg=color)
        self.root.after(5000, lambda: self.status_bar.config(text="Готово", fg='black'))
    
    def on_closing(self):
        """Обработка закрытия приложения"""
        if messagebox.askokcancel("Выход", "Закрыть приложение?"):
            if hasattr(self, 'db_connection'):
                self.db_connection.close()
            self.root.destroy()

def main():
    """Основная функция"""
    root = tk.Tk()
    app = RealEstateApp(root)
    
    # Обработка закрытия окна
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    
    # Центрирование окна
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()

if __name__ == "__main__":
    main()