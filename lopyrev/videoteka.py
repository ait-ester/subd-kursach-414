import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import psycopg2
from psycopg2 import Error
from datetime import date

class AutoSizeTreeview(ttk.Treeview):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sort_column = None
        self.sort_reverse = False
        
    def auto_size_columns(self):
       
        for col in self['columns']:
            self.auto_size_column(col)
    
    def auto_size_column(self, column):
        
        
        min_width = 50
        
       
        self.update_idletasks()
        header_width = self.column(column, 'width')
        
       
        max_width = header_width
        
       
        for item in self.get_children():
            value = self.set(item, column)
            if value:
               
                text_width = len(str(value)) * 8
                max_width = max(max_width, text_width)
        
        
        new_width = max(min_width, min(max_width + 20, 500))  
        self.column(column, width=int(new_width))
    
    def sort_by_column(self, column, reverse):
        # Сортировка по колонке
        
        # Получаем все элементы
        items = [(self.set(item, column), item) for item in self.get_children('')]
        
        # Определяем тип сортировки в зависимости от колонки
        if column == "ID":
            items.sort(key=lambda t: int(t[0]), reverse=reverse)
        elif column == "Год":
            items.sort(key=lambda t: int(t[0]) if t[0].isdigit() else 0, reverse=reverse)
        elif column == "Длит.":
            items.sort(key=lambda t: int(t[0].split()[0]) if t[0] and t[0].split()[0].isdigit() else 0, reverse=reverse)
        elif column == "Рейтинг":
            items.sort(key=lambda t: float(t[0].split('/')[0]) if '/' in t[0] and t[0].split('/')[0].replace('.', '').isdigit() else 0, reverse=reverse)
        else:
            # Для текстовых колонок (Название, Жанры)
            items.sort(key=lambda t: t[0].lower(), reverse=reverse)
        
        # Перемещаем элементы в отсортированном порядке
        for index, (val, item) in enumerate(items):
            self.move(item, '', index)
        
        # Обновляем заголовок с указанием направления сортировки
        self.update_sort_indicator(column, reverse)
    
    def update_sort_indicator(self, column, reverse):
        # Обновление индикатора сортировки в заголовке
    
        for col in self['columns']:
            current_text = self.heading(col)['text']
            if current_text.endswith(' ▲') or current_text.endswith(' ▼'):
                self.heading(col, text=current_text[:-2])
        
        # Добавляем стрелку к текущей колонке
        arrow = ' ▼' if reverse else ' ▲'
        current_text = self.heading(column)['text']
        if not current_text.endswith(arrow):
            self.heading(column, text=current_text + arrow)

class VideoLibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Домашняя видеотека")
        self.root.geometry("1400x800")
        
        # Подключение к базе данных
        self.connection = None
        self.connect_to_db()
        
        # Создание интерфейса
        self.create_widgets()
        
    def connect_to_db(self):
        # Подключение к PostgreSQL
        try:
            self.connection = psycopg2.connect(
                database="gilopsan",  
                user="gilopsan",      
                password="22081921",          
                host="localhost",
                port="5432"
            )
            print("Успешное подключение к базе данных")
        except Error as e:
            messagebox.showerror("Ошибка подключения", f"Не удалось подключиться к БД: {e}")
            self.root.destroy()
    
    def create_widgets(self):
        # Создание элементов интерфейса

        # Главный контейнер
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Левая панель (поиск и фильтры)
        left_frame = ttk.LabelFrame(main_frame, text="Поиск и фильтры", padding="10")
        left_frame.grid(row=0, column=0, sticky=(tk.N, tk.S), padx=(0, 10))
        
        # Поле поиска по названию
        ttk.Label(left_frame, text="Название фильма:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        self.search_title = ttk.Entry(left_frame, width=30)
        self.search_title.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Поиск по актеру
        ttk.Label(left_frame, text="Актер:").grid(row=2, column=0, sticky=tk.W, pady=(0, 5))
        self.search_actor = ttk.Entry(left_frame, width=30)
        self.search_actor.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Фильтр по жанру
        ttk.Label(left_frame, text="Жанр:").grid(row=4, column=0, sticky=tk.W, pady=(0, 5))
        self.genre_var = tk.StringVar()
        self.genre_combo = ttk.Combobox(left_frame, textvariable=self.genre_var, width=28, state="readonly")
        self.genre_combo.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        self.load_genres()
        
        # Фильтр по рейтингу
        ttk.Label(left_frame, text="Минимальный рейтинг:").grid(row=6, column=0, sticky=tk.W, pady=(0, 5))
        self.rating_var = tk.StringVar(value="1")
        rating_combo = ttk.Combobox(left_frame, textvariable=self.rating_var, 
                                    values=[str(i) for i in range(1, 11)], width=5)
        rating_combo.grid(row=7, column=0, sticky=tk.W, pady=(0, 20))
        
        # Кнопки поиска
        ttk.Button(left_frame, text="Найти фильмы", command=self.search_movies).grid(row=8, column=0, pady=(0, 5))
        ttk.Button(left_frame, text="Показать все", command=self.show_all_movies).grid(row=9, column=0, pady=(0, 5))
        ttk.Button(left_frame, text="Статистика", command=self.show_statistics).grid(row=10, column=0, pady=(0, 5))
        
        # Кнопки управления
        ttk.Separator(left_frame, orient='horizontal').grid(row=11, column=0, sticky=(tk.W, tk.E), pady=10)
        ttk.Button(left_frame, text="Добавить фильм", command=self.open_add_movie_window).grid(row=12, column=0, pady=(0, 5))
        ttk.Button(left_frame, text="Добавить актера", command=self.open_add_actor_window).grid(row=13, column=0, pady=(0, 5))
        ttk.Button(left_frame, text="Добавить просмотр", command=self.open_add_viewing_window).grid(row=14, column=0, pady=(0, 5))
        ttk.Button(left_frame, text="Редактировать фильм", command=self.open_edit_movie_window).grid(row=15, column=0, pady=(0, 5))
        ttk.Button(left_frame, text="Удалить фильм", command=self.delete_movie).grid(row=16, column=0, pady=(0, 5))
        ttk.Button(left_frame, text="Автоподбор ширины", command=self.auto_size_columns).grid(row=17, column=0, pady=(20, 0))
        
        # Правая панель (результаты)
        right_frame = ttk.Frame(main_frame)
        right_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Таблица с фильмами
        self.tree = AutoSizeTreeview(right_frame, 
                                     columns=("ID", "Название", "Год", "Длит.", "Рейтинг", "Жанры"), 
                                     show="headings", height=25)
        
        # Настройка колонок с минимальными ширинами
        columns_config = [
            ("ID", 50, 80),
            ("Название", 200, 400),
            ("Год", 60, 80),
            ("Длит.", 70, 100),
            ("Рейтинг", 80, 100),
            ("Жанры", 200, 500)
        ]
        
        for col, min_width, max_width in columns_config:
            self.tree.heading(col, text=col, 
                             command=lambda c=col: self.on_header_click(c))
            self.tree.column(col, width=min_width, minwidth=min_width, stretch=True)
        
        # Полосы прокрутки
        v_scrollbar = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(right_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Размещение элементов
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        v_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        h_scrollbar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        # Информация о выбранном фильме
        info_frame = ttk.LabelFrame(right_frame, text="Подробная информация", padding="10")
        info_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        
        self.info_text = scrolledtext.ScrolledText(info_frame, width=100, height=10, font=("Arial", 10))
        self.info_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Привязка события выбора в таблице
        self.tree.bind('<<TreeviewSelect>>', self.on_movie_select)
        
        # Настройка расширения
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)
        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(0, weight=1)
        right_frame.rowconfigure(2, weight=0)
        info_frame.columnconfigure(0, weight=1)
        info_frame.rowconfigure(0, weight=1)
        
        # Загружаем все фильмы при запуске
        self.show_all_movies()
    
    def on_header_click(self, column):
        
        if self.tree.sort_column == column:
            self.tree.sort_reverse = not self.tree.sort_reverse
        else:
            self.tree.sort_column = column
            self.tree.sort_reverse = False
        
        # Сортируем данные в таблице
        self.tree.sort_by_column(column, self.tree.sort_reverse)
    
    def load_genres(self):
        # Загрузка жанров в выпадающий список
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT genre_name FROM genres ORDER BY genre_name")
            genres = [row[0] for row in cursor.fetchall()]
            self.genre_combo['values'] = ['Все жанры'] + genres
            self.genre_combo.set('Все жанры')
            cursor.close()
        except Error as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить жанры: {e}")
    
    def search_movies(self):
        # Поиск фильмов по критериям
        try:
            cursor = self.connection.cursor()
            
           
            query = """
            SELECT m.id, m.name, m.release_year, m.duration, m.my_rating, 
                   STRING_AGG(DISTINCT g.genre_name, ', ') as genres
            FROM movies m
            LEFT JOIN movie_genres mg ON m.id = mg.movie_id
            LEFT JOIN genres g ON mg.genre_id = g.id
            WHERE 1=1
            """
            
            params = []
            
            # Фильтры
            title = self.search_title.get().strip()
            if title:
                query += " AND LOWER(m.name) LIKE LOWER(%s)"
                params.append(f"%{title}%")
            
            actor = self.search_actor.get().strip()
            if actor:
                query += """
                AND m.id IN (
                    SELECT ma.movie_id 
                    FROM movie_actors ma 
                    JOIN actors a ON ma.actor_id = a.id 
                    WHERE LOWER(a.actor_name) LIKE LOWER(%s)
                )
                """
                params.append(f"%{actor}%")
            
            genre = self.genre_var.get()
            if genre and genre != 'Все жанры':
                query += " AND g.genre_name = %s"
                params.append(genre)
            
            rating = self.rating_var.get()
            if rating:
                query += " AND m.my_rating >= %s"
                params.append(int(rating))
            
            query += " GROUP BY m.id ORDER BY m.my_rating DESC, m.name"
            
            cursor.execute(query, params)
            results = cursor.fetchall()
            cursor.close()
            
            self.display_results(results)
            
        except Error as e:
            messagebox.showerror("Ошибка поиска", f"Ошибка при поиске: {e}")
    
    def show_all_movies(self):
        # Показать все фильмы
        try:
            cursor = self.connection.cursor()
            query = """
            SELECT m.id, m.name, m.release_year, m.duration, m.my_rating, 
                   STRING_AGG(DISTINCT g.genre_name, ', ') as genres
            FROM movies m
            LEFT JOIN movie_genres mg ON m.id = mg.movie_id
            LEFT JOIN genres g ON mg.genre_id = g.id
            GROUP BY m.id 
            ORDER BY m.name
            """
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            
            self.display_results(results)
            
        except Error as e:
            messagebox.showerror("Ошибка", f"Ошибка при загрузке фильмов: {e}")
    
    def display_results(self, results):
        # тображение результатов в таблице
        # Очистка таблицы
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Заполнение данными
        for row in results:
        
            duration = f"{row[3]} мин" if row[3] else ""
        
            rating = f"{row[4]}/10" if row[4] else ""
            
            self.tree.insert("", tk.END, values=(
                row[0], row[1], row[2], duration, rating, row[5]
            ))
        
        # Автоподбор ширины колонок
        self.auto_size_columns()
        
        
        self.tree.sort_column = None
        self.tree.sort_reverse = False
        
    
        for col in self.tree['columns']:
            current_text = self.tree.heading(col)['text']
            if current_text.endswith(' ▲') or current_text.endswith(' ▼'):
                self.tree.heading(col, text=current_text[:-2])
    
    def auto_size_columns(self):
        # Автоматическая подстройка ширины колонок
        if hasattr(self.tree, 'auto_size_columns'):
            self.tree.auto_size_columns()
    
    def on_movie_select(self, event):
        # Обработка выбора фильма в таблице
        selection = self.tree.selection()
        if not selection:
            return
            
        item = self.tree.item(selection[0])
        movie_id = item['values'][0]
        
        self.show_movie_details(movie_id)
    
    def show_movie_details(self, movie_id):
        # Показать детальную информацию о фильме
        try:
            cursor = self.connection.cursor()
            
            # Информация о фильме
            cursor.execute("""
                SELECT name, release_year, duration, description, my_rating
                FROM movies WHERE id = %s
            """, (movie_id,))
            movie_info = cursor.fetchone()
            
            # Актеры
            cursor.execute("""
                SELECT a.actor_name
                FROM actors a
                JOIN movie_actors ma ON a.id = ma.actor_id
                WHERE ma.movie_id = %s
                ORDER BY a.actor_name
            """, (movie_id,))
            actors = cursor.fetchall()
            
            # Жанры
            cursor.execute("""
                SELECT g.genre_name
                FROM genres g
                JOIN movie_genres mg ON g.id = mg.genre_id
                WHERE mg.movie_id = %s
                ORDER BY g.genre_name
            """, (movie_id,))
            genres = cursor.fetchall()
            
            # Просмотры
            cursor.execute("""
                SELECT viewing_date, notes
                FROM viewings
                WHERE movie_id = %s
                ORDER BY viewing_date DESC
            """, (movie_id,))
            viewings = cursor.fetchall()
            
            cursor.close()
            
            # Формируем текст
            info_text = ""
            if movie_info:
                info_text += f"🎬 Название: {movie_info[0]}\n"
                info_text += f"📅 Год выпуска: {movie_info[1]}\n"
                info_text += f"⏱️ Длительность: {movie_info[2]} мин\n"
                info_text += f"⭐ Ваш рейтинг: {movie_info[4]}/10\n\n"
                
                if movie_info[3]:
                    info_text += f"📝 Описание:\n{movie_info[3]}\n\n"
                
                if genres:
                    genre_list = ", ".join([g[0] for g in genres])
                    info_text += f"🎭 Жанры: {genre_list}\n\n"
                
                if actors:
                    actor_list = ", ".join([a[0] for a in actors])
                    info_text += f"👥 Актеры: {actor_list}\n\n"
                
                if viewings:
                    info_text += "📅 История просмотров:\n"
                    for view in viewings:
                        date_str = view[0].strftime("%d.%m.%Y")
                        notes = f" - {view[1]}" if view[1] else ""
                        info_text += f"  📌 {date_str}{notes}\n"
            
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(1.0, info_text)
            
        except Error as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить информацию: {e}")
    
    def show_statistics(self):
        # Показать статистику
        try:
            cursor = self.connection.cursor()
            
            # Статистика
            stats = []
            
            # Количество фильмов
            cursor.execute("SELECT COUNT(*) FROM movies")
            stats.append(f"🎬 Всего фильмов: {cursor.fetchone()[0]}")
            
            # Средний рейтинг
            cursor.execute("SELECT AVG(my_rating) FROM movies")
            avg_rating = cursor.fetchone()[0]
            stats.append(f"⭐ Средний рейтинг: {avg_rating:.1f}/10")
            
            # Фильмы по жанрам
            cursor.execute("""
                SELECT g.genre_name, COUNT(*) as count
                FROM genres g
                JOIN movie_genres mg ON g.id = mg.genre_id
                GROUP BY g.genre_name
                ORDER BY count DESC
                LIMIT 5
            """)
            top_genres = cursor.fetchall()
            stats.append("\n🏆 Топ-5 жанров:")
            for genre, count in top_genres:
                stats.append(f"  🎭 {genre}: {count}")
            
            # Самые популярные актеры
            cursor.execute("""
                SELECT a.actor_name, COUNT(*) as count
                FROM actors a
                JOIN movie_actors ma ON a.id = ma.actor_id
                GROUP BY a.actor_name
                ORDER BY count DESC
                LIMIT 5
            """)
            top_actors = cursor.fetchall()
            stats.append("\n👑 Топ-5 актеров:")
            for actor, count in top_actors:
                stats.append(f"  👤 {actor}: {count} фильмов")
            
            # Последние просмотры
            cursor.execute("""
                SELECT m.name, v.viewing_date
                FROM viewings v
                JOIN movies m ON v.movie_id = m.id
                ORDER BY v.viewing_date DESC
                LIMIT 5
            """)
            recent_viewings = cursor.fetchall()
            stats.append("\n📅 Последние просмотры:")
            for movie, view_date in recent_viewings:
                date_str = view_date.strftime("%d.%m.%Y")
                stats.append(f"  📌 {date_str}: {movie}")
            
            cursor.close()
            
            # Показываем статистику
            stats_window = tk.Toplevel(self.root)
            stats_window.title("Статистика видеотеки")
            stats_window.geometry("500x450")
            
            text_widget = scrolledtext.ScrolledText(stats_window, width=60, height=30, font=("Arial", 10))
            text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
            
            stats_text = "\n".join(stats)
            text_widget.insert(1.0, stats_text)
            
        except Error as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить статистику: {e}")
    
    def open_add_movie_window(self):
        # Окно добавления нового фильма
        self.create_movie_window(None, "Добавить новый фильм", "add")
    
    def open_edit_movie_window(self):
        # Окно редактирования фильма
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Предупреждение", "Выберите фильм для редактирования")
            return
        
        item = self.tree.item(selection[0])
        movie_id = item['values'][0]
        
        self.create_movie_window(movie_id, "Редактировать фильм", "edit")
    
    def create_movie_window(self, movie_id, title, mode):
        # Создание окна для добавления/редактирования фильма
        add_window = tk.Toplevel(self.root)
        add_window.title(title)
        add_window.geometry("600x700")
        
        # Переменные для данных
        current_movie_id = movie_id
        current_actors = []
        current_genres = []
        
    
        canvas = tk.Canvas(add_window)
        scrollbar = ttk.Scrollbar(add_window, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        row = 0
        
        ttk.Label(scrollable_frame, text="Название фильма:").grid(row=row, column=0, sticky=tk.W, padx=10, pady=(10, 5))
        row += 1
        title_entry = ttk.Entry(scrollable_frame, width=50)
        title_entry.grid(row=row, column=0, columnspan=2, padx=10, sticky=(tk.W, tk.E))
        row += 1
        
        ttk.Label(scrollable_frame, text="Год выпуска:").grid(row=row, column=0, sticky=tk.W, padx=10, pady=(10, 5))
        ttk.Label(scrollable_frame, text="Длительность (минут):").grid(row=row, column=1, sticky=tk.W, padx=10, pady=(10, 5))
        row += 1
        year_entry = ttk.Entry(scrollable_frame, width=20)
        year_entry.grid(row=row, column=0, sticky=tk.W, padx=10)
        duration_entry = ttk.Entry(scrollable_frame, width=20)
        duration_entry.grid(row=row, column=1, sticky=tk.W, padx=10)
        row += 1
        
        ttk.Label(scrollable_frame, text="Ваш рейтинг (1-10):").grid(row=row, column=0, sticky=tk.W, padx=10, pady=(10, 5))
        row += 1
        rating_entry = ttk.Entry(scrollable_frame, width=10)
        rating_entry.grid(row=row, column=0, sticky=tk.W, padx=10)
        row += 1
        
        ttk.Label(scrollable_frame, text="Описание:").grid(row=row, column=0, sticky=tk.W, padx=10, pady=(10, 5))
        row += 1
        desc_text = scrolledtext.ScrolledText(scrollable_frame, width=70, height=8)
        desc_text.grid(row=row, column=0, columnspan=2, padx=10, sticky=(tk.W, tk.E))
        row += 1
        
        ttk.Label(scrollable_frame, text="Жанры:").grid(row=row, column=0, sticky=tk.W, padx=10, pady=(10, 5))
        row += 1
        
        
        genre_frame = ttk.Frame(scrollable_frame)
        genre_frame.grid(row=row, column=0, columnspan=2, padx=10, sticky=(tk.W, tk.E))
        row += 1
        
        genre_listbox = tk.Listbox(genre_frame, selectmode=tk.MULTIPLE, height=8, width=40)
        genre_scrollbar = ttk.Scrollbar(genre_frame, orient=tk.VERTICAL, command=genre_listbox.yview)
        genre_listbox.configure(yscrollcommand=genre_scrollbar.set)
        
        genre_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        genre_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        ttk.Label(scrollable_frame, text="Актеры (через запятую):").grid(row=row, column=0, sticky=tk.W, padx=10, pady=(10, 5))
        row += 1
        actors_entry = ttk.Entry(scrollable_frame, width=70)
        actors_entry.grid(row=row, column=0, columnspan=2, padx=10, sticky=(tk.W, tk.E))
        row += 1
        
        # Заполняем список жанров
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT id, genre_name FROM genres ORDER BY genre_name")
            all_genres = cursor.fetchall()
            
            genre_dict = {}
            for genre_id, genre_name in all_genres:
                genre_listbox.insert(tk.END, genre_name)
                genre_dict[genre_name] = genre_id
            
            
            if mode == "edit" and current_movie_id:
                # Загружаем информацию о фильме
                cursor.execute("""
                    SELECT name, release_year, duration, description, my_rating
                    FROM movies WHERE id = %s
                """, (current_movie_id,))
                movie_data = cursor.fetchone()
                
                if movie_data:
                    title_entry.insert(0, movie_data[0])
                    if movie_data[1]:
                        year_entry.insert(0, str(movie_data[1]))
                    if movie_data[2]:
                        duration_entry.insert(0, str(movie_data[2]))
                    if movie_data[3]:
                        desc_text.insert(1.0, movie_data[3])
                    if movie_data[4]:
                        rating_entry.insert(0, str(movie_data[4]))
                
                # Загружаем текущие жанры
                cursor.execute("""
                    SELECT g.genre_name
                    FROM genres g
                    JOIN movie_genres mg ON g.id = mg.genre_id
                    WHERE mg.movie_id = %s
                """, (current_movie_id,))
                current_genres = [row[0] for row in cursor.fetchall()]
                
                # Выделяем текущие жанры в списке
                for i, (genre_id, genre_name) in enumerate(all_genres):
                    if genre_name in current_genres:
                        genre_listbox.selection_set(i)
                
                # Загружаем текущих актеров
                cursor.execute("""
                    SELECT a.actor_name
                    FROM actors a
                    JOIN movie_actors ma ON a.id = ma.actor_id
                    WHERE ma.movie_id = %s
                    ORDER BY a.actor_name
                """, (current_movie_id,))
                current_actors = [row[0] for row in cursor.fetchall()]
                actors_entry.insert(0, ", ".join(current_actors))
            
            cursor.close()
            
        except Error as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить данные: {e}")
        
        def save_movie():
            # Сохранение фильма в базу
            try:
                cursor = self.connection.cursor()
                
                if mode == "add":
                    # Добавляем фильм
                    cursor.execute("""
                        INSERT INTO movies (name, release_year, duration, description, my_rating)
                        VALUES (%s, %s, %s, %s, %s) RETURNING id
                    """, (
                        title_entry.get(),
                        int(year_entry.get()) if year_entry.get() else None,
                        int(duration_entry.get()) if duration_entry.get() else None,
                        desc_text.get(1.0, tk.END).strip(),
                        int(rating_entry.get()) if rating_entry.get() else None
                    ))
                    
                    movie_id = cursor.fetchone()[0]
                    
                else: 
                    movie_id = current_movie_id
                    
                    # Обновляем информацию о фильме
                    cursor.execute("""
                        UPDATE movies 
                        SET name = %s, 
                            release_year = %s, 
                            duration = %s, 
                            description = %s, 
                            my_rating = %s
                        WHERE id = %s
                    """, (
                        title_entry.get(),
                        int(year_entry.get()) if year_entry.get() else None,
                        int(duration_entry.get()) if duration_entry.get() else None,
                        desc_text.get(1.0, tk.END).strip(),
                        int(rating_entry.get()) if rating_entry.get() else None,
                        movie_id
                    ))
                    
                    
                    cursor.execute("DELETE FROM movie_genres WHERE movie_id = %s", (movie_id,))
                    
                    
                    cursor.execute("DELETE FROM movie_actors WHERE movie_id = %s", (movie_id,))
                
                # Добавляем жанры
                selected_genres = genre_listbox.curselection()
                for index in selected_genres:
                    genre_name = genre_listbox.get(index)
                    genre_id = genre_dict[genre_name]
                    cursor.execute("INSERT INTO movie_genres (movie_id, genre_id) VALUES (%s, %s)", 
                                  (movie_id, genre_id))
                
                # Добавляем актеров
                actors = [a.strip() for a in actors_entry.get().split(',') if a.strip()]
                for actor_name in actors:
                    
                    cursor.execute("SELECT id FROM actors WHERE actor_name = %s", (actor_name,))
                    result = cursor.fetchone()
                    if result:
                        actor_id = result[0]
                    else:
                        # Добавляем нового актера
                        cursor.execute("INSERT INTO actors (actor_name) VALUES (%s) RETURNING id", (actor_name,))
                        actor_id = cursor.fetchone()[0]
                    
                    # Связываем актера с фильмом
                    cursor.execute("INSERT INTO movie_actors (movie_id, actor_id) VALUES (%s, %s)", 
                                  (movie_id, actor_id))
                
                self.connection.commit()
                cursor.close()
                
                messagebox.showinfo("Успех", 
                    f"Фильм успешно {'добавлен' if mode == 'add' else 'обновлен'}!")
                add_window.destroy()
                self.show_all_movies()  
                
                
                if mode == "edit":
                    selection = self.tree.selection()
                    if selection:
                        item = self.tree.item(selection[0])
                        if item['values'][0] == movie_id:
                            self.show_movie_details(movie_id)
                
            except Exception as e:
                self.connection.rollback()
                messagebox.showerror("Ошибка", 
                    f"Не удалось {'добавить' if mode == 'add' else 'обновить'} фильм: {e}")
        
        # Кнопки
        button_frame = ttk.Frame(scrollable_frame)
        button_frame.grid(row=row, column=0, columnspan=2, pady=20)
        ttk.Button(button_frame, text="Сохранить", command=save_movie).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Отмена", command=add_window.destroy).pack(side=tk.LEFT, padx=5)
        
        # Упаковка прокрутки
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Фокус на первом поле
        title_entry.focus_set()
    
    def open_add_actor_window(self):
        # Окно добавления актера
        add_window = tk.Toplevel(self.root)
        add_window.title("Добавить актера")
        add_window.geometry("300x150")
        
        ttk.Label(add_window, text="Имя актера:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=(20, 5))
        actor_entry = ttk.Entry(add_window, width=30)
        actor_entry.grid(row=1, column=0, padx=10, sticky=(tk.W, tk.E))
        
        def save_actor():
            actor_name = actor_entry.get().strip()
            if not actor_name:
                messagebox.showwarning("Предупреждение", "Введите имя актера")
                return
            
            try:
                cursor = self.connection.cursor()
                cursor.execute("INSERT INTO actors (actor_name) VALUES (%s)", (actor_name,))
                self.connection.commit()
                cursor.close()
                
                messagebox.showinfo("Успех", "Актер успешно добавлен!")
                add_window.destroy()
                
            except Exception as e:
                self.connection.rollback()
                messagebox.showerror("Ошибка", f"Не удалось добавить актера: {e}")
        
        ttk.Button(add_window, text="Сохранить", command=save_actor).grid(row=2, column=0, pady=20)
    
    def open_add_viewing_window(self):
        # Окно добавления просмотра
        add_window = tk.Toplevel(self.root)
        add_window.title("Добавить просмотр")
        add_window.geometry("400x350")
        
        ttk.Label(add_window, text="Выберите фильм:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=(10, 5))
        
        # Выпадающий список фильмов - ТОЛЬКО ВЫШЕДШИЕ
        movie_var = tk.StringVar()
        self.movie_combo = ttk.Combobox(add_window, textvariable=movie_var, width=40, state="readonly")
        self.movie_combo.grid(row=1, column=0, padx=10, sticky=(tk.W, tk.E))
        
        # Информация о годе выпуска
        self.release_year_label = ttk.Label(add_window, text="")
        self.release_year_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=(0, 10))
        
        # Заполняем список ТОЛЬКО ВЫШЕДШИХ фильмов
        self.load_released_movies_for_viewing()
        
        # Привязываем событие выбора фильма
        self.movie_combo.bind('<<ComboboxSelected>>', self.on_movie_selected_for_viewing)
        
        ttk.Label(add_window, text="Дата просмотра (ГГГГ-ММ-ДД):").grid(row=3, column=0, sticky=tk.W, padx=10, pady=(10, 5))
        date_entry = ttk.Entry(add_window, width=15)
        date_entry.grid(row=4, column=0, sticky=tk.W, padx=10)
        date_entry.insert(0, date.today().strftime("%Y-%m-%d"))
        
        ttk.Label(add_window, text="Заметки:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=(10, 5))
        notes_entry = scrolledtext.ScrolledText(add_window, width=40, height=6)
        notes_entry.grid(row=6, column=0, padx=10, sticky=(tk.W, tk.E))
        
        def save_viewing():
            movie_text = movie_var.get()
            if not movie_text:
                messagebox.showwarning("Предупреждение", "Выберите фильм")
                return
            
            # Извлекаем ID из строки
            try:
                movie_id = int(movie_text.split("ID: ")[1].rstrip(")"))
            except:
                messagebox.showerror("Ошибка", "Неверный формат выбора фильма")
                return
            
            # Проверяем год выпуска фильма
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT release_year FROM movies WHERE id = %s", (movie_id,))
                release_year_result = cursor.fetchone()
                cursor.close()
                
                if release_year_result:
                    release_year = release_year_result[0]
                    current_year = date.today().year
                    
                    if release_year and release_year > current_year:
                        # ЗАПРЕЩАЕМ добавление просмотра
                        messagebox.showerror("Ошибка", 
                            f"Невозможно добавить просмотр!\n"
                            f"Фильм '{movie_text.split('(ID:')[0].strip()}' выйдет только в {release_year} году.")
                        return
            except Exception as e:
                print(f"Ошибка при проверке года: {e}")
            
            viewing_date = date_entry.get()
            notes = notes_entry.get(1.0, tk.END).strip()
            
            try:
                cursor = self.connection.cursor()
                cursor.execute("""
                    INSERT INTO viewings (movie_id, viewing_date, notes)
                    VALUES (%s, %s, %s)
                """, (movie_id, viewing_date, notes))
                
                self.connection.commit()
                cursor.close()
                
                messagebox.showinfo("Успех", "Просмотр успешно добавлен!")
                add_window.destroy()
                
                # Обновляем информацию о выбранном фильме
                selection = self.tree.selection()
                if selection:
                    item = self.tree.item(selection[0])
                    if item['values'][0] == movie_id:
                        self.show_movie_details(movie_id)
                
            except Exception as e:
                self.connection.rollback()
                messagebox.showerror("Ошибка", f"Не удалось добавить просмотр: {e}")
        
        ttk.Button(add_window, text="Сохранить", command=save_viewing).grid(row=7, column=0, pady=20)
    
    def load_released_movies_for_viewing(self):
        # Загрузка только вышедших фильмов для окна добавления просмотра
        try:
            cursor = self.connection.cursor()
            current_year = date.today().year
            
            # Загружаем фильмы, которые уже вышли (год выпуска <= текущий год)
            cursor.execute("""
                SELECT id, name, release_year 
                FROM movies 
                WHERE release_year IS NULL OR release_year <= %s 
                ORDER BY name
            """, (current_year,))
            
            movies = cursor.fetchall()
            
            movie_list = []
            self.movie_info = {}  # Словарь для хранения информации о фильмах
            
            for movie_id, movie_name, release_year in movies:
                display_text = f"{movie_name} (ID: {movie_id})"
                movie_list.append(display_text)
                self.movie_info[display_text] = {
                    'id': movie_id,
                    'year': release_year,
                    'name': movie_name
                }
            
            if not movie_list:
                self.movie_combo['values'] = ["Нет вышедших фильмов"]
                self.movie_combo.set("Нет вышедших фильмов")
                self.movie_combo.config(state="disabled")
                self.release_year_label.config(
                    text="В вашей коллекции нет фильмов, которые уже вышли в прокат",
                    foreground="red"
                )
            else:
                self.movie_combo['values'] = movie_list
                self.movie_combo.config(state="readonly")
            
            cursor.close()
            
        except Error as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить фильмы: {e}")
    
    def on_movie_selected_for_viewing(self, event):
        # Обработка выбора фильма в окне добавления просмотра
        selected_movie = self.movie_combo.get()
        
        if selected_movie in self.movie_info:
            movie_data = self.movie_info[selected_movie]
            release_year = movie_data['year']
            
            if release_year:
                self.release_year_label.config(
                    text=f"Год выпуска: {release_year}",
                    foreground="black"
                )
            else:
                self.release_year_label.config(
                    text="Год выпуска: неизвестен",
                    foreground="gray"
                )
    
    def delete_movie(self):
        # Удаление выбранного фильма
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Предупреждение", "Выберите фильм для удаления")
            return
        
        item = self.tree.item(selection[0])
        movie_id = item['values'][0]
        movie_name = item['values'][1]
        
        # Подтверждение
        if not messagebox.askyesno("Подтверждение", f"Вы действительно хотите удалить фильм '{movie_name}'?"):
            return
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM movies WHERE id = %s", (movie_id,))
            self.connection.commit()
            cursor.close()
            
            messagebox.showinfo("Успех", "Фильм удален!")
            self.show_all_movies()  
            
        except Exception as e:
            self.connection.rollback()
            messagebox.showerror("Ошибка", f"Не удалось удалить фильм: {e}")

def main():
    root = tk.Tk()
    app = VideoLibraryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()