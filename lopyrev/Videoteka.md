Сегодня разработал структуру базы данных и создал таблицы для домашней видеотеки

Таблица с фильмами
У нас есть название фильма, год релиза, жанр, длительность фильма, описание, свой рейтинг и дата просмотра
id|name|release_year|duration|description|my_rating

Таблица с актерами
В этой таблице хранятся актеры
id|actor_name|

Таблица жанров
В этой таблице хранятся жанры
id|ganre_name|

Таблица просмотров
id|movie_id|viewing_date|notes

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

