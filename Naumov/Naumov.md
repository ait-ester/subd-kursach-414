<p align="center">Министерство образования, науки и молодежной политики Республики Коми</p>

<p align="center">ГПОУ "Сыктывкарский политехнический техникум"</p>




<p align="center">Курсовая работа</p>


<p align="center">тема:БД коммерческого учебного центра "Юниум" </p>


<p align="right"> выполнил </p>

<p align="right">студент 4 курса </p>

<p align="right">414 группы </p>

<p align="right">Наумов Макарий Викторович</p>



<p align="right">проверил</p>

<p align="right">Пунгин И.В.</p>

<p align="right">дата проверки: </p>



<p align="center">Сыктывкар, 2025</p>


Специальность: 09.02.07 «Информационные системы и программирование»
Тема курсовой работы: База данных коммерческого учебного центра
Срок представления работы к защите: 22 декабря 2025 года
Перечень подлежащих разработке вопросов:
1.	Анализ предметной области. Постановка задачи.
1.1. Описание предметной области и функции решаемых задач.
1.2. Перечень входных данных.
1.3. Перечень выходных данных
1.4. Ограничения предметной области (если таковые имеются).
1.5. Взаимодействие с другими программами.
2.	Инфологическая (концептуальная) модель базы данных.
2.1. Выделение информационных объектов.
2.2. Определение атрибутов объектов.
2.3. Определение отношений и мощности отношений между объектами.
2.4. Построение концептуальной модели.
3.	Логическая структура БД.
4.	Физическая структура базы данных.
5.	Реализация проекта в среде конкретной СУБД.
5.1. Создание таблиц.
5.2. Создание запросов.
5.3. Разработка интерфейса.
5.4. Назначение прав доступа.
5.5. Создание индексов.
5.6. Разработка стратегии резервного копирования базы данных
Руководитель работы __________________И.В. Пунгин
Задание принял к исполнению ___________________________М.В. Наумов
 
Оглавление
ВВЕДЕНИЕ	4
1. АНАЛИЗ ПРЕДМЕТНОЙ ОБЛАСТИ. ПОСТАНОВКА ЗАДАЧИ	5
1.1. Описание предметной области и функции решаемых задач	5
1.2. Перечень входных данных	5
1.3. Перечень выходных данных	6
1.4. Ограничения предметной области	6
1.5. Взаимодействие с другими программами	6
2. ИНФОЛОГИЧЕСКАЯ (КОНЦЕПТУАЛЬНАЯ) МОДЕЛЬ БД	7
2.1. Выделение информационных объектов	7
2.2. Определение атрибутов объектов	7
2.3. Определение отношений и мощности отношений между объектами	11
2.4. Построение концептуальной модели (словесное описание)	12
3. ЛОГИЧЕСКАЯ СТРУКТУРА БАЗЫ ДАННЫХ	12
4. Физическая структура базы данных	18
4.1. Пользовательские типы данных	18
4.2. Описание таблиц базы данных	18
4.3. Схема структуры базы данных	23
5. РЕАЛИЗАЦИЯ ПРОЕКТА В СРЕДЕ КОНКРЕТНОЙ СУБД (POSTGRESQL)	23
5.1. Создание таблиц	23
5.2. Создание запросов	24
5.3. Разработка интерфейса	24
5.4. Назначение прав доступа	25
5.5. Создание индексов	25
5.6. Разработка стратегии резервного копирования базы данных	26
5.7. Стратегия защиты базы данных	26
5.8. Разработка API для работы с базой данных	26




 
ВВЕДЕНИЕ

В современном мире дополнительное образование становится неотъемлемой частью подготовки школьников и студентов к будущей профессиональной деятельности. Коммерческий учебный центр осуществляет образовательную деятельность, предоставляя широкий спектр курсов в сфере языковой подготовки, информационных технологий, художественного развития, а также тренингов, направленных на подготовку к государственным экзаменам (ОГЭ, ЕГЭ).
Актуальность: Управление учебными группами, расписанием, клиентской базой, финансовыми потоками и академическими результатами требует применения автоматизированных информационных систем, основанных на надёжных базах данных. Ручное ведение записей, распределения нагрузки преподавателей и учёт посещаемости становятся неэффективными при увеличении количества курсов и обучающихся. Это приводит к росту вероятности ошибок и снижению качества организационной работы.
Целью данной курсовой работы является разработка базы данных для коммерческого учебного центра, обеспечивающей хранение, поиск и обработку данных о курсах, студентах, преподавателях, расписании, оплатах и результатах обучения.
Для достижения цели необходимо решить следующие задачи:
•	провести анализ предметной области учебного центра;
•	выделить сущности базы данных и их атрибуты;
•	сформировать концептуальную (ER) модель;
•	разработать логическую модель базы данных;
•	спроектировать физическую структуру БД в PostgreSQL;
•	реализовать SQL-скрипты создания таблиц, индексов и ограничений;
•	разработать запросы демонстрации функциональности базы данных.
Разрабатываемая система должна обеспечить целостность данных, масштабируемость, защищённость и удобство использования в реальных условиях коммерческого учебного учреждения.



1. АНАЛИЗ ПРЕДМЕТНОЙ ОБЛАСТИ. ПОСТАНОВКА ЗАДАЧИ
1.1. Описание предметной области и функции решаемых задач
Коммерческий учебный центр осуществляет платные образовательные услуги по различным направлениям. Центр обслуживает клиентов (учеников), формирует учебные программы, заключает договоры, ведёт расчёты за обучение и учитывает результаты посещаемости и успеваемости.
Основные функции системы:
•	хранение информации об обучающихся;
•	хранение информации о преподавателях;
•	хранение данных об учебных курсах и направлениях;
•	ведение расписания занятий;
•	управление учебными группами;
•	учёт платежей за обучение;
•	фиксация посещаемости занятий;
•	хранение результатов обучения и оценок;
•	возможность просмотра статистики и аналитики.

1.2. Перечень входных данных
В систему вводятся следующие данные:
•	сведения об ученике: ФИО, возраст, контакты родителей, история обучения;
•	сведения о преподавателе: ФИО, специализация, контактные данные;
•	сведения о курсе: название, тип, длительность, стоимость;
•	расписание: дата, время, преподаватель, аудитория;
•	группа: курс + преподаватель + набор учеников;
•	финансовые данные: оплаты, задолженности, скидки;
•	оценки и результаты аттестаций.



1.3. Перечень выходных данных
Система должна формировать:
•	списки обучающихся по курсам;
•	расписание занятий на период (день, неделю, месяц);
•	отчёты по оплатам и задолженностям;
•	отчёты по посещаемости;
•	отчёты по успеваемости;
•	статистику по популярности курсов;
•	рейтинг преподавателей по загруженности.

1.4. Ограничения предметной области
•	один ученик может посещать несколько курсов одновременно;
•	один преподаватель может вести несколько различных курсов;
•	занятие всегда относится к конкретной группе;
•	нельзя записать ученика в группу, если в ней максимальное количество мест;
•	нельзя удалить преподавателя, если он ещё назначен на занятия;
•	нельзя удалить курс, если к нему привязаны активные группы;
•	доступ к финансовой информации должен быть ограничен;
•	операция оплаты должна фиксироваться с датой и суммой.

1.5. Взаимодействие с другими программами
На текущем этапе система автономна и взаимодействует только с PostgreSQL.
В будущем возможно расширение интеграции:
•	веб-интерфейс администратора и менеджеров;
•	CRM для маркетинговой аналитики;
•	LMS (Learning Management System);
•	платёжные системы (например, ЮKassa, СберПэй).

 
2. ИНФОЛОГИЧЕСКАЯ (КОНЦЕПТУАЛЬНАЯ) МОДЕЛЬ БД

2.1. Выделение информационных объектов
В результате анализа предметной области учебного центра «Юниум» были выделены следующие сущности:
1.	student — обучающийся
2.	roditel — родитель / законный представитель
3.	prepodavatel — преподаватель
4.	kategoriya_kursov — категория курса
5.	kurs — учебный курс
6.	gruppa — учебная группа
7.	zanyatie — занятие (урок)
8.	poseshchaemost — посещаемость
9.	oplata — оплата
10.	otsenka — оценка / результат обучения
11.	auditoriya — учебный кабинет
12.	administrator — администратор системы
13.	roditel_student — связь родителя со студентом (M:N)
14.	student_gruppa — связь студента с группой (M:N)

2.2. Определение атрибутов объектов
student
•	student_id (PK)
•	familiya
•	imya
•	otchestvo
•	data_rozhdeniya
•	telefon
•	email
•	data_registracii
•	status

roditel
•	roditel_id (PK)
•	familiya
•	imya
•	telefon
•	email
•	rodstvo

roditel_student
•	student_id (FK)
•	roditel_id (FK)

prepodavatel
•	prepodavatel_id (PK)
•	familiya
•	imya
•	telefon
•	email
•	specializaciya
•	data_nachala

kategoriya_kursov
•	kategoriya_id (PK)
•	nazvanie
•	opisanie


kurs
•	kurs_id (PK)
•	kategoriya_id (FK)
•	nazvanie
•	prodolzhitelnost_chasy
•	stoimost_mesyac
•	opisanie

gruppa
•	gruppa_id (PK)
•	kurs_id (FK)
•	prepodavatel_id (FK)
•	nazvanie
•	data_nachala
•	max_studentov

student_gruppa
•	student_id (FK)
•	gruppa_id (FK)
•	data_zachisleniya
•	status

zanyatie
•	zanyatie_id (PK)
•	gruppa_id (FK)
•	data_vremya
•	auditoriya_id (FK)
•	tema_zanyatiya

poseshchaemost
•	poseshchaemost_id (PK)
•	zanyatie_id (FK)
•	student_id (FK)
•	status (present / absent / late)

oplata
•	oplata_id (PK)
•	student_id (FK)
•	data
•	summa
•	tip_oplaty (nal / karta / online)
•	kommentariy

otsenka
•	otsenka_id (PK)
•	student_id (FK)
•	kurs_id (FK)
•	znachenie
•	data
•	kommentariy

auditoriya
•	auditoriya_id (PK)
•	nazvanie
•	vmestimost



administrator
•	administrator_id (PK)
•	username
•	password_hash
•	role
•	created_at

2.3. Определение отношений и мощности отношений между объектами
•	roditel 1 — M student
один родитель может относиться к нескольким студентам
student может иметь нескольких родителей
→ поэтому реализуем через таблицу roditel_student
•	student M — N gruppa
один student → может учиться в нескольких gruppa
одна gruppa → содержит многих student
→ реализуем через student_gruppa
•	prepodavatel 1 — M gruppa
один преподаватель ведёт несколько групп
•	kurs 1 — M gruppa
один курс может иметь несколько учебных групп
•	kategoriya_kursov 1 — M kurs
каждая категория включает несколько курсов
•	gruppa 1 — M zanyatie
в группе много занятий
•	zanyatie 1 — M poseshchaemost
одно занятие → несколько записей посещаемости
•	student 1 — M poseshchaemost
один student имеет много записей посещаемости
•	student 1 — M oplata
•	student 1 — M otsenka
•	auditoriya 1 — M zanyatie



2.4. Построение концептуальной модели (словесное описание)
База данных учебного центра должна обеспечивать хранение информации о студентах и их родителях, преподавателях, учебных курсах и категориях курсов. На основе курсов формируются учебные группы, которые ведутся преподавателями.
Для каждой группы проводится расписание занятий, фиксируемых в таблице zanyatie.
Посещаемость студентов учитывается в poseshchaemost. Оплаты обучения отражаются через таблицу oplata. Результаты обучения (оценки) фиксируются в таблице otsenka.
Для хранения информации об учебных помещениях используется таблица auditoriya. Права и доступ администраторов системы определяются таблицей administrator.

3. ЛОГИЧЕСКАЯ СТРУКТУРА БАЗЫ ДАННЫХ

Логическая структура базы данных отражает преобразование концептуальной ER-модели в систему взаимосвязанных отношений (таблиц) реляционного типа. На этом этапе выполняется нормализация отношений, выбираются типы данных, определяются первичные и внешние ключи, а также задаются ограничения целостности, необходимые для корректного функционирования базы данных коммерческого учебного центра.

Детальное логическое описание всех сущностей:
Таблица student
Хранит данные об учащихся учебного центра.
Атрибут	Тип данных	Назначение
student_id (PK)	SERIAL	Уникальный идентификатор студента
familiya	VARCHAR(50)	Фамилия
imya	VARCHAR(50)	Имя
otchestvo	VARCHAR(50)	Отчество
data_rozhdeniya	DATE	Дата рождения
telefon	VARCHAR(20)	Контактный телефон
email	VARCHAR(100), UNIQUE	Электронная почта
data_registracii	DATE	Дата регистрации
status	ENUM student_status	active / inactive

Таблица roditel
Хранит информацию о родителях (законных представителях).
Атрибут	Тип	Описание
roditel_id (PK)	SERIAL	Уникальный идентификатор
familiya	VARCHAR(50)	Фамилия
imya	VARCHAR(50)	Имя
telefon	VARCHAR(20)	Телефон
email	VARCHAR(100)	E-mail
rodstvo	VARCHAR(30)	Степень родства


Таблица roditel_student (связь M:N)
Позволяет одному студенту иметь нескольких родителей и наоборот.
Атрибут	Тип	Ключ
student_id	INT	FK → student
roditel_id	INT	FK → roditel
PK(student_id, roditel_id)

Таблица prepodavatel
Атрибут	Тип	Описание
prepodavatel_id (PK)	SERIAL	Уникальный ID
familiya	VARCHAR(50)	Фамилия
imya	VARCHAR(50)	Имя
telefon	VARCHAR(20)	Телефон
email	VARCHAR(100)	E-mail
specializaciya	VARCHAR(100)	Предмет/направление
data_nachala	DATE	Дата приема на работу


Таблица kategoriya_kursov
Описание категорий курсов.
Атрибут	Тип
kategoriya_id (PK)	SERIAL
nazvanie	VARCHAR(100)
opisanie	TEXT


Таблица kurs
Хранит информацию о курсах, таких как английский, программирование, ЕГЭ и др.
Атрибут	Тип	Ключ
kurs_id (PK)	SERIAL	
kategoriya_id	INT	FK → kategoriya_kursov
nazvanie	VARCHAR(100)	
prodolzhitelnost_chasy	INT	
stoimost_mesyac	NUMERIC(10,2)	
opisanie	TEXT	


Таблица gruppa
Отражает учебные группы (например, «Английский A1 вечер», «Подготовка к ОГЭ группа №2»).
Атрибут	Тип	Ключ
gruppa_id (PK)	SERIAL	
kurs_id	INT	FK → kurs
prepodavatel_id	INT	FK → prepodavatel
nazvanie	VARCHAR(100)	
data_nachala	DATE	
max_studentov	INT CHECK > 0	


Таблица student_gruppa (M:N)
Студент может посещать несколько групп, а в группе — несколько студентов.
Атрибут	Тип	Ключ
student_id	INT	FK → student
gruppa_id	INT	FK → gruppa
data_zachisleniya	DATE	
status	ENUM gruppa_zachislenie_status	
PK(student_id, gruppa_id)


Таблица auditoriya
Аудитории — места проведения занятий.
Атрибут	Тип
auditoriya_id (PK)	SERIAL
nazvanie	VARCHAR(50)
vmestimost	INT CHECK > 0


Таблица zanyatie
Содержит информацию о каждом конкретном занятии.
Атрибут	Тип	Ключ
zanyatie_id (PK)	SERIAL	
gruppa_id	INT	FK → gruppa
data_vremya	TIMESTAMP	
auditoriya_id	INT	FK → auditoriya
tema_zanyatiya	VARCHAR(200)	


Таблица poseshchaemost
Фиксация посещений студентов.
Атрибут	Тип	Ключ
poseshchaemost_id (PK)	SERIAL	
zanyatie_id	INT	FK → zanyatie
student_id	INT	FK → student
status	ENUM poseshchaemost_status	present / absent / late
UNIQUE(zanyatie_id, student_id)

Таблица oplata
Фиксация платежей учащихся.
Атрибут	Тип
oplata_id (PK)	SERIAL
student_id	INT FK → student
data	DATE
summa	NUMERIC(12,2) CHECK > 0
tip_oplaty	ENUM tip_oplaty
kommentariy	TEXT


Таблица otsenka
Хранит итоговые и тематические оценки студентов.
Атрибут	Тип
otsenka_id (PK)	SERIAL
student_id	INT FK → student
kurs_id	INT FK → kurs
znachenie	INT CHECK 1–100
data	DATE
kommentariy	TEXT


Таблица administrator
Таблица учетных записей администраторов системы.
Атрибут	Тип
administrator_id (PK)	SERIAL
username	VARCHAR(50) UNIQUE
password_hash	TEXT
role	ENUM administrator_role
created_at	TIMESTAMP


 
4. Физическая структура базы данных
Физическая структура базы данных представляет собой итоговое представление сущностей предметной области в виде конкретных таблиц, хранящихся в системе управления базами данных PostgreSQL. На данном этапе логическая модель преобразуется в набор SQL-объектов, включающих таблицы, первичные и внешние ключи, ограничения целостности, типы данных и пользовательские перечислимые типы (ENUM).
В данном разделе приводится описание созданных таблиц, их атрибутов, а также связей между ними, сформированных в соответствии с реляционной моделью данных и требованиями предметной области коммерческого учебного центра.

4.1. Пользовательские типы данных
Для повышения целостности данных и ограничения допустимых значений в базе данных были созданы пользовательские типы ENUM. Их использование позволяет гарантировать корректность вводимой информации и исключить логические ошибки (например, неверный статус студента или способ оплаты):
CREATE TYPE student_status AS ENUM ('active', 'inactive');
CREATE TYPE poseshchaemost_status AS ENUM ('present', 'absent', 'late');
CREATE TYPE tip_oplaty AS ENUM ('nal', 'karta', 'online');
CREATE TYPE gruppa_zachislenie_status AS ENUM ('active', 'finished', 'expelled');
CREATE TYPE administrator_role AS ENUM ('admin', 'manager', 'auditor');

4.2. Описание таблиц базы данных

Таблица student (Учащиеся):
CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    familiya VARCHAR(50) NOT NULL,
    imya VARCHAR(50) NOT NULL,
    otchestvo VARCHAR(50),
    data_rozhdeniya DATE NOT NULL,
    telefon VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    data_registracii DATE DEFAULT CURRENT_DATE,
    status student_status DEFAULT 'active'
);

Таблица roditel (Родители/законные представители):
CREATE TABLE roditel (
    roditel_id SERIAL PRIMARY KEY,
    familiya VARCHAR(50) NOT NULL,
    imya VARCHAR(50) NOT NULL,
    telefon VARCHAR(20),
    email VARCHAR(100),
    rodstvo VARCHAR(30) NOT NULL
);

Таблица roditel_student (Связь M:N между родителями и учащимися):
CREATE TABLE roditel_student (
    student_id INT REFERENCES student(student_id) ON DELETE CASCADE,
    roditel_id INT REFERENCES roditel(roditel_id) ON DELETE CASCADE,
    PRIMARY KEY (student_id, roditel_id)
);

Таблица prepodavatel (Преподаватели):
CREATE TABLE prepodavatel (
    prepodavatel_id SERIAL PRIMARY KEY,
    familiya VARCHAR(50) NOT NULL,
    imya VARCHAR(50) NOT NULL,
    telefon VARCHAR(20),
    email VARCHAR(100),
    specializaciya VARCHAR(100),
    data_nachala DATE NOT NULL
);

Таблица kategoriya_kursov (Категории курсов):
CREATE TABLE kategoriya_kursov (
    kategoriya_id SERIAL PRIMARY KEY,
    nazvanie VARCHAR(100) NOT NULL,
    opisanie TEXT
);

Таблица kurs (Курсы):
CREATE TABLE kurs (
    kurs_id SERIAL PRIMARY KEY,
    kategoriya_id INT REFERENCES kategoriya_kursov(kategoriya_id) ON DELETE SET NULL,
    nazvanie VARCHAR(100) NOT NULL,
    prodolzhitelnost_chasy INT NOT NULL,
    stoimost_mesyac NUMERIC(10,2) NOT NULL,
    opisanie TEXT
);

Таблица gruppa (Учебные группы): CREATE TABLE gruppa (
    gruppa_id SERIAL PRIMARY KEY,
    kurs_id INT REFERENCES kurs(kurs_id) ON DELETE CASCADE,
    prepodavatel_id INT REFERENCES prepodavatel(prepodavatel_id) ON DELETE SET NULL,
    nazvanie VARCHAR(100) NOT NULL,
    data_nachala DATE NOT NULL,
    max_studentov INT CHECK (max_studentov > 0)
);

Таблица student_gruppa (Записи о зачислении студентов в группы, M:N):
CREATE TABLE student_gruppa (
    student_id INT REFERENCES student(student_id) ON DELETE CASCADE,
    gruppa_id INT REFERENCES gruppa(gruppa_id) ON DELETE CASCADE,
    data_zachisleniya DATE DEFAULT CURRENT_DATE,
    status gruppa_zachislenie_status DEFAULT 'active',
    PRIMARY KEY (student_id, gruppa_id)
);

Таблица auditoriya (Учебные аудитории):
CREATE TABLE auditoriya (
    auditoriya_id SERIAL PRIMARY KEY,
    nazvanie VARCHAR(50) NOT NULL,
    vmestimost INT CHECK (vmestimost > 0)
);

Таблица zanyatie (Занятия):
CREATE TABLE zanyatie (
    zanyatie_id SERIAL PRIMARY KEY,
    gruppa_id INT REFERENCES gruppa(gruppa_id) ON DELETE CASCADE,
    data_vremya TIMESTAMP NOT NULL,
    auditoriya_id INT REFERENCES auditoriya(auditoriya_id) ON DELETE SET NULL,
    tema_zanyatiya VARCHAR(200)
);

Таблица poseshchaemost (Посещаемость занятий):
CREATE TABLE poseshchaemost (
    poseshchaemost_id SERIAL PRIMARY KEY,
    zanyatie_id INT REFERENCES zanyatie(zanyatie_id) ON DELETE CASCADE,
    student_id INT REFERENCES student(student_id) ON DELETE CASCADE,
    status poseshchaemost_status NOT NULL,
    UNIQUE (zanyatie_id, student_id)
);

Таблица oplata (Оплаты):
CREATE TABLE oplata (
    oplata_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES student(student_id) ON DELETE CASCADE,
    data DATE DEFAULT CURRENT_DATE,
    summa NUMERIC(12,2) NOT NULL CHECK (summa > 0),
    tip_oplaty tip_oplaty NOT NULL,
    kommentariy TEXT
);

Таблица otsenka (Оценки по курсам):
CREATE TABLE otsenka (
    otsenka_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES student(student_id) ON DELETE CASCADE,
    kurs_id INT REFERENCES kurs(kurs_id) ON DELETE CASCADE,
    znachenie INT CHECK (znachenie BETWEEN 1 AND 100),
    data DATE DEFAULT CURRENT_DATE,
    kommentariy TEXT
);

Таблица administrator (Администраторы учебного центра):
CREATE TABLE administrator (
    administrator_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role administrator_role DEFAULT 'manager',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

 4.3. Схема структуры базы данных


5. РЕАЛИЗАЦИЯ ПРОЕКТА В СРЕДЕ КОНКРЕТНОЙ СУБД (POSTGRESQL)
5.1. Создание таблиц 
На основе разработанной логической структуры базы данных были созданы таблицы PostgreSQL с использованием инструкций CREATE TABLE, а также дополнительных объектов — ENUM, внешних ключей, ограничений целостности и проверок.
В процессе реализованы:
•	все сущности предметной области: student, roditel, prepodavatel, kurs, gruppa, zanyatie, poseshchaemost, oplata, otsenka, administrator и др.;
•	связи 1:M и M:N, реализованные через внешние ключи и таблицы-связки;
•	типы ENUM для статусов студентов, посещаемости, типов оплаты, ролей администратора и статусов зачисления в группы;
•	каскадное поведение (ON DELETE CASCADE, ON DELETE SET NULL) для обеспечения корректности данных.

5.2. Создание запросов
Для проверки корректности работы БД и обеспечения функционала учебного центра были разработаны следующие группы SQL-запросов:
1.	Запросы выборки:
o	получение списка студентов, зачисленных в определённую группу;
o	просмотр расписания занятий группы;
o	вывод посещаемости студента;
o	вывод оплат за выбранный период;
o	получение перечня курсов и их стоимости.
2.	Запросы вставки (INSERT):
o	добавление новых студентов и родителей;
o	создание групп и расписания занятий;
o	регистрация оплат и оценок.
3.	Запросы обновления (UPDATE):
o	изменение контактной информации студента;
o	изменение статуса учащегося;
o	исправление даты занятия или аудитории.
4.	Запросы удаления (DELETE):
o	удаление студента с каскадным удалением записей посещаемости и связей с родителями;
o	удаление занятия.

5.3. Разработка интерфейса


5.4. Назначение прав доступа
Для обеспечения безопасности данных разработана структура ролей PostgreSQL.
Реализовано:
1.	Роль администратора (admin_role)
o	полный доступ к базе данных;
o	возможность создавать таблицы и управлять пользователями.
2.	Роль менеджера (manager_role)
o	работа со студентами, группами, расписанием;
o	запрет на удаление таблиц и изменение системных объектов.
3.	Роль аудитора (auditor_role)
o	разрешено только чтение всех данных.
4.	Назначение прав:
o	GRANT SELECT, INSERT, UPDATE для менеджера;
o	GRANT SELECT для аудитора;

5.5. Создание индексов
Для ускорения выполнения запросов были созданы индексы на тех столбцах, где часто выполняется поиск или соединение таблиц:
•	student(email) — поиск по email;
•	roditel_student(student_id, roditel_id) — оптимизация связки M:N;
•	gruppa(kurs_id) и gruppa(prepodavatel_id) — ускорение выборки групп;
•	zanyatie(gruppa_id) — ускорение получения расписания;
•	poseshchaemost(zanyatie_id, student_id) — контроль уникальности и быстроты запросов;
•	oplata(student_id);
•	otsenka(student_id, kurs_id).
Индексы создавались командой CREATE INDEX.


5.6. Разработка стратегии резервного копирования базы данных
Для обеспечения сохранности данных разработана стратегия backup:
1.	Полный резервный бэкап базы:
pg_dump -U postgres -F c -b -v -f /home/user/backups/unium_db.backup unium_db
2.	Периодичность резервирования:
o	полный бэкап — 1 раз в сутки;
o	ежечасные архивы WAL (журналы транзакций);
o	хранение копий 7–30 дней.
3.	Место хранения:
o	локальный сервер;
o	облачное хранилище (при необходимости).
4.	Восстановление базы:
pg_restore -U postgres -d unium_db /home/user/backups/unium_db.backup

5.7. Стратегия защиты базы данных
Для защиты данных реализованы следующие меры:
1. Использование ролей и разделение прав
Созданы роли admin, manager, auditor.
2. Шифрование паролей
Администратор хранит пароль в виде хеша.
3. Регулярные бэкапы (см. пункт 5.6)

5.8. Разработка API для работы с базой данных




