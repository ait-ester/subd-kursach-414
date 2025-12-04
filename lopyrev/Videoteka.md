Сегодня разработал структуру базы данных и создал таблицы для домашней видеотеки

Таблица с фильмами
У нас есть название фильма, год релиза, длительность фильма, описание, свой рейтинг
CREATE TABLE movies (id SERIAL PRIMARY KEY, name VARCHAR(200) NOT NULL, release_year INTEGER, duration INTEGER, description TEXT, my_rating INTEGER CHECK (my_rating >= 1 AND my_rating <= 10));

Таблица с актерами
В этой таблице хранятся актеры
CREATE TABLE actors (id SERIAL PRIMARY KEY, actor_name VARCHAR(100) NOT NULL);

Таблица жанров
В этой таблице хранятся жанры
CREATE TABLE genres (id SERIAL PRIMARY KEY, genre_name VARCHAR(50) UNIQUE NOT NULL);

Таблица просмотров
CREATE TABLE viewings (id SERIAL PRIMARY KEY, movie_id INTEGER REFERENCES movies(id) ON DELETE CASCADE, viewing_date DATE NOT NULL DEFAULT CURRENT_DATE, notes TEXT);

Связь фильм-актеры
Здесь устанавливается связь между актерами и фильмами в которых они снимались
CREATE TABLE movie_actors (
    movie_id INTEGER REFERENCES movies(id) ON DELETE CASCADE,
    actor_id INTEGER REFERENCES actors(id) ON DELETE CASCADE,
    PRIMARY KEY (movie_id, actor_id)
);

Связь фильм-жанр
Здесь устанавливается связь между фильмом и его жанрами(может быть несколько жанров)
CREATE TABLE movie_genres (
    movie_id INTEGER REFERENCES movies(id) ON DELETE CASCADE,
    genre_id INTEGER REFERENCES genres(id) ON DELETE CASCADE,
    PRIMARY KEY (movie_id, genre_id)
);

