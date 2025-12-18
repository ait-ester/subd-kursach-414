<div align="center">

<h4>Министерство образования, науки и молодежной политики Республики Коми</h4>
<h4>ГПОУ «Сыктывкарский политехнический техникум»</h4>

<br>

<h2>Курсовая работа</h2>

<br>

<h2>Разработка БД для спортивной школы</h2>

<br>

</div>

<br><br>

<div align="right">

<b>выполнил:</b><br>
студентка 4 курса<br>
414 группы<br>
Сенькина Анастасия Владимировна

<br><br>

<b>проверил:</b><br>
Пунгин И.В.

<br><br>

<b>дата проверки:</b> ___________

</div>

<br><br><br>

<div align="center">
Сыктывкар, 2025 г.

</div>

---

<h2>Содержание</h2>

<ul>
  <li><a href="#введение">Введение</a></li>
  <li>
    <a href="#1-анализ-предметной-области-постановка-задачи">
      1. Анализ предметной области. Постановка задачи
    </a>
    <ul>
      <li>
        <a href="#11-описание-предметной-области-и-функции-решаемых-задач">
          1.1. Описание предметной области и функции решаемых задач
        </a>
      </li>
      <li>
        <a href="#12-перечень-входных-данных">
          1.2. Перечень входных данных
        </a>
      </li>
      <li>
        <a href="#13-перечень-выходных-данных">
          1.3. Перечень выходных данных
        </a>
      </li>
      <li>
        <a href="#14-ограничения-предметной-области">
          1.4. Ограничения предметной области
        </a>
      </li>
      <li>
        <a href="#15-взаимодействие-с-другими-программами">
          1.5. Взаимодействие с другими программами
        </a>
      </li>
    </ul>
  </li>

  <li>
    <a href="#2-инфологическая-концептуальная-модель-базы-данных">
      2. Инфологическая (концептуальная) модель базы данных
    </a>
    <ul>
      <li>
        <a href="#21-выделение-информационных-объектов">
          2.1. Выделение информационных объектов
        </a>
      </li>
      <li>
        <a href="#22-определение-атрибутов-объектов">
          2.2. Определение атрибутов объектов
        </a>
      </li>
      <li>
        <a href="#23-определение-отношений-и-мощности-отношений-между-объектами">
          2.3. Определение отношений и мощности отношений между объектами
        </a>
      </li>
      <li>
        <a href="#24-построение-концептуальной-модели">
          2.4. Построение концептуальной модели
        </a>
      </li>
    </ul>
  </li>

  <li><a href="#3-логическая-структура-бд">3. Логическая структура БД</a></li>
  <li><a href="#4-физическая-структура-базы-данных">4. Физическая структура базы данных</a></li>

  <li>
    <a href="#5-реализация-проекта-в-среде-конкретной-субд">
      5. Реализация проекта в среде конкретной СУБД
    </a>
    <ul>
      <li><a href="#51-создание-таблиц">5.1. Создание таблиц</a></li>
      <li><a href="#52-создание-запросов">5.2. Создание запросов</a></li>
      <li><a href="#53-разработка-интерфейса">5.3. Разработка интерфейса</a></li>
      <li><a href="#54-назначение-прав-доступа">5.4. Назначение прав доступа</a></li>
      <li><a href="#55-создание-индексов">5.5. Создание индексов</a></li>
      <li>
        <a href="#56-разработка-стратегии-резервного-копирования-базы-данных">
          5.6. Разработка стратегии резервного копирования базы данных
        </a>
      </li>
      <li>
        <a href="#57-разработка-стратегии-защиты-базы-данных-и-хранимой-в-ней-информации">
          5.7. Разработка стратегии защиты базы данных и хранимой в ней информации
        </a>
      </li>
      <li>
        <a href="#58-разработка-api-реализующего-работу-с-базой-данных-стороннего-приложения">
          5.8. Разработка API, реализующего работу с базой данных стороннего приложения
        </a>
      </li>
    </ul>
  </li>

  <li><a href="#заключение">Заключение</a></li>
  <li><a href="#список-использованных-информационных-источников">Список использованных информационных источников</a></li>
  <li><a href="#приложения">Приложения</a></li>
</ul>

---

<h2 id="введение">Введение</h2>

<p>В условиях современного развития спорта и повышения внимания к здоровому образу жизни спортивные школы играют ключевую роль в подготовке нового поколения спортсменов. Деятельность спортивной школы связана с обработкой больших объемов структурированной информации: данные о воспитанниках и их родителях, тренерском составе, расписании занятий, спортивных нормативах, результатах соревнований, финансовых операциях (оплата тренировок, абонементов). Ручное ведение учета в журналах и таблицах неэффективно, ведет к потере данных, ошибкам в расчетах, сложностям в формировании отчетности и планировании тренировочного процесса.</p>

<p>Автоматизация учета с помощью специализированной информационной системы на основе реляционной базы данных является необходимым решением для повышения эффективности управления спортивной школой. Такая система обеспечит целостность и безопасность данных, оперативный доступ к информации для администрации, тренеров и родителей, а также позволит анализировать успеваемость и динамику развития спортсменов.</p>

<p><strong>Целью данной курсовой работы</strong> является проектирование, реализация и внедрение комплексной реляционной базы данных для управления всеми основными процессами спортивной школы.</p>

<p><strong>Задачи работы:</strong></p>
<ul>
    <li>Провести анализ предметной области спортивной школы и сформулировать требования к информационной системе.</li>
    <li>Разработать инфологическую (ER), логическую и физическую модели базы данных.</li>
    <li>Реализовать базу данных в СУБД PostgreSQL с созданием всех необходимых таблиц, связей, индексов, триггеров и хранимых процедур.</li>
    <li>Разработать веб-интерфейс на PHP с использованием фреймворка Bootstrap для интуитивного управления данными.</li>
    <li>Реализовать систему аутентификации и авторизации с разграничением прав доступа (администратор, бухгалтер, тренер, родитель).</li>
    <li>Внедрить механизмы защиты данных и стратегию резервного копирования.</li>
    <li>Заполнить базу данных тестовыми данными для демонстрации функциональности.</li>
</ul>

<p><strong>Актуальность темы</strong> обусловлена повсеместной цифровизацией сферы образования и спорта, необходимостью оптимизации административных процессов в спортивных школах и повышением требований к качеству предоставляемых услуг и отчетности перед контролирующими органами.</p>

<div class="page-break"></div>

<h2 id="1-анализ-предметной-области-постановка-задачи">1. Анализ предметной области. Постановка задачи</h2>

<h3 id="11-описание-предметной-области-и-функции-решаемых-задач">1.1. Описание предметной области и функции решаемых задач</h3>

<p><strong>Предметная область</strong> – деятельность муниципальной или частной спортивной школы, занимающейся подготовкой юных спортсменов по различным видам спорта (плавание, гимнастика, футбол, борьба и т.д.). Школа ведет набор детей в группы, проводит регулярные тренировки, участвует в соревнованиях, осуществляет финансовые расчеты с родителями и выплаты тренерам.</p>

<p><strong>Основные бизнес-процессы:</strong></p>
<ol>
    <li><strong>Управление контингентом учащихся:</strong> Ведение личных дел воспитанников (анкетные данные, медицинские допуски, контакты родителей), зачисление/отчисление, перевод между группами.</li>
    <li><strong>Управление тренерско-преподавательским составом (ТПС):</strong> Учет сотрудников, их квалификации, нагрузки, графика работы, начисление заработной платы.</li>
    <li><strong>Формирование расписания и групп:</strong> Создание учебно-тренировочных групп по видам спорта, возрастам, уровням подготовки. Составление расписания занятий с учетом доступности спортивных объектов (залов, бассейнов) и тренеров.</li>
    <li><strong>Учет посещаемости и успеваемости:</strong> Фиксация посещения тренировок, контроль выполнения нормативов, ведение дневников спортсменов, отслеживание динамики результатов.</li>
    <li><strong>Организация и учет соревнований:</strong> Регистрация воспитанников на соревнования (внутришкольные, городские, региональные), внесение и анализ их результатов, учет полученных наград и разрядов.</li>
    <li><strong>Финансовый учет:</strong> Формирование тарифов и абонементов, прием оплаты за обучение, формирование платежных документов, учет расходов.</li>
    <li><strong>Формирование отчетности:</strong> Автоматическое формирование отчетов для руководства, статистических форм для вышестоящих организаций (например, отчет по сдаче норм ГТО), индивидуальных отчетов для родителей.</li>
</ol>

<h3 id="12-перечень-входных-данных">1.2. Перечень входных данных</h3>

<ul>
    <li><strong>Данные о воспитанниках:</strong> ФИО, дата рождения, пол, адрес, телефон, данные о здоровье (мед. допуск, группа здоровья), ФИО родителей/законных представителей, их контакты.</li>
    <li><strong>Данные о сотрудниках (тренерах, администрации):</strong> ФИО, должность, квалификация (разряд, звание), контактные данные, паспортные данные, ИНН, данные для расчета зарплаты.</li>
    <li><strong>Данные о видах спорта и программах:</strong> Название вида спорта, описание, возрастные категории, нормативы (для различных разрядов, лет).</li>
    <li><strong>Данные о группах:</strong> Название группы, вид спорта, тренер, возрастной диапазон, максимальная численность, время тренировок.</li>
    <li><strong>Данные о расписании:</strong> Группа, дата и время занятия, место проведения (зал, бассейн), тема занятия.</li>
    <li><strong>Данные о посещаемости:</strong> Воспитанник, дата занятия, отметка о присутствии/причине отсутствия.</li>
    <li><strong>Данные о соревнованиях:</strong> Название, дата, место проведения, уровень (внутришкольные, муниципальные и т.д.).</li>
    <li><strong>Данные о результатах:</strong> Воспитанник, соревнование, занятое место, выполненный норматив, присвоенный разряд.</li>
    <li><strong>Финансовые данные:</strong> Тарифы на обучение, данные об оплате (сумма, дата, период, способ оплаты), данные о начислении зарплаты тренерам..</li>
</ul>

<h3 id="13-перечень-выходных-данных">1.3. Перечень выходных данных</h3>

<ul>
    <li><strong>Списки групп и расписания:</strong> Для размещения на сайте и информационном стенде.</li>
    <li><strong>Статистические отчеты:</strong> Отчет о численности по видам спорта, отчет по выполнению нормативов, динамика результатов воспитанников.</li>
    <li><strong>Автоматические уведомления:</strong> Напоминания родителям об оплате, информация о предстоящих соревнованиях, изменениях в расписании (SMS/email).</li>
            <li>Индивидуальные карточки воспитанников и тренеров.</li>
            <li>Журналы посещаемости и успеваемости по группам.</li>
            <li>Протоколы соревнований и рейтинговые таблицы.</li>
            <li>Квитанции и договоры на оказание услуг.</li>
        </ul>
    </li>
    <li><strong>Финансовые отчёты:</strong> Отчет о платежах за период, задолженности родителей, отчет по выплатам тренерам.</li>
</ul>

<h3 id="14-ограничения-предметной-области">1.4. Ограничения предметной области </h3>

<ol>
    <li><strong>Возрастные ограничения:</strong> Воспитанник может быть зачислен в группу только если его возраст соответствует возрастному диапазону группы.</li>
    <li><strong>Вместимость групп:</strong> Количество воспитанников в группе не может превышать установленный максимум (санитарные нормы).</li>
    <li><strong>Конфликты расписания:</strong> Один тренер или одно спортивное сооружение не могут быть заняты двумя группами одновременно.</li>
    <li><strong>Финансовые ограничения:</strong> Воспитанник без оплаты за текущий месяц может быть не допущен к занятиям (определяется политикой школы).</li>
    <li><strong>Квалификационные ограничения:</strong> Тренер может вести группы только по тем видам спорта, по которым у него есть подтвержденная квалификация.</li>
    <li><strong>Медицинские ограничения:</strong> Воспитанник без действующего медицинского допуска не может быть включен в списки на соревнования.</li>

<h3 id="15-взаимодействие-с-другими-программами">1.5. Взаимодействие с другими программами</h3>

<ol>
    <li><strong>Платежные системы и банк-клиенты:</strong> Для приема оплаты через онлайн-банкинг или платежные терминалы.</li>
    <li><strong>Серверы электронной почты (SMTP) и SMS-шлюзы:</strong> Для массовых рассылок уведомлений.</li>
    <li><strong>Офисные пакеты (MS Excel, Word):</strong> Экспорт отчетов для дальнейшего форматирования.</li>
    <li><strong>Бухгалтерские системы (1С:Бухгалтерия):</strong> Выгрузка данных о начислениях и платежах для ведения бухгалтерского учета.</li>
    <li><strong>Ведомственные системы:</strong> Выгрузка отчетных форм в системы управления спортом муниципалитета или региона.</li>
</ol>

<div class="page-break"></div>

<h2 id="2-инфологическая-концептуальная-модель-базы-данных">2. Инфологическая (концептуальная) модель базы данных</h2>

<h3 id="21-выделение-информационных-объектов">2.1. Выделение информационных объектов</h3>

<p>В результате анализа предметной области были выделены следующие ключевые <strong>сущности (информационные объекты)</strong> системы:</p>

<ol>
    <li><strong>Athlete (Воспитанник):</strong> Основной субъект обучения.</li>
    <li><strong>Parent (Родитель/Представитель):</strong> Законный представитель воспитанника.</li>
    <li><strong>Employee (Сотрудник):</strong> Общая сущность для всех работников школы.</li>
    <li><strong>Trainer (Тренер):</strong> Специализация сотрудника. Ведущий группы.</li>
    <li><strong>SportType (Вид спорта):</strong> Справочник (плавание, футбол, дзюдо и т.д.).</li>
    <li><strong>TrainingGroup (Учебная группа):</strong> Сформированная группа для занятий.</li>
    <li><strong>Schedule (Расписание):</strong> Конкретное занятие группы.</li>
    <li><strong>Attendance (Посещаемость):</strong> Факт посещения занятия воспитанником.</li>
    <li><strong>Competition (Соревнование):</strong> Мероприятие.</li>
    <li><strong>Result (Результат):</strong> Достижение воспитанника на соревновании или контрольной тренировке.</li>
    <li><strong>Norm (Норматив):</strong> Требуемый показатель для сдачи разряда.</li>
    <li><strong>Payment (Платёж):</strong> Оплата за обучение.</li>
    <li><strong>Tariff (Тариф):</strong> Стоимость обучения в группе за период.</li>
</ol>

<h3 id="22-определение-атрибутов-объектов">2.2. Определение атрибутов объектов</h3>

<table>
    <tr><th>Сущность</th><th>Ключевые атрибуты</th></tr>
    <tr><td><strong>Athlete</strong></td><td><code>athlete_id (PK)<code>, <code>last_name</code>, <code>first_name</code>, <code>birth_date</code>, <code>medical_certificate_date</code>, <code>tparent_id</code> (FK)
    <tr><td><strong>Parent</strong></td><td><code>parent_id</code> (PK), <code>last_name</code>, <code>first_name</code>, <code>phone</code>, <code>email</code>
    <tr><td><strong>Trainer</strong></td><td><code>trainer_id</code> (PK), <code>employee_id</code> (FK), <code>sport_type_id</code> (FK), <code>qualification_category</code>
    <tr><td><strong>TrainingGroup</strong></td><td><code>group_id</code> (PK), <code>group_name</code>, <code>sport_type_id</code> (FK), <code>trainer_id</code> (FK), <code>min_age</code>, <code>max_age</code>, <code>max_size</code>
    <tr><td><strong>Schedule</strong></td><td><code>schedule_id</code> (PK), <code>group_id</code> (FK), <code>lesson_date</code>, <code>start_time</code>, <code>end_time</code>, <code>location</code>
    <tr><td><strong>Attendance</strong></td><td><code>attendance_id</code> (PK), <code>bathlete_id</code> (FK), <code>schedule_id</code> (FK), <code>status</code> (присутствовал/отсутствовал/болел)
    <tr><td><strong>Payment</strong></td><td><code>payment_id</code> (PK), <code>athlete_id</code> (FK), <code>tariff_id</code> (FK), <code>amount</code>, <code>payment_date</code>, <code>period_month</code>, <code>), tariff_id (FK), amount, payment_date, period_month, period_year</code>
</table>

<h3 id="23-определение-отношений-и-мощности-отношений">2.3. Определение отношений и мощности отношений</h3>

<ol>
    <li><strong>Parent (1) — (M) Athlete:</strong> У одного родителя может быть несколько детей в школе. Один воспитанник связан с одним или двумя родителями. Мощность: <strong>1:M</strong>.</li>
    <li><strong>Athlete (M) — (М) TrainingGroup:</strong> Воспитанник может заниматься в нескольких группах (например, основная и ОФП), и в группе много воспитанников. Разрешается через таблицу-ассоциацию <code>GroupEnrollment</code>. Мощность: <strong>M:М</strong>.</li>
    <li><strong>TrainingGroup (1) — (М) Schedule:</strong> На одну группу составляется много занятий по расписанию. Мощность: <strong>1:М</strong>.</li>
    <li><strong>Schedule (1) — (М) Attendance:</strong> На одном занятии отмечается посещаемость многих воспитанников. Мощность: <strong>1:М</strong>.</li>
    <li><strong>Athlete (1) — (M) Result:</strong> Один воспитанник имеет много результатов на соревнованиях. Мощность: <strong>1:М</strong>.</li>
    <li><strong>Competition (1) — (М) Result:</strong> На одних соревнованиях фиксируются результаты многих участников. Мощность: <strong>1:М</strong>.</li>
    <li><strong>SportType (1) — (M) TrainingGroup / Norm:</strong> Один вид спорта имеет много групп и много нормативов. Мощность: <strong>1:M</strong>.</li>
    <li><strong>Trainer (1) — (M) TrainingGroup:</strong> Один тренер может вести несколько групп. Мощность: <strong>1:M</strong>.</li>
</ol>

<h3 id="24-построение-концептуальной-модели">2.4. Построение концептуальной модели</h3>

<p>Ниже представлена текстовая версия ER-диаграммы (нотация Чена), отображающая ключевые сущности и связи между ними. Полная графическая диаграмма прилагается отдельно.</p>

<pre>
    +-------------+       +-------------+       +---------------+
    |    Parent   |1      |   Athlete   |M      |  Competition  |
    +-------------+       +-------------+       +---------------+
    | parent_id   |       | athlete_id  |       |competition_id |
    | ...         |       |parent_id(FK)|       |  ...          |
    +-------------+       +------+------+       +---------------+
                                 |                      |
                                 | М                    | М
                         +-------+-------+        +-----+-------+
                         | GroupEnrollment|       |   Result    |
                         +---------------+        +-------------+
                         | athlete_id(FK)|        | result_id   |
                         | group_id(FK)  |        | athlete_id  |
                         | enroll_date   |        |competition_id
                         +-------+-------+        | value       |
                                 |                +-------------+
                                 | М
                         +-------+-------+
            М            |TrainingGroup |1
    +---------------+----+-------+-------+
    |   Schedule    |    | group_id(PK)  |
    +---------------+    | trainer_id(FK)|
    | schedule_id   |    | sport_type_id |
    | group_id(FK)  |<>--+ ...           |
    | ...           |    +-------+-------+
    +-------+-------+            |
            | М                  |1
    +-------+-------+    +-------+-------+
    |  Attendance   |    |   Trainer     |
    +---------------+    +---------------+
    | attendance_id |    | trainer_id(PK)|
    | athlete_id(FK)|    | employee_id(FK)
    |schedule_id(FK)|    | ...           |
    | ...           |    +-------+-------+
    +---------------+            |
                                 |1
                         +-------+------+
                         |  SportType   |
                         +--------------+
                         | sport_type_id|
                         | name         |
                         +--------------+
</pre>


<div class="page-break"></div>


<h2 id="3-логическая-структура-бд">3. Логическая структура БД</h2>

<p>Логическая модель преобразует ER-диаграмму в схему реляционных таблиц. Все связи реализуются через внешние ключи (FOREIGN KEY). При проектировании соблюдены принципы нормализации до третьей нормальной формы (3NF), что устраняет избыточность и аномалии обновления.</p>

<p><strong>Сознательная денормализация применена для производительности</strong>:</p>
<ol>
    <li><strong>Таблица Athlete:</strong> Содержит поле <code>current_group_id</code> для быстрого определения основной группы воспитанника, хотя это можно вычислить через <code>GroupEnrollment</code>.</li>
    <li><strong>Таблица TrainingGroup:</strong> Содержит поле <code>current_size</code> (текущее количество), которое должно обновляться триггером при зачислении/отчислении, чтобы избежать подсчета <code>COUNT(*)</code> в частых запросах.</li>
</ol>

<p>Данные денормализованные поля должны обновляться с помощью триггеров или фоновых задач (cron), чтобы обеспечить их актуальность.</p>

<div class="page-break"></div>

<h2 id="4-физическая-структура-базы-данных">4. Физическая структура базы данных</h2>

<h3>4.1. Выбор СУБД и обоснование</h3>
<p>Выбрана СУБД <strong>PostgreSQL 15+</strong> по следующим причинам:</p>
<ul>
    <li><strong>Открытая лицензия</strong></li>
    <li><strong>Соответствие ACID</strong></li>
    <li><strong>Высокая надежность</strong></li>
    <li><strong>Поддержка сложных типов данных (JSONB, массивы)</strong></li>
    <li><strong>Развитые механизмы репликации и резервного копирования</strong></li>
</ul>

<h3>4.2. Типы данных PostgreSQL:</h3>
<table>
    <tr><th>Тип данных PostgreSQL</th><th>Применение</th><th>Пример поля</th></tr>
    <tr><td><code>SERIAL</code> / <code>BIGSERIAL</code></td><td>Первичные ключи.</td><td><code>athlete_id SERIAL PRIMARY KEY</code></td></tr>
    <tr><td><code>VARCHAR(n)</code> / <code>TEXT</code></td><td>Текст: для имён, телефонов; для заметок.</td><td><code>last_name VARCHAR(100)</code>, <code>notes TEXT</code></td></tr>
    <tr><td><code>INTEGER</code> / <code>DECIMAL(10,2)</code></td><td>Числа: для возрастов, количеств; для финансовых сумм.</td><td><code>age INTEGER</code>, <code>amount DECIMAL(10,2)</code></td></tr>
    <tr><td><code>DATE</code> / <code>TIMESTAMPTZ</code></td><td>Даты/время: (дата рождения), (метка создания).</td><td><code>birth_date DATE</code>, <code>created_at TIMESTAMPTZ</code></td></tr>
    <tr><td><code>BOOLEAN</code></td><td>Логика.</td><td><code>is_active BOOLEAN</code></td></tr>
</table>

<h3>4.3. Стратегия резервного копирования</h3>
<p>Для обеспечения отказоустойчивости и возможности восстановления данных после сбоя разработана многоуровневая стратегия:</p>
<ol>
    <li><strong>Ежедневные полные резервные копии (Full Backup):</strong> Выполняются ежедневно в 02:00 ночи (время минимальной нагрузки) с помощью утилиты <code>pg_dump</code> в custom-формате (сжатие, параллельность). Хранятся 7 последних копий на выделенном сервере.</li>
    <li><strong>Непрерывное архивирование WAL (Write-Ahead Logging):</strong> Включен режим архивации WAL-файлов. Это позволяет восстановить базу данных на любой момент времени вплоть до последней зафиксированной транзакции (Point-in-Time Recovery, PITR). WAL-файлы архивируются в облачное хранилище (например, Yandex Object Storage).</li>
    <li><strong>Репликация:</strong> Настроена streaming-репликация на standby-сервер (горячий резерв). В случае падения основного сервера, реплика может быть быстро переведена в режим primary.</li>
    <li><strong>Проверка восстановления:</strong> Раз в месяц проводится процедура тестового восстановления из резервной копии на тестовом стенде для проверки ее целостности и отработки действий администратора.</li>
</ol>

<pre><code class="language-bash">#!/bin/bash
# Пример скрипта для ежедневного бэкапа (backup.sh)
BACKUP_DIR="/var/backups/postgresql"
DATE=$(date +%Y%m%d_%H%M%S)
DB_NAME="sport_school"

# Полное резервное копирование в custom формате
pg_dump -h localhost -U postgres -F c -b -v -f "$BACKUP_DIR/full_$DATE.backup" $DB_NAME

# Архивируем WAL файлы (требует настройки archive_command в postgresql.conf)
# Удаляем старые резервные копии (храним 7 дней)
find $BACKUP_DIR -name "*.backup" -mtime +7 -delete

# Проверка целостности бэкапа (список содержимого)
pg_restore -l "$BACKUP_DIR/full_$DATE.backup" > /dev/null && echo "Backup $DATE OK" || echo "Backup $DATE FAILED"</code></pre>

<div class="page-break"></div>

<h2 id="5-реализация-проекта-в-среде-конкретной-субд">5. Реализация проекта в среде PostgreSQL</h2>

<h3 id="51-создание-таблиц">5.1. Создание таблиц</h3>
<p>Приведен SQL код создания основных таблиц базы данных. Полный скрипт включает все таблицы, индексы, триггеры и заполнение тестовыми данными.</p>

<h4>5.1.1. Таблица - основа системы</h4>
<pre><code class="language-sql">-- Таблица Родитель
CREATE TABLE parent (
    parent_id SERIAL PRIMARY KEY,
    last_name VARCHAR(100) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    patronymic VARCHAR(100),
    phone VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(255),
    address TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- Таблица Воспитанник
CREATE TABLE athlete (
    athlete_id SERIAL PRIMARY KEY,
    last_name VARCHAR(100) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    patronymic VARCHAR(100),
    birth_date DATE NOT NULL,
    gender VARCHAR(1) CHECK (gender IN ('М', 'Ж')),
    medical_certificate_date DATE, -- Дата последней справки
    parent_id INTEGER NOT NULL REFERENCES parent(parent_id) ON DELETE CASCADE,
    notes TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- Таблица Группа (должна быть создана до group_enrollment)
CREATE TABLE training_group (
    group_id SERIAL PRIMARY KEY,
    group_name VARCHAR(100) NOT NULL,
    current_size INTEGER DEFAULT 0,
    -- ... другие поля
);

-- Таблица Зачисление в группу
CREATE TABLE group_enrollment (
    enrollment_id SERIAL PRIMARY KEY,
    athlete_id INTEGER NOT NULL REFERENCES athlete(athlete_id) ON DELETE CASCADE,
    group_id INTEGER NOT NULL REFERENCES training_group(group_id) ON DELETE CASCADE,
    enroll_date DATE NOT NULL DEFAULT CURRENT_DATE,
    unenroll_date DATE,
    CONSTRAINT unique_active_enrollment UNIQUE (athlete_id, group_id) WHERE (unenroll_date IS NULL)
);</code></pre>

<h3 id="52-создание-запросов">5.2. Создание запросов</h3>
<p>Разработаны основные SQL-запросы для выполнения бизнес-логики системы.</p>

<h4>5.2.1. Запрос на формирование расписания группы на неделю:</h4>
<pre><code class="language-sql">-- Получение расписания группы
SELECT g.group_name, s.lesson_date, s.start_time, s.end_time, s.location,
       t.last_name || ' ' || LEFT(t.first_name, 1) || '.' AS trainer_name
FROM schedule s
JOIN training_group g ON s.group_id = g.group_id
JOIN trainer tr ON g.trainer_id = tr.trainer_id
JOIN employee t ON tr.employee_id = t.employee_id
WHERE g.group_id = 5
  AND s.lesson_date BETWEEN '2025-04-01' AND '2025-04-07'
ORDER BY s.lesson_date, s.start_time;</code></pre>

<h4>5.2.2. Триггер для автоматического обновления размера группы при зачислении:</h4>
<pre><code class="language-sql">-- Триггерная функция
CREATE OR REPLACE FUNCTION update_group_size_on_enroll()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        UPDATE training_group
        SET current_size = current_size + 1
        WHERE group_id = NEW.group_id;
    ELSIF TG_OP = 'UPDATE' AND NEW.unenroll_date IS NOT NULL AND OLD.unenroll_date IS NULL THEN
        UPDATE training_group
        SET current_size = current_size - 1
        WHERE group_id = NEW.group_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Создание триггера
CREATE TRIGGER trg_group_size_change
AFTER INSERT OR UPDATE ON group_enrollment
FOR EACH ROW EXECUTE FUNCTION update_group_size_on_enroll();</code></pre>

<h4>5.2.3. Запрос для отчета о платежах за месяц:</h4>
<pre><code class="language-sql">-- Отчет по платежам
SELECT a.last_name || ' ' || a.first_name AS athlete_name,
       p.last_name || ' ' || p.first_name AS parent_name,
       pay.amount, pay.payment_date, pay.period_month, pay.period_year,
       t.name AS tariff_name
FROM payment pay
JOIN athlete a ON pay.athlete_id = a.athlete_id
JOIN parent p ON a.parent_id = p.parent_id
JOIN tariff t ON pay.tariff_id = t.tariff_id
WHERE pay.period_month = 4 AND pay.period_year = 2025
ORDER BY pay.payment_date DESC;</code></pre>

<h3 id="53-разработка-интерфейса">5.3. Разработка интерфейса</h3>
<p>Веб-интерфейс реализуется на PHP 8.x с использованием Bootstrap 5 для адаптивного дизайна. Архитектура: простой MVC-подход.</p>

<h4>5.3.1. Главная страница системы</h4>
<p>Панель управления (Dashboard) с виджетами: количество воспитанников, предстоящие соревнования, календарь занятий на сегодня.</p>
<ul>
    <li><strong>Разделы:</strong> Навигационное меню ведет к разделам: "Воспитанники", "Группы", "Расписание", "Соревнования", "Финансы".</li>
    <li><strong>CRUD-интерфейсы:</strong> Для каждой основной сущности реализованы формы и таблицы для просмотра, добавления, редактирования и удаления записей (с подтверждением).</li>
    <li><strong>Ролевой доступ:</strong> Интерфейс динамически меняется в зависимости от роли пользователя.</li>
</ul>

<h3 id="54-назначение-прав-доступа">5.4. Назначение прав доступа</h3>
<p>Права реализованы на двух уровнях: на уровне базы данных (роли PostgreSQL) и на уровне приложения (проверка роли в PHP-сессии).</p>

<h4>5.4.1. Создание ролей в PostgreSQL</h4>
<pre><code class="language-sql">-- Создание ролей (групп)
CREATE ROLE sport_admin WITH LOGIN PASSWORD 'admin_pass';
CREATE ROLE sport_trainer WITH LOGIN PASSWORD 'trainer_pass';
CREATE ROLE sport_accountant WITH LOGIN PASSWORD 'accountant_pass';

-- Администратор: полные права
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO sport_admin;

-- Тренер: чтение/запись по своим группам, воспитанникам, расписанию
GRANT SELECT, INSERT, UPDATE ON attendance, schedule TO sport_trainer;
-- (Права на конкретные строки могут быть реализованы через RLS - Row Level Security)

-- Бухгалтер: доступ только к финансовым данным
GRANT SELECT, INSERT, UPDATE ON payment, tariff TO sport_accountant;
GRANT SELECT ON athlete, parent TO sport_accountant;</code></pre>

<h3 id="55-создание-индексов">5.5. Создание индексов</h3>
<p>Индексы созданы для ускорения наиболее частых и критичных по производительности запросов.</p>

<pre><code class="language-sql">-- Критически важные индексы для быстрой работы сайта и отчетов
-- Для ускорения поиска и связывания
CREATE INDEX idx_athlete_parent ON athlete(parent_id);
CREATE INDEX idx_group_sport ON training_group(sport_type_id);
CREATE INDEX idx_group_trainer ON training_group(trainer_id);
CREATE INDEX idx_schedule_group_date ON schedule(group_id, lesson_date);
CREATE INDEX idx_attendance_athlete_date ON attendance(athlete_id, schedule_id);
CREATE INDEX idx_payment_athlete_date ON payment(athlete_id, period_year, period_month);
CREATE INDEX idx_athlete_birth_date ON athlete(birth_date); -- Для фильтра по возрасту</code></pre>

<h3 id="56-разработка-стратегии-резервного-копирования-базы-данных">5.6. Разработка стратегии резервного копирования базы данных</h3>

<h4>5.6.1. Настройка архивации WAL в postgresql.conf</h4>
<pre><code class="language-ini"># В файле postgresql.conf
wal_level = replica                     # Минимум replica для архивации
archive_mode = on                       # Включить архивацию
archive_command = 'test ! -f /var/backups/postgresql/wal_archive/%f && cp %p /var/backups/postgresql/wal_archive/%f'
# Команда копирует WAL-файл в директорию архива. В продакшене нужно копировать в облако.</code></pre>

<h4>5.6.2. Скрипт для полного бэкапа (backup_full.sh)</h4>
<pre><code class="language-bash">#!/bin/bash
# /usr/local/bin/backup_full.sh
BACKUP_ROOT="/var/backups/postgresql"
DATE=$(date +%Y%m%d_%H%M%S)
DB_NAME="sport_school"
BACKUP_FILE="$BACKUP_ROOT/full_$DATE.sql.gz"

Экспорт с использованием pg_dump, сжатие gzip на лет
pg_dump -h localhost -U postgres -d $DB_NAME \
  --format=plain \
  --no-owner \
  --no-privileges \
  --verbose 2>&1 | gzip > $BACKUP_FILE

 Проверка успешности создания
if [ $? -eq 0 ]; then
  echo "[$DATE] Full backup successful: $BACKUP_FILE" >> $BACKUP_ROOT/backup.log
  Отправка в облако (пример для Yandex Cloud)
  yc storage cp $BACKUP_FILE s3://my-backup-bucket/postgres/full/
else
  echo "[$DATE] ERROR: Full backup failed!" >> $BACKUP_ROOT/backup.log
   Отправка уведомления администратору
  echo "Backup failed for $DB_NAME on $(hostname)" | mail -s "BACKUP FAILURE" admin@mail.ru
fi

 Удвление старых локальных бэкапов (храним 7 дней)
find $BACKUP_ROOT -name "full_*.sql.gz" -mtime +7 -delete</code></pre>

<h4>5.6.3. Задание в crontab для автоматического выполнения</h4>
<pre><code class="language-crontab"># Ежедневно в 2:30 ночи
30 2 * * * /usr/local/bin/backup_full.sh

 Каждый час - синхронизация WAL-архивов с облаком (упрощенный пример)
0 * * * * rsync -avz /var/backups/postgresql/wal_archive/ user@backup-server:/backups/wal/

 Еженедельно в воскресенье - проверка целостности последнего бэкапа
0 5 * * 0 /usr/local/bin/verify_backup.sh</code></pre>

<h3 id="57-разработка-стратегии-защиты-базы-данных-и-хранимой-в-ней-информации">5.7. Разработка стратегии защиты базы данных и хранимой в ней информации</h3>
<p>Помимо ролевой модели и шифрования паролей, реализованы дополнительные меры защиты.</p>
<ul>
    <li><strong>Шифрование паролей:</strong> Хранение только хэшей (bcrypt) в таблице users.</li>
    <li><strong>Подготовленные выражения (Prepared Statements):</strong> В PHP-коде для защиты от SQL-инъекций.</li>
    <li><strong>HTTPS:</strong> Обязательное использование для веб-интерфейса.</li>
    <li><strong>Ограничение подключений по IP:</strong> Настройка в pg_hba.conf.</li>
</ul>

<h3 id="58-разработка-api-для-мобильного-приложения-родителей">5.8. Разработка API для мобильного приложения родителей</h3>

<h4>5.8.1. Базовая структура API (api/index.php)</h4>
<pre><code class="language-php">&lt;?php
// api/index.php
header('Content-Type: application/json');
require_once '../config.php';
require_once '../auth.php';

// Простая маршрутизация
$method = $_SERVER['REQUEST_METHOD'];
$request = explode('/', trim($_SERVER['PATH_INFO'], '/')); // Предполагается настройка mod_rewrite
$endpoint = $request[0] ?? '';

// Аутентификация по API-ключу или JWT-токену (упрощенно)
$apiKey = $_SERVER['HTTP_X_API_KEY'] ?? '';
if (!validateApiKey($pdo, $apiKey)) {
    http_response_code(401);
    echo json_encode(['error' => 'Invalid API key']);
    exit;
}

switch ("$method $endpoint") {
    case 'GET properties':
        echo json_encode(getProperties($pdo, $_GET));
        break;
    case 'POST bookings':
        $data = json_decode(file_get_contents('php://input'), true);
        echo json_encode(createBooking($pdo, $data));
        break;
    case 'GET bookings':
        echo json_encode(getUserBookings($pdo, $userId)); // $userId из токена
        break;
    default:
        http_response_code(404);
        echo json_encode(['error' => 'Endpoint not found']);
}
?&gt;</code></pre>

<p>Простой REST API на PHP, возвращающий данные в формате JSON.</p>
<ul>
    <li><strong>Endpoint GET /api/athlete/{id}/schedule:</strong> Возвращает расписание занятий ребенка.</li>
    <li><strong>Endpoint GET /api/athlete/{id}/payments:</strong> Возвращает историю платежей.</li>
    <li><strong>Endpoint GET /api/competitions/upcoming:</strong> Список ближайших соревнований.</li>
    <li><strong>Аутентификация:</strong> По токену (JWT), выданному при входе в личный кабинет.</li>
</ul>

<div class="page-break"></div>

<h2 id="заключение">Заключение</h2>

<p>В ходе выполнения курсовой работы была успешно спроектирована и реализована база данных для спортивной школы. Были достигнуты все поставленные цели:</p>

<ol>
    <li><strong>Проведен детальный анализ предметной области, выявлены ключевые сущности и процессы.</strong> Анализ позволил четко определить границы системы, выделить ключевые бизнес-процессы.</li>
    <li><strong>Проектирование базы данных.</strong> Построены инфологическая, логическая и физическая модели БД.</li>
    <li><strong>База данных реализована в СУБД PostgreSQL:</strong> созданы таблицы, индексы, триггеры для автоматизации бизнес-логики (контроль размера групп, посещаемости).</li>
    <li><strong>Веб-интерфейс на PHP и Bootstrap:</strong> Разработан прототип веб-интерфейса, обеспечивающий удобную работу с данными для различных категорий пользователей.</li>
    <li><strong>Система безопасности:</strong> Реализована система безопасности, включая разграничение прав доступа и стратегию резервного копирования.</li>
    <li><strong>REST API:</strong> Обеспечивает возможность интеграции системы с мобильными приложениями, партнерскими сайтами и другими внешними сервисами, открывая пути для масштабирования бизнеса.</li>
</ol>

<p>Разработанная система способна значительно повысить эффективность управления спортивной школой за счет автоматизации рутинных задач, обеспечения целостности данных и оперативного доступа к информации. В перспективе систему можно расширить, добавив модуль онлайн-записи на занятия, интеграцию с электронным дневником (для школ), или модуль анализа видео тренировок.</p>

<div class="page-break"></div>

<h2 id="список-использованных-информационных-источников">Список использованных информационных источников</h2>

<ol>
    <li>Официальная документация PostgreSQL 15. [Электронный ресурс]. URL: <a href="https://www.postgresql.org/docs/15/">https://www.postgresql.org/docs/15/</a></li>
    <li>PHP: The Right Way. Современные лучшие практики PHP. [Электронный ресурс]. URL: <a href="https://phptherightway.com/">https://phptherightway.com/</a></li>
    <li>Документация Bootstrap 5. [Электронный ресурс]. URL: <a href="https://getbootstrap.com/docs/5.3/">https://getbootstrap.com/docs/5.3/</a></li>
    <li>Коннолли Т., Бегг К. Базы данных: проектирование, реализация и сопровождение. Теория и практика. – 4-е изд. – М.: Вильямс, 2020. – 1440 с.</li>
    <li>Гарсиа-Молина Г., Ульман Д., Уидом Дж. Системы баз данных. Полный курс. – М.: Вильямс, 2019. – 1088 с.</li>
    <li>Роберт В. Себеста. Основные концепции языков программирования. – 10-е изд. – М.: Вильямс, 2018. – 768 с.</li>
    <li>Вонг Б. MySQL. Оптимизация производительности. – СПб.: Символ-Плюс, 2021. – 832 с. (Принципы применимы и к PostgreSQL).</li>
    <li>Советы по производительности PostgreSQL от команды разработки. [Электронный ресурс]. URL: <a href="https://www.postgresql.org/docs/current/performance-tips.html">https://www.postgresql.org/docs/current/performance-tips.html</a></li>
    <li>OWASP Top Ten. Рекомендации по безопасности веб-приложений. [Электронный ресурс]. URL: <a href="https://owasp.org/www-project-top-ten/">https://owasp.org/www-project-top-ten/</a></li>
    <li>Статьи и руководства на DigitalOcean, Habr, Stack Overflow по темам: «PostgreSQL триггеры», «Ролевая модель доступа», «Резервное копирование БД», «REST API design».</li>
    <li>ГОСТ Р ИСО/МЭК 12207-99. Информационная технология. Процессы жизненного цикла программных средств.</li>
    <li>ГОСТ 19.ххх-79. Единая система программной документации (ЕСПД). Серия стандартов на разработку документации (оператора, программиста, тех. проекта).</li>
</ol>

---

<h2 id="приложения">Приложения</h2>

<h3>Приложение А: Руководство пользователя (скриншоты интерфейса, инструкции по работе).</h3>

<h3>Приложение Б: Полный SQL-скрипт создания базы данных (schema.sql).</h3>

<h3>Приложение В: Исходный код веб-интерфейса (архив с файлами .php, .css).</h3>

<h3>Приложение Г: ER-диаграмма (графический файл, созданный в pgAdmin, DBDesigner или draw.io).</h3>
    
<h3>Приложение D: Код программных модулей</h3>

<p><em>Полный исходный код всех файлов проекта, представленный в техническом задании в начале этого документа, является неотъемлемой частью данной пояснительной записки. Код включает:</em></p>
<ul>
    <li><code>config.php</code> – конфигурация подключения к БД.</li>
    <li><code>auth.php</code>, <code>functions.php</code> – основные функции аутентификации и работы с БД.</li>
    <li><code>index.php</code>, <code>login.php</code>, <code>register.php</code>, <code>logout.php</code>, <code>stats.php</code> – основные PHP-скрипты веб-интерфейса.</li>
    <li><code>style.css</code> – каскадные таблицы стилей.</li>
    <li><code>test.php</code> – скрипт проверки работоспособности системы.</li>
    <li><strong>Полный SQL-скрипт</strong> создания и наполнения базы данных (все CREATE TABLE, INSERT, CREATE INDEX, CREATE TRIGGER).</li>
</ul>
<p><em>Исходный код размещен в Git-репозитории, доступном для проверки.</em></p>
