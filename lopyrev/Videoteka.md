
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

Вставка данных в таблицы

Жанры:
INSERT INTO genres (genre_name) VALUES ('Драма'), ('Комедия'), ('Ужасы'), ('Боевик'), ('Фантастика'), 
('Триллер'), ('Мелодрама'), ('Детектив'), ('Мультфильм'), ('Фэнтези'), ('Приключения'), 
('Исторический'), ('Криминал'), ('Биография'), ('Вестерн');

Актеры:
NSERT INTO actors (actor_name) VALUES ('Леонардо ДиКаприо'), ('Кейт Уинслет'), ('Билли Зейн'), ('Мэттью Макконахи'), ('Энн Хэтэуэй'), 
('Майкл Кейн'), ('Марлон Брандо'), ('Аль Пачино'), ('Роберт Де Ниро'), ('Джеймс Каан'), ('Том Хэнкс'), ('Робин Райт'), ('Гэри Синиз'), 
('Майкл Кларк Дункан'), ('Дэвид Морс'), ('Клинт Иствуд'), ('Морган Фриман'), ('Тим Роббинс'), ('Джин Хэкмен'), ('Эдвард Нортон'), 
('Брэд Питт'), ('Хелена Бонем Картер'), ('Джонни Депп'), ('Орландо Блум'), ('Кира Найтли'), ('Юэн Макгрегор'), ('Натали Портман'), 
('Хэйден Кристенсен'), ('Иэн Маккеллен'), ('Элайджа Вуд'), ('Вигго Мортенсен'), ('Шон Эстин');

Фильмы:
INSERT INTO movies (name, release_year, duration, description, my_rating) VALUES ('Титаник', 1997, 194, 'Молодые влюбленные Джек и Роза находят друг друга в первом и последнем плавании «непотопляемого» Титаника.', 9), 
('Интерстеллар', 2014, 169, 'Фермер Купер отправляется в космическое путешествие, чтобы найти новую планету для человечества.', 10), 
('Крестный отец', 1972, 175, 'Эпос о сицилийской мафиозной семье Корлеоне.', 10), 
('Форрест Гамп', 1994, 142, 'История простодушного, но доброго человека, который невольно влияет на важные события в истории США.', 9), 
('Зеленая миля', 1999, 189, 'История надзирателя тюрьмы и необычного заключенного с даром исцеления.', 10), 
('Побег из Шоушенка', 1994, 142, 'Банкир Энди Дюфрейн оказывается в тюрьме Шоушенк за убийство жены и её любовника.', 10), 
('Бойцовский клуб', 1999, 139, 'Страдающий бессонницей сотрудник страховой компании и мыловар Тайлер Дёрден создают подпольный бойцовский клуб.', 9), 
('Пираты Карибского моря: Проклятие Черной жемчужины', 2003, 143, 'Капитан Джек Воробей и кузнец Уилл Тёрнер спасают похищенную дочь губернатора.', 8), 
('Звездные войны: Эпизод 3 — Месть Ситхов', 2005, 140, 'Анакин Скайуокер переходит на темную сторону Силы, становясь Дартом Вейдером.', 8), 
('Властелин колец: Братство Кольца', 2001, 178, 'Хоббит Фродо должен уничтожить Кольцо Всевластия в огне Ородруина.', 10);

Связь фильм-жанр
INSERT INTO movie_genres (movie_id, genre_id) VALUES (1, 6), (1, 11), (2, 4), (2, 1), (3, 1), (3, 13), (4, 1), (4, 2), (5, 1), (5, 10), 
(6, 1), (7, 1), (7, 5), (8, 11), (8, 2), (8, 10), (9, 4), (9, 11), (10, 10), (10, 11);

Связь фильм-актер
INSERT INTO movie_actors (movie_id, actor_id) VALUES (1, 1), (1, 2), (1, 3), (2, 4), (2, 5), (2, 6), (3, 7), (3, 8), (3, 9), (3, 10), 
(4, 11), (4, 12), (4, 13), (5, 11), (5, 14), (5, 15), (6, 16), (6, 17), (6, 18), (6, 19), (7, 20), (7, 21), (7, 22), (8, 23), (8, 24), 
(8, 25), (9, 26), (9, 27), (9, 28), (10, 29), (10, 30), (10, 31), (10, 32);

Таблица просмотров
INSERT INTO viewings (movie_id, viewing_date, notes) VALUES (1, '2023-12-09', 'Грустный но интересный фильм'), (1, '2024-12-24', 'Рождественский просмотр'), 
(2, '2024-04-12', 'Пятничный просмотр после работы'), (3, '2024-09-09', 'Обычный просмотр классики'), (3, '2024-10-12', 'Смотрел с друзьями'), 
(4, '2024-10-20', 'Интересный фильм'), (5, '2025-01-10', 'Эмоциональное кино'), (6, '2025-02-11', 'Лучший фильм'), (7, '2025-02-20', '-'), 
(8, '2025-03-04', 'Вечерний просмотр кино'), (9, '2025-03-19', 'Пересмотр в отпуске'), (10, '2025-06-11', 'Вспомнил классику');

Запросы к базе данных:
Вывод всех фильмов с жанрами и актерами
SELECT 
    m.name as "Фильм",
    m.release_year as "Год",
    m.my_rating as "Рейтинг",
    STRING_AGG(DISTINCT g.genre_name, ', ') as "Жанры",
    STRING_AGG(DISTINCT a.actor_name, ', ') as "Актеры",
    COUNT(DISTINCT v.id) as "Просмотров"
FROM movies m
LEFT JOIN movie_genres mg ON m.id = mg.movie_id
LEFT JOIN genres g ON mg.genre_id = g.id
LEFT JOIN movie_actors ma ON m.id = ma.movie_id
LEFT JOIN actors a ON ma.actor_id = a.id
LEFT JOIN viewings v ON m.id = v.movie_id
GROUP BY m.id
ORDER BY m.my_rating DESC;

Статистика фильмо по жанрам
SELECT 
    g.genre_name as "Жанр",
    COUNT(DISTINCT mg.movie_id) as "Фильмов",
    ROUND(AVG(m.my_rating), 1) as "Средний рейтинг"
FROM genres g
LEFT JOIN movie_genres mg ON g.id = mg.genre_id
LEFT JOIN movies m ON mg.movie_id = m.id
GROUP BY g.id
HAVING COUNT(DISTINCT mg.movie_id) > 0
ORDER BY COUNT(DISTINCT mg.movie_id) DESC;

История просмотров
SELECT 
    m.name as "Фильм",
    v.viewing_date as "Дата просмотра",
    v.notes as "Заметки"
FROM viewings v
JOIN movies m ON v.movie_id = m.id
ORDER BY v.viewing_date DESC;

09.12.25
Дописал приложение на python с ui для взаимодействия с базой данных
