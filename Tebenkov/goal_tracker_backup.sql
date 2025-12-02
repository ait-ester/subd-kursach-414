--
-- PostgreSQL database dump
--

\restrict 4VKXHjy23coqy9UzAweyg0N9bOD1rC2gvvkTFQojQmZEQRRRJrc4s1IjO1Vfqdu

-- Dumped from database version 14.19 (Ubuntu 14.19-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.19 (Ubuntu 14.19-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: update_updated_at_column(); Type: FUNCTION; Schema: public; Owner: tracker_user
--

CREATE FUNCTION public.update_updated_at_column() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$;


ALTER FUNCTION public.update_updated_at_column() OWNER TO tracker_user;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: categories; Type: TABLE; Schema: public; Owner: tracker_user
--

CREATE TABLE public.categories (
    id integer NOT NULL,
    user_id integer NOT NULL,
    name character varying(50) NOT NULL,
    type character varying(20) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT categories_type_check CHECK (((type)::text = ANY ((ARRAY['goal'::character varying, 'habit'::character varying])::text[])))
);


ALTER TABLE public.categories OWNER TO tracker_user;

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: tracker_user
--

CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_id_seq OWNER TO tracker_user;

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tracker_user
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- Name: goal_progress; Type: TABLE; Schema: public; Owner: tracker_user
--

CREATE TABLE public.goal_progress (
    id integer NOT NULL,
    goal_id integer NOT NULL,
    date date NOT NULL,
    value numeric(10,2) NOT NULL,
    notes text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.goal_progress OWNER TO tracker_user;

--
-- Name: goal_progress_id_seq; Type: SEQUENCE; Schema: public; Owner: tracker_user
--

CREATE SEQUENCE public.goal_progress_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.goal_progress_id_seq OWNER TO tracker_user;

--
-- Name: goal_progress_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tracker_user
--

ALTER SEQUENCE public.goal_progress_id_seq OWNED BY public.goal_progress.id;


--
-- Name: goals; Type: TABLE; Schema: public; Owner: tracker_user
--

CREATE TABLE public.goals (
    id integer NOT NULL,
    user_id integer NOT NULL,
    title character varying(200) NOT NULL,
    description text,
    category character varying(50),
    goal_type character varying(20),
    target_value numeric(10,2),
    current_value numeric(10,2) DEFAULT 0,
    unit character varying(20),
    start_date date NOT NULL,
    end_date date,
    status character varying(20) DEFAULT 'active'::character varying,
    priority integer,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT goals_goal_type_check CHECK (((goal_type)::text = ANY ((ARRAY['boolean'::character varying, 'numeric'::character varying, 'habit'::character varying])::text[]))),
    CONSTRAINT goals_priority_check CHECK (((priority >= 1) AND (priority <= 5))),
    CONSTRAINT goals_status_check CHECK (((status)::text = ANY ((ARRAY['active'::character varying, 'completed'::character varying, 'failed'::character varying, 'paused'::character varying])::text[])))
);


ALTER TABLE public.goals OWNER TO tracker_user;

--
-- Name: goals_id_seq; Type: SEQUENCE; Schema: public; Owner: tracker_user
--

CREATE SEQUENCE public.goals_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.goals_id_seq OWNER TO tracker_user;

--
-- Name: goals_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tracker_user
--

ALTER SEQUENCE public.goals_id_seq OWNED BY public.goals.id;


--
-- Name: habit_tracking; Type: TABLE; Schema: public; Owner: tracker_user
--

CREATE TABLE public.habit_tracking (
    id integer NOT NULL,
    habit_id integer NOT NULL,
    date date NOT NULL,
    completed_count integer DEFAULT 0,
    target_count integer NOT NULL,
    notes text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.habit_tracking OWNER TO tracker_user;

--
-- Name: habit_tracking_id_seq; Type: SEQUENCE; Schema: public; Owner: tracker_user
--

CREATE SEQUENCE public.habit_tracking_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.habit_tracking_id_seq OWNER TO tracker_user;

--
-- Name: habit_tracking_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tracker_user
--

ALTER SEQUENCE public.habit_tracking_id_seq OWNED BY public.habit_tracking.id;


--
-- Name: habits; Type: TABLE; Schema: public; Owner: tracker_user
--

CREATE TABLE public.habits (
    id integer NOT NULL,
    user_id integer NOT NULL,
    name character varying(100) NOT NULL,
    description text,
    category character varying(50),
    frequency character varying(20),
    target_count integer DEFAULT 1,
    start_date date NOT NULL,
    end_date date,
    is_active boolean DEFAULT true,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT habits_frequency_check CHECK (((frequency)::text = ANY ((ARRAY['daily'::character varying, 'weekly'::character varying, 'monthly'::character varying])::text[])))
);


ALTER TABLE public.habits OWNER TO tracker_user;

--
-- Name: habits_id_seq; Type: SEQUENCE; Schema: public; Owner: tracker_user
--

CREATE SEQUENCE public.habits_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.habits_id_seq OWNER TO tracker_user;

--
-- Name: habits_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tracker_user
--

ALTER SEQUENCE public.habits_id_seq OWNED BY public.habits.id;


--
-- Name: reminders; Type: TABLE; Schema: public; Owner: tracker_user
--

CREATE TABLE public.reminders (
    id integer NOT NULL,
    user_id integer NOT NULL,
    habit_id integer NOT NULL,
    reminder_time time without time zone NOT NULL,
    days_of_week character varying(13),
    is_active boolean DEFAULT true,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.reminders OWNER TO tracker_user;

--
-- Name: reminders_id_seq; Type: SEQUENCE; Schema: public; Owner: tracker_user
--

CREATE SEQUENCE public.reminders_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reminders_id_seq OWNER TO tracker_user;

--
-- Name: reminders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tracker_user
--

ALTER SEQUENCE public.reminders_id_seq OWNED BY public.reminders.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: tracker_user
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(50) NOT NULL,
    email character varying(100) NOT NULL,
    password_hash character varying(255) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    is_active boolean DEFAULT true
);


ALTER TABLE public.users OWNER TO tracker_user;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: tracker_user
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO tracker_user;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tracker_user
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: weight_tracking; Type: TABLE; Schema: public; Owner: tracker_user
--

CREATE TABLE public.weight_tracking (
    id integer NOT NULL,
    user_id integer NOT NULL,
    date date NOT NULL,
    weight numeric(5,2) NOT NULL,
    body_fat_percent numeric(4,2),
    muscle_mass numeric(5,2),
    waist_circumference numeric(4,1),
    hip_circumference numeric(4,1),
    notes text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT weight_tracking_body_fat_percent_check CHECK (((body_fat_percent >= (0)::numeric) AND (body_fat_percent <= (100)::numeric))),
    CONSTRAINT weight_tracking_weight_check CHECK ((weight > (0)::numeric))
);


ALTER TABLE public.weight_tracking OWNER TO tracker_user;

--
-- Name: weight_tracking_id_seq; Type: SEQUENCE; Schema: public; Owner: tracker_user
--

CREATE SEQUENCE public.weight_tracking_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.weight_tracking_id_seq OWNER TO tracker_user;

--
-- Name: weight_tracking_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tracker_user
--

ALTER SEQUENCE public.weight_tracking_id_seq OWNED BY public.weight_tracking.id;


--
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- Name: goal_progress id; Type: DEFAULT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.goal_progress ALTER COLUMN id SET DEFAULT nextval('public.goal_progress_id_seq'::regclass);


--
-- Name: goals id; Type: DEFAULT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.goals ALTER COLUMN id SET DEFAULT nextval('public.goals_id_seq'::regclass);


--
-- Name: habit_tracking id; Type: DEFAULT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.habit_tracking ALTER COLUMN id SET DEFAULT nextval('public.habit_tracking_id_seq'::regclass);


--
-- Name: habits id; Type: DEFAULT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.habits ALTER COLUMN id SET DEFAULT nextval('public.habits_id_seq'::regclass);


--
-- Name: reminders id; Type: DEFAULT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.reminders ALTER COLUMN id SET DEFAULT nextval('public.reminders_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: weight_tracking id; Type: DEFAULT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.weight_tracking ALTER COLUMN id SET DEFAULT nextval('public.weight_tracking_id_seq'::regclass);


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: tracker_user
--

COPY public.categories (id, user_id, name, type, created_at) FROM stdin;
1	1	Здоровье	goal	2025-12-02 13:26:51.05242
2	1	Спорт	goal	2025-12-02 13:26:51.05242
3	1	Утренние	habit	2025-12-02 13:26:51.05242
4	1	Ежедневные	habit	2025-12-02 13:26:51.05242
5	2	Карьера	goal	2025-12-02 13:26:51.056176
6	2	Личное развитие	habit	2025-12-02 13:26:51.056176
\.


--
-- Data for Name: goal_progress; Type: TABLE DATA; Schema: public; Owner: tracker_user
--

COPY public.goal_progress (id, goal_id, date, value, notes, created_at) FROM stdin;
1	1	2024-01-05	80.00	Начальный вес	2025-12-02 13:26:51.060853
2	1	2024-01-20	79.00	После диеты	2025-12-02 13:26:51.060853
3	1	2024-02-01	78.50	Текущий вес	2025-12-02 13:26:51.060853
4	4	2024-01-15	1.00	Первая книга	2025-12-02 13:26:51.062069
5	4	2024-01-31	2.00	Вторая книга	2025-12-02 13:26:51.062069
6	4	2024-02-15	3.00	Третья книга	2025-12-02 13:26:51.062069
\.


--
-- Data for Name: goals; Type: TABLE DATA; Schema: public; Owner: tracker_user
--

COPY public.goals (id, user_id, title, description, category, goal_type, target_value, current_value, unit, start_date, end_date, status, priority, created_at, updated_at) FROM stdin;
2	1	Похудеть до 70кг	\N	\N	\N	\N	0.00	\N	2024-01-01	\N	active	\N	2025-12-02 13:18:26.887861	2025-12-02 13:18:26.887861
1	1	Похудеть до 75кг	\N	\N	numeric	75.00	72.50	кг	2025-12-02	\N	active	2	2025-12-02 13:16:27.887383	2025-12-02 13:19:16.535455
3	1	Похудеть до 75кг	Сбросить 5 кг	Здоровье	numeric	75.00	78.50	кг	2024-01-01	2024-06-01	active	1	2025-12-02 13:26:51.058163	2025-12-02 13:26:51.058163
4	1	Бегать 3 раза в неделю	Подготовка к забегу	Спорт	habit	3.00	2.00	раз/неделю	2024-01-10	2024-12-31	active	2	2025-12-02 13:26:51.058163	2025-12-02 13:26:51.058163
5	2	Изучить английский	Дойти до уровня B2	Карьера	boolean	1.00	0.50	уровень	2024-01-01	2024-12-31	active	1	2025-12-02 13:26:51.059846	2025-12-02 13:26:51.059846
6	2	Прочитать 10 книг	Для саморазвития	Карьера	numeric	10.00	3.00	книг	2024-01-01	2024-12-31	active	2	2025-12-02 13:26:51.059846	2025-12-02 13:26:51.059846
\.


--
-- Data for Name: habit_tracking; Type: TABLE DATA; Schema: public; Owner: tracker_user
--

COPY public.habit_tracking (id, habit_id, date, completed_count, target_count, notes, created_at) FROM stdin;
1	1	2024-02-01	1	1	\N	2025-12-02 13:26:51.067297
2	1	2024-02-02	1	1	\N	2025-12-02 13:26:51.067297
3	1	2024-02-03	0	1	Проспал	2025-12-02 13:26:51.067297
4	1	2024-02-04	1	1	\N	2025-12-02 13:26:51.067297
5	2	2024-02-01	1	1	\N	2025-12-02 13:26:51.070434
6	2	2024-02-02	1	1	\N	2025-12-02 13:26:51.070434
7	2	2024-02-03	1	1	\N	2025-12-02 13:26:51.070434
8	2	2024-02-04	0	1	Забыл	2025-12-02 13:26:51.070434
9	3	2024-02-01	1	1	\N	2025-12-02 13:26:51.072392
10	3	2024-02-02	1	1	\N	2025-12-02 13:26:51.072392
11	3	2024-02-03	0	1	Лег поздно	2025-12-02 13:26:51.072392
12	3	2024-02-04	1	1	\N	2025-12-02 13:26:51.072392
\.


--
-- Data for Name: habits; Type: TABLE DATA; Schema: public; Owner: tracker_user
--

COPY public.habits (id, user_id, name, description, category, frequency, target_count, start_date, end_date, is_active, created_at) FROM stdin;
1	1	Утренняя зарядка	\N	\N	daily	1	2025-12-02	\N	t	2025-12-02 13:16:27.887383
2	1	Утренняя зарядка	15 минут упражнений	Утренние	daily	1	2024-01-01	\N	t	2025-12-02 13:26:51.063106
3	1	Пить воду	2 литра в день	Ежедневные	daily	1	2024-01-15	\N	t	2025-12-02 13:26:51.063106
4	2	Ранний подъем	Вставать в 6 утра	Личное развитие	daily	1	2024-01-01	\N	t	2025-12-02 13:26:51.065329
\.


--
-- Data for Name: reminders; Type: TABLE DATA; Schema: public; Owner: tracker_user
--

COPY public.reminders (id, user_id, habit_id, reminder_time, days_of_week, is_active, created_at) FROM stdin;
1	1	1	07:30:00	1,2,3,4,5	t	2025-12-02 13:26:51.07816
2	1	2	12:00:00	\N	t	2025-12-02 13:26:51.07816
3	2	3	06:00:00	\N	t	2025-12-02 13:26:51.07816
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: tracker_user
--

COPY public.users (id, username, email, password_hash, created_at, is_active) FROM stdin;
1	demo_user	demo@example.com	hashed_password_123	2025-12-02 13:16:27.881094	t
2	test_user	test@example.com	hashed_password_456	2025-12-02 13:16:27.881094	t
\.


--
-- Data for Name: weight_tracking; Type: TABLE DATA; Schema: public; Owner: tracker_user
--

COPY public.weight_tracking (id, user_id, date, weight, body_fat_percent, muscle_mass, waist_circumference, hip_circumference, notes, created_at) FROM stdin;
1	1	2025-11-25	78.50	\N	\N	\N	\N	Неделю назад	2025-12-02 13:16:27.887383
2	1	2025-11-29	77.80	\N	\N	\N	\N	Три дня назад	2025-12-02 13:16:27.887383
3	1	2025-12-02	77.20	\N	\N	\N	\N	Сегодня	2025-12-02 13:16:27.887383
4	1	2024-01-01	80.50	25.00	\N	\N	\N	Начало	2025-12-02 13:26:51.074116
5	1	2024-01-15	79.50	24.50	\N	\N	\N	Через 2 недели	2025-12-02 13:26:51.074116
6	1	2024-02-01	78.50	24.00	\N	\N	\N	Месяц спустя	2025-12-02 13:26:51.074116
7	2	2024-01-01	70.00	\N	\N	\N	\N	Начальный вес	2025-12-02 13:26:51.076324
8	2	2024-02-01	69.50	\N	\N	\N	\N	Похудел немного	2025-12-02 13:26:51.076324
\.


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tracker_user
--

SELECT pg_catalog.setval('public.categories_id_seq', 6, true);


--
-- Name: goal_progress_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tracker_user
--

SELECT pg_catalog.setval('public.goal_progress_id_seq', 6, true);


--
-- Name: goals_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tracker_user
--

SELECT pg_catalog.setval('public.goals_id_seq', 6, true);


--
-- Name: habit_tracking_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tracker_user
--

SELECT pg_catalog.setval('public.habit_tracking_id_seq', 12, true);


--
-- Name: habits_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tracker_user
--

SELECT pg_catalog.setval('public.habits_id_seq', 4, true);


--
-- Name: reminders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tracker_user
--

SELECT pg_catalog.setval('public.reminders_id_seq', 3, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tracker_user
--

SELECT pg_catalog.setval('public.users_id_seq', 2, true);


--
-- Name: weight_tracking_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tracker_user
--

SELECT pg_catalog.setval('public.weight_tracking_id_seq', 8, true);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);


--
-- Name: categories categories_user_id_name_type_key; Type: CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_user_id_name_type_key UNIQUE (user_id, name, type);


--
-- Name: goal_progress goal_progress_goal_id_date_key; Type: CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.goal_progress
    ADD CONSTRAINT goal_progress_goal_id_date_key UNIQUE (goal_id, date);


--
-- Name: goal_progress goal_progress_pkey; Type: CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.goal_progress
    ADD CONSTRAINT goal_progress_pkey PRIMARY KEY (id);


--
-- Name: goals goals_pkey; Type: CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.goals
    ADD CONSTRAINT goals_pkey PRIMARY KEY (id);


--
-- Name: habit_tracking habit_tracking_habit_id_date_key; Type: CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.habit_tracking
    ADD CONSTRAINT habit_tracking_habit_id_date_key UNIQUE (habit_id, date);


--
-- Name: habit_tracking habit_tracking_pkey; Type: CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.habit_tracking
    ADD CONSTRAINT habit_tracking_pkey PRIMARY KEY (id);


--
-- Name: habits habits_pkey; Type: CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.habits
    ADD CONSTRAINT habits_pkey PRIMARY KEY (id);


--
-- Name: reminders reminders_pkey; Type: CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.reminders
    ADD CONSTRAINT reminders_pkey PRIMARY KEY (id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: weight_tracking weight_tracking_pkey; Type: CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.weight_tracking
    ADD CONSTRAINT weight_tracking_pkey PRIMARY KEY (id);


--
-- Name: weight_tracking weight_tracking_user_id_date_key; Type: CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.weight_tracking
    ADD CONSTRAINT weight_tracking_user_id_date_key UNIQUE (user_id, date);


--
-- Name: idx_goal_progress_date; Type: INDEX; Schema: public; Owner: tracker_user
--

CREATE INDEX idx_goal_progress_date ON public.goal_progress USING btree (date);


--
-- Name: idx_goal_progress_goal_date; Type: INDEX; Schema: public; Owner: tracker_user
--

CREATE INDEX idx_goal_progress_goal_date ON public.goal_progress USING btree (goal_id, date DESC);


--
-- Name: idx_goals_status; Type: INDEX; Schema: public; Owner: tracker_user
--

CREATE INDEX idx_goals_status ON public.goals USING btree (status);


--
-- Name: idx_goals_user_id; Type: INDEX; Schema: public; Owner: tracker_user
--

CREATE INDEX idx_goals_user_id ON public.goals USING btree (user_id);


--
-- Name: idx_habit_tracking_date; Type: INDEX; Schema: public; Owner: tracker_user
--

CREATE INDEX idx_habit_tracking_date ON public.habit_tracking USING btree (date);


--
-- Name: idx_habit_tracking_habit_date; Type: INDEX; Schema: public; Owner: tracker_user
--

CREATE INDEX idx_habit_tracking_habit_date ON public.habit_tracking USING btree (habit_id, date DESC);


--
-- Name: idx_habits_is_active; Type: INDEX; Schema: public; Owner: tracker_user
--

CREATE INDEX idx_habits_is_active ON public.habits USING btree (is_active);


--
-- Name: idx_habits_user_id; Type: INDEX; Schema: public; Owner: tracker_user
--

CREATE INDEX idx_habits_user_id ON public.habits USING btree (user_id);


--
-- Name: idx_reminders_habit_id; Type: INDEX; Schema: public; Owner: tracker_user
--

CREATE INDEX idx_reminders_habit_id ON public.reminders USING btree (habit_id);


--
-- Name: idx_reminders_user_id; Type: INDEX; Schema: public; Owner: tracker_user
--

CREATE INDEX idx_reminders_user_id ON public.reminders USING btree (user_id);


--
-- Name: idx_users_email; Type: INDEX; Schema: public; Owner: tracker_user
--

CREATE INDEX idx_users_email ON public.users USING btree (email);


--
-- Name: idx_users_username; Type: INDEX; Schema: public; Owner: tracker_user
--

CREATE INDEX idx_users_username ON public.users USING btree (username);


--
-- Name: idx_weight_tracking_date; Type: INDEX; Schema: public; Owner: tracker_user
--

CREATE INDEX idx_weight_tracking_date ON public.weight_tracking USING btree (date);


--
-- Name: idx_weight_user_date; Type: INDEX; Schema: public; Owner: tracker_user
--

CREATE INDEX idx_weight_user_date ON public.weight_tracking USING btree (user_id, date DESC);


--
-- Name: goals update_goals_updated_at; Type: TRIGGER; Schema: public; Owner: tracker_user
--

CREATE TRIGGER update_goals_updated_at BEFORE UPDATE ON public.goals FOR EACH ROW EXECUTE FUNCTION public.update_updated_at_column();


--
-- Name: categories categories_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: goal_progress goal_progress_goal_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.goal_progress
    ADD CONSTRAINT goal_progress_goal_id_fkey FOREIGN KEY (goal_id) REFERENCES public.goals(id) ON DELETE CASCADE;


--
-- Name: goals goals_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.goals
    ADD CONSTRAINT goals_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: habit_tracking habit_tracking_habit_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.habit_tracking
    ADD CONSTRAINT habit_tracking_habit_id_fkey FOREIGN KEY (habit_id) REFERENCES public.habits(id) ON DELETE CASCADE;


--
-- Name: habits habits_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.habits
    ADD CONSTRAINT habits_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: reminders reminders_habit_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.reminders
    ADD CONSTRAINT reminders_habit_id_fkey FOREIGN KEY (habit_id) REFERENCES public.habits(id) ON DELETE CASCADE;


--
-- Name: reminders reminders_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.reminders
    ADD CONSTRAINT reminders_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: weight_tracking weight_tracking_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tracker_user
--

ALTER TABLE ONLY public.weight_tracking
    ADD CONSTRAINT weight_tracking_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

\unrestrict 4VKXHjy23coqy9UzAweyg0N9bOD1rC2gvvkTFQojQmZEQRRRJrc4s1IjO1Vfqdu

