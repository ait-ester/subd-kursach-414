### <p align="center">Министерство образования, науки и молодежной политики Республики Коми
### <p align="center">ГПОУ "Сыктывкарский политехнический техникум"
## <p align="center">Курсовая работа

## <p align="center">**Тема: База данных гостиницы. Подсистема «Работа с клиентами»**








#### <p align="right">**Выполнил**

<p align="right">Студент 4 курса 414 группы Михаил Игоревич Елесов

#### <p align="right">**Проверил**
<p align="right">Пунгин Илья Вячеславович

#### <p align="right">**Дата проверки:**
<p align="right">18.12.2025


<p align="center">Сыктывкар 2025


---

# <p align="center">**Содержание**

[-Введение](#введение)  
[-Анализ предметной области](#Анализ-предметной-области)  
[-Проектирование базы данных](#Проектирование-базы-данных)  
[-Логическая структура](#Логическая-структура)  
[-Физическая структура](#Физическая-структура-данных)  
[-Реализация системы](#Реализация-системы)  
[-Безопасность](#Безопасность)  
[-Разработка стратегии резервного копирования](#Разработка-стратегии-резервного-копирования)  
[-Заключение](#Заключение)  
[-Приложение](#Приложение)

# <p align="center">**Введение**
##### Актуальность темы  
Современные отели предлагают много услуг: регистрация клиентов, бронирование номеров, составление расписаний и пр. Из-за этого данных стало очень много — о клиентах, бронях, номерах, финансах.
Вручную работать с этим объемом информации сложно, медленно и можно ошибиться. Поэтому сегодня важно иметь не просто файлы или таблицы, а единую базу данных.
Она нужна, чтобы:  
1.	Быстро находить свободные номера и оформлять клиентов.  
2.	Надежно и безопасно хранить все данные в одном месте.  
3.	Автоматизировать рутину — печать счетов, отчётов.  
4.	Анализировать работу отеля для принятия правильных решений.  
Простыми словами, база данных упрощает структурирование, хранение больших объёмов информации, а также управление ими, поэтому тема считается довольно актуальной.  

##### Цель и Задачи
Целью является создание системы управления гостиницей на основе базы данных с удобным пользовательским интерфейсом.
Для достижения цели были поставлены задачи:  
1.	Анализ предметной области  
2.	Описание структуры базы данных  
3.	Реализация базы данных в СУБД PostgreSQL  
4.	Реализация пользовательского интерфейса с помощью языка программирования Python в редакторе Visual Studio Code

##### Практическая значимость  
Результаты моей курсовой работы могут быть полезны для реальной деятельности гостиницы.  
1.	 Созданная база данных — это готовый каркас системы, который можно установить в небольшой гостинице или отеле, чтобы автоматизировать работу с бронями, клиентами и номерами.  
2.	Система упростит рутинную работу:  
•    Ускорит процесс заселения и выписки гостей.  
•    Уменьшит число ошибок в расчетах и при поиске информации.  
•    Сама будет создавать счета, отчеты и напоминания.  
3.	С помощью базы данных руководитель сможет легко и быстро получать нужную информацию:  
•	Видеть, какие номера пользуются спросом.  
•	Вести историю постоянных клиентов.  
4.	Работа может стать хорошим примером для других студентов, которые учатся создавать базы данных, показывая весь процесс от идеи до готовой системы.  

# <p align="center">**Анализ предметной области**

##### Описание предметной области
База данных для гостиницы должна хранить информацию о постояльцах, работниках, комнатах и их статусах и историю бронирований.  
**Основные компоненты системы:**  
1.	Список должностей  
2.	Список сотрудников  
3.	Список номеров  
4.	Список постояльцев  
5.	История бронирований  

##### Перечень входных данных  
1.Список должностей  
2.Список сотрудников  
•	ФИО  
•	Должность  

3.Койки  
•	Номера, в которых койки находятся  
•	Статус коек  
•	Цена за ночь  

4.	Постояльцы  
•	ФИО  
•	Контактные данные  
•	Паспортные данные  

##### Перечень выходных данных  
1.	История бронирований  
•	Дата заезда  
•	Дата выселения  
•	Постоялец  
•	Койка  
•	Количество ночей  
•	Итоговый ценник  

2.	Расписание уборок номеров  
•	Дата  
•	Номер уборки  
•	Горничная  

##### Требования и ограничения  
**Функциональные требования**   

1.	Управление клиентами  
    •	Хранение данных гостей (ФИО, контактные и паспортные данные)  

2.	Управление номерным фондом  
    •	Учёт номеров и их статусов  

3.	Управление процессом бронирования 
    •	Создание и изменение брони  
    •	Контроль за датами заезда и выезда  

4.	Управление расписаниями  

**Требования к данным**  
1.	Целостность (гарантия, что данные не противоречат друг другу)  
2.	Точность (Корректное отражение всех операций)  

**Практические ограничения**  
1.	Простота и удобство интерфейса  
2.	Уникальность данных (не должно быть одинаковых записей)  

# <p align="center">**Проектирование базы данных**

##### Концептуальная модель
Концептуальная модель – схема, отображающая основные компоненты системы и связи между ними (см. рисунок 1).

Основные компоненты:  
1.	Должности(roles)
2.	Работники(workers)  
3.	Комнаты(rooms)  
4.	Койки(beds)  
5.	Постояльцы(clients)  
6.	Бронирования(reservations)  
7.	Расписание уборки(schedule_of_cleaning_rooms)  

**Связи:**  
1.	Должности – работники  
•	Работник обязательно должен иметь должность

2.	Комнаты – койки  
•	Каждая койка должна быть закреплена за определённой комнатой

3.	Постояльцы – бронирования  
•	Одна бронь закрепляется за одним постояльцем  
•	Один постоялец может сделать несколько броней

4.	Койки – бронирования  
•	В записи бронирования должна быть указана койка

5.	Работники – бронирования
•	Бронь должен создавать администратор

6.	Расписание уборки – Комнаты  
•	Комната должна указываться в записи

7.	Расписание уборки – работники  
•	Должна быть указана горничная, ответственная за уборку

# <p align="center">**Логическая структура**

**База данных состоит из 7 таблиц (см. рисунок 2):**  
1.	roles (должности):    
•  id – Уникальный идентификатор (первичный ключ)  
•	name – название должности  

2.	workers (работники):
•	id – Уникальный идентификатор (первичный ключ)
•	name – ФИО работника
•	role – должность (внешний ключ от roles.id)

3.	rooms (комнаты):  
•	number – номер комнаты, уникальный идентификатор (первичный ключ)  
•	floor – этаж  
•	number_of_places – количество мест  
•	is_active – свободна ли комната  

4.	beds (койки):  
•	id – Уникальный идентификатор (первичный ключ)  
•	room_number – номер комнаты (внешний ключ от rooms.number)  
•	is_occupied – свободна ли койка  
•	price_per_night – ценник за ночь  

5.	clients (постояльцы):  
•	id – Уникальный идентификатор (первичный ключ)  
•	name – Имя  
•	surname – фамилия  
•	surname1 – отчество  
•	phone_number – номер телефона  
•	email – адрес электронной почты  
•	passport_series – серия паспорта  
•	passport_number – номер паспорта  

6.	reservation (бронирования):  
•	date_of_checkin – дата заезда  
•	date_of_checkout – дата выезда  
•	client – постоялец (внешний ключ от clients.id)  
•	administrator – администратор (внешний ключ от workers.id)  
•	bed – койка (внешний ключ от beds.id)  
•	number_of_nights – количество ночей  
•	total_price – Итоговый ценник  

7.	schedule_of_cleaning_rooms (расписание уборок комнат):  
•	date_of_cleaning – Дата уборки  
•	room_number – номер комнаты (внешний ключ от rooms.number)  
•	housemaid – горничная (внешний ключ от workers.id)   

# <p align="center">**Физическая структура данных**

Физическая реализация включает в себя создание таблиц и их описание.

roles:
|Название|Тип|Комментарий|
|--------|---|-----------|
|id|	INTEGER|	Ключ|
|name|	VARCHAR NOT NULL|	Название|

workers:
|Название|Тип|Комментарий|
|--------|---|-----------|
|id|	INTEGER|	Ключ|
|name|	VARCHAR NOT NULL|	ФИО|
|role|	INTEGER|	Должность|

rooms:
|Название|Тип|Комментарий|
|--------|---|-----------|
|number|VARCHAR(3) NOT NULL|Номер комнаты, ключ|
|floor|INTEGER|Этаж|
|number_of_places|INTEGER|оличество мест|
|is_active|BOOLEAN|Свободна ли комната|

beds:
|Название|Тип|Комментарий|
|--------|---|-----------|
|id|INTEGER|Ключ|
|room_number|VARCHAR(3) NOT NULL|Номер комнаты|
|is_occupied|BOOLEAN|Занята ли койка|
|price_per_nigh|REAL|Цена за ночь|

clients:
|Название|Тип|Комментарий|
|--------|---|-----------|
|id|	INTEGER|	Ключ
|name|	VARCHAR NOT NULL|	Имя
|surname|	VARCHAR NOT NULL|	Фамилия
|surname1|	VARCHAR|	Отчество
|phone_number|	VARCHAR(11) NOT NULL|	Номер телефона
|email|	VARCHAR|	Электронная почта
|passport_series|	VARCHAR(4) NOT NULL|	Серия паспорта
|passport_number|	VARCHAR(6) NOT NULL|	Номер паспорта

reservation:
|Название|Тип|Комментарий|
|--------|---|-----------|
|date_of_checkin|DATE NOT NULL|Дата заезда
|date_of_checkout|DATE NOT NULL|Дата выезда
|client|INTEGER|Постоялец
|administrator|INTEGER|Администратор
|number_of_nights|INTEGER|Количество ночей
|total_price|REAL|Итоговый ценник

schedule_of_cleaning_rooms:
|Название|Тип|Комментарий|
|--------|---|-----------|
|date_of_cleaning|DATE NOT NULL|Дата уборки
|room_number|VARCHAR(3) NOT NULL|Комната
|housemaid|INTEGER NOT NULL|Горничная

# <p align="center">**Реализация системы**

##### Создание базы данных  
База данных создавалась в СУБД PostgreSQL 18.  
**Создание таблиц:**  
```sql
    • create table roles (id integer primary key, name varchar(20) not null); -- таблица с должностями  
    • create table workers(id integer primary key, name varchar not null, role integer, foreign key (role) references roles(id)); -- таблица с работниками
    • create table rooms(number varchar(3) primary key, floor integer, number_of_places integer, is_active boolean); -- таблица с номерами
    • create table beds(id integer primary key, room_number varchar(3) not null, is_occupied boolean, price_per_night real, foreign key (room_number) references rooms(number)); -- таблица с койками
    • create table clients(id integer primary key, name varchar not null, surname varchar not null, surname1 varchar, phone_number varchar(11) not null, email varchar, passport_series varchar(4) not null, passport_number varchar(6) not null); -- таблица с постояльцами
    • create table reservation(date_of_checkin date, date_of_checkout date, client integer, administrator integer, bed integer, number_of_nights integer, total_price real, foreign key (client) references clients(id), foreign key (administrator) references workers(id), foreign key (bed) references beds(id)); -- история брони (будет заполняться в приложении)
    • create table schedule_of_cleaning_rooms (date_of_cleaning date not null, room_number varchar(3) not null, housemaid integer not null, foreign key (room_number) references rooms(number), foreign key (housemaid) references workers(id)); -- таблица для расписания уборок номеров (будет заполняться в приложении)
```
**Заполнение таблиц необходимыми данными:**  
```sql
    • insert into rooms values('111', 1, 1, true), ('112', 1, 1, true), ('113', 1, 1, true), ('114', 1, 1, true), ('115', 1, 1, true), ('116', 1, 1, true);  
    • insert into rooms values('211', 2, 2, true), ('212', 2, 2, true), ('213', 2, 2, true), ('214', 2, 2, true), ('215', 2, 2, true), ('216', 2, 2, true);  
    • insert into rooms values('311', 3, 3, true), ('312', 3, 3, true), ('313', 3, 3, true), ('314', 3, 3, true), ('315', 3, 3, true), ('316', 3, 3, true);  
    • insert into rooms values('411', 4, 4, true), ('412', 4, 4, true), ('413', 4, 4, true), ('414', 4, 4, true), ('415', 4, 4, true), ('416', 4, 4, true);  
    • insert into beds values(1, '111', false, 100), (2, '112', false, 100), (3, '113', true, 100), (4, '114', true, 100), (5, '115', true, 100), (6, '116', true, 100);  
    • insert into beds values(7, '211', true, 200), (8, '211', true, 200), (9, '212', true, 200), (10, '212', true, 200), (11, '213', true, 200), (12, '213', true, 200);  
    • insert into beds values(13, '214', true, 200), (14, '214', true, 200), (15, '215', true, 200), (16, '215', true, 200), (17, '216', true, 200), (18, '216', true, 200);  
    • insert into beds values(19, '311', true, 300), (20, '311', true, 300), (21, '311', true, 300);  
    • insert into beds values(22, '312', true, 300), (23, '312', true, 300), (24, '312', true, 300);  
    • insert into beds values(25, '313', true, 300), (26, '313', true, 300), (27, '313', true, 300);  
    • insert into beds values(28, '314', true, 300), (29, '314', true, 300), (30, '314', true, 300);  
    • insert into beds values(31, '315', true, 300), (32, '315', true, 300), (33, '315', true, 300);  
    • insert into beds values(34, '316', true, 300), (35, '316', true, 300), (36, '316', true, 300);  
    • insert into beds values(37, '411', true, 400), (38, '411', true, 400), (39, '411', true, 400), (40, '411', true, 400);  
    • insert into beds values(41, '412', true, 400), (42, '412', true, 400), (43, '412', true, 400), (44, '412', true, 400);  
    • insert into beds values(45, '413', true, 400), (46, '413', true, 400), (47, '413', true, 400), (48, '413', true, 400);  
    • insert into beds values(49, '414', true, 400), (50, '414', true, 400), (51, '414', true, 400), (52, '414', true, 400);  
    • insert into beds values(53, '415', true, 400), (54, '415', true, 400), (55, '415', true, 400), (56, '415', true, 400);  
    • insert into beds values(57, '416', true, 400), (58, '416', true, 400), (59, '416', true, 400), (60, '416', true, 400);  
```
**Создание процедур:**
```sql  
    • create or replace procedure extension(client_id integer, new_date date) as $$ begin update reservation set date_of_checkout=new_date where client=client_id; end; $$ language plpgsql; -- процедура, обновляющая дату выселения  
    • create or replace procedure checkin(date_checkin date, date_checkout date, client_id integer, admin integer, bed integer, number_of_nights integer) as $$ declare t_price real; b_price real; begin select price_per_night into b_price from beds where id = bed; t_price := b_price * number_of_nights; insert into reservation values(date_checkin, date_checkout, client_id, admin, bed,  number_of_nights, t_price); end; $$ language plpgsql; -- процедура заселения 
``` 

##### Разработка пользовательского интерфейса
Для пользовательского интерфейса для базы данных использовался язык программирования Python и редактор кода Visual Studio Code.  
Для реализации нужного результата использовались следующие библиотеки:  
    • tkinter  
    • psycopg2  
    • datetime  
    • tkalendar  

Архитектура приложения и его компоненты (см. рисунки 3 – 10):  
    1. Главное окно  
    • **Вкладки**  
        ◦ **Вкладка для бронирований**  
    ◦ ◦Поля для заполнений информации о клиентах, администраторах и датах  
    ◦ ◦Таблица бронирований  
    ◦ ◦Кнопки создания, удаления бронирований и обновления данных  
        ◦ **Вкладка постояльцев**  
    ◦ ◦Таблица с постояльцами  
    ◦ ◦Кнопки добавления, удаления постояльцев и обновления данных  
    ◦ ◦Фильтр постояльцев  
        ◦ **Вкладка номеров и коек**  
    ◦ ◦Таблица с койками  
    ◦ ◦Кнопка для изменения статуса определённой койки  
    ◦ ◦Фильтр коек  
        ◦ **Вкладка для расписаний уборок**  
    ◦ ◦Таблица с расписанием  
    ◦ ◦Поля для заполнения информации о дате, номере и горничной  
    ◦ ◦Кнопка для добавления записи в базу  
    ◦ ◦Фильтр записей об уборке  
        ◦ **Вкладка работников**  
    ◦ ◦Таблица с работниками  
    ◦ ◦Кнопки добавления, удаления работников и обновления данных  
    ◦ ◦Фильтр работников  
        ◦ **Вкладка отчётов**  
    2. **Диалоговые окна** (Окна для заполнения)  

##### **Тестирование системы**
Функциональное тестирование:  
    1. Проверка корректного добавления данных  
    2. Поиск брони, постояльца, работника по определённым параметрам  

Тестирование пользовательского интерфейса:  
    1. Проверка работоспособности всех кнопок  
    2. Проверка фильтров  
    3. Проверка добавления в базу данных различных записей  
    4. Попытка внести в базу некорректную запись  

Обнаруженные ошибки:  
**Проблема:** можно сделать несколько броней на одну и ту же койку.  
**Решение:** Обновление виджета, отвечающего за выбор койки, который будет принимать в себя номера только тех коек, которые не заняты. 

# <p align="center">**Безопасность**

Для защиты данных были созданы представления:  
```sql
    • create VIEW reservation_history as SELECT r.date_of_checkin, r.date_of_checkout, r.number_of_nights, r.total_price, c.id as client_id, c.name as client_name, c.surname as client_surname, c.phone_number as client_phone, w.id as admin_id, w.name as admin_name, b.id as bed_id, b.room_number, b.price_per_night as bed_price, rm.floor, rm.number_of_places FROM reservation r LEFT JOIN clients c ON r.client = c.id LEFT JOIN workers w ON r.administrator = w.id LEFT JOIN beds b ON r.bed = b.id LEFT JOIN rooms rm ON b.room_number = rm.number ORDER BY r.date_of_checkin DESC;   
    • create VIEW current_reservations as select rh.*, CasE when rh.date_of_checkout > CURRENT_DATE THEN rh.date_of_checkout - CURRENT_DATE ELSE 0 END as nights_remaining FROM reservation_history rh where CURRENT_DATE BETWEEN rh.date_of_checkin and rh.date_of_checkout ORDER BY rh.room_number;   
    • CREATE VIEW cleaning_schedule_view AS SELECT sc.date_of_cleaning, sc.room_number, r.floor, r.number_of_places, w.id as housemaid_id, w.name as housemaid_name, rol.name as housemaid_role, CASE WHEN sc.date_of_cleaning < CURRENT_DATE THEN 'Выполнена' WHEN sc.date_of_cleaning = CURRENT_DATE THEN 'На сегодня' ELSE 'Запланирована' END as cleaning_status FROM schedule_of_cleaning_rooms sc LEFT JOIN rooms r ON sc.room_number = r.number LEFT JOIN workers w ON sc.housemaid = w.id LEFT JOIN roles rol ON w.role = rol.id ORDER BY sc.date_of_cleaning, r.floor, sc.room_number;  
    • CREATE VIEW workers_info AS SELECT w.id, w.name as full_name, split_part(w.name, ' ', 1) as first_name, split_part(w.name, ' ', 2) as middle_name, split_part(w.name, ' ', 3) as last_name, r.id as role_id, r.name as role_name, FROM workers w LEFT JOIN roles r ON w.role = r.id ORDER BY r.id, w.name;  
```

# <p align="center">**Разработка стратегии резервного копирования**

Резервное копирование – процесс, целью которого является обеспечить возможность восстановления данных при сбое (аппаратном, человеческой ошибке и пр.) с минимальными потерями.

Сначала был воспроизведён полный бэкап всей базы данных:  
```pg_dump -U elesov elesov > elesovhosteldb_backup.sql```

Затем были созданы бэкапы отдельных таблиц:  
```
pg_dump -t reservation elesov > /tmp/reservationhostel.dump;  
pg_dump -t schedule_of_cleaning_rooms elesov > /tmp/ schedule_of_cleaning_rooms hostel.dump;
```

Также был создана копия python-файла, отвечавшего за графический пользовательский интерфейс.

# <p align="center">**Заключение**

В ходе выполнения курсовой работы была цель была достигнута. Создана простая система для управления гостиницей: реализованы простая и удобная база данных для управления гостиницей и подсистема для работы с клиентами в виде понятного пользовательского интерфейса.  
    1. Аналитическая часть:  
    • Проведён анализ предметной области  
    • Определены все требования и ограничения  
    2. Проектная часть  
    • Разработана концептуальная модель базы данных  
    • На основе этой концептуальной модели была разработана логическая структура  
    • На основе логической структуры была разработана физическая структура базы данных  
    3. Программная реализация:  
        ◦ Созданы база данных и запросы к ней в СУБД PostgreSQL  
        ◦ Разработан пользовательский интерфейс для упрощённого управления этой самой базой данных с помощью языка программирования Python  
        ◦ Были созданы резервные копии всех компонентов системы в случае сбоев  
Из ключевых характеристик системы можно выделить возможность добавления неограниченного количества записей, возможность фильтровать информацию, а также отображение простой и краткой статистики.  
Система полностью функционирует и может использоваться для управления гостиницей и её составляющими, в том числе и для работы с клиентами.  

# <p align="center">**Список литературы**  

    1. PostgreSQL: Documentation: 18 – https://www.postgresql.org/docs/current/  
    2. Руководство по работе с базами данных PostgreSQL – https://metanit.com/sql/postgresql/?ysclid=mj5wn2eii2901306410
    3. tkinter — Python interface to Tcl/Tk — Python 3.14.2 documentation – https://docs.python.org/3/library/tkinter.html
    4. Руководство по программированию на Tkinter и Python – https://metanit.com/python/tkinter/?ysclid=mj5wsjm2gu718044868
    5. psycopg2 · PyPI – https://pypi.org/project/psycopg2/
    6. Python и базы данных | Модуль psycopg. Подключение к серверу PostgreSQL – https://metanit.com/python/database/2.1.php?ysclid=mj5wuhzuvv34999340
    
# <p align="center">**Приложение**

Фрагмент кода
```python
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import psycopg2
from datetime import date, datetime
from tkcalendar import DateEntry  # pip(pip3) install tkcalendar


class HotelManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Система управления гостиницей")
        self.root.geometry("1200x700")

        # Параметры подключения к базе данных
        self.db_params = {
            'host': 'localhost', #127.0.0.1
            'database': 'test', #elesov
            'user': 'postgres', #elesov
            'password': '1224', #1224
            'port': '5432' #5432
        }

        self.setup_ui()
        self.connect_to_db()

    def setup_ui(self):
        # Создаем меню
        self.create_menu()

        # Создаем вкладки
        self.tab_control = ttk.Notebook(self.root)

        # Вкладка бронирования
        self.tab_reservation = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_reservation, text='Бронирование')
        self.setup_reservation_tab()

        # Вкладка клиенты
        self.tab_clients = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_clients, text='Клиенты')
        self.setup_clients_tab()

        # Вкладка номера
        self.tab_rooms = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_rooms, text='Номера')
        self.setup_rooms_tab()

        # Вкладка уборка
        self.tab_cleaning = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_cleaning, text='Уборка')
        self.setup_cleaning_tab()

        # Вкладка работники
        self.tab_workers = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_workers, text='Работники')
        self.setup_workers_tab()

        # Вкладка отчеты
        self.tab_reports = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_reports, text='Отчеты')
        self.setup_reports_tab()

        self.tab_control.pack(expand=1, fill="both")
```
