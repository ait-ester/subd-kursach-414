--
-- PostgreSQL database dump
--

\restrict 4XTjCDpGhcHVs6xmtF09tI19eath8gLChvZIbTaiVwvRGHfQnqlvWzBDMFxDiCH

-- Dumped from database version 18.1
-- Dumped by pg_dump version 18.1

-- Started on 2025-12-18 06:12:59

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 246 (class 1255 OID 16848)
-- Name: api_add_operation(integer, integer, integer, integer, date, numeric, character varying, character varying); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.api_add_operation(IN p_user_id integer, IN p_account_id integer, IN p_category_id integer, IN p_payee_id integer, IN p_op_date date, IN p_amount numeric, IN p_operation_type character varying, IN p_description character varying)
    LANGUAGE plpgsql
    AS $$
BEGIN
    INSERT INTO operations (
        user_id,
        account_id,
        category_id,
        payee_id,
        operation_date,
        amount,
        operation_type,
        description
    )
    VALUES (
        p_user_id,
        p_account_id,
        p_category_id,
        p_payee_id,
        p_op_date,
        p_amount,
        p_operation_type,
        p_description
    );
END;
$$;


ALTER PROCEDURE public.api_add_operation(IN p_user_id integer, IN p_account_id integer, IN p_category_id integer, IN p_payee_id integer, IN p_op_date date, IN p_amount numeric, IN p_operation_type character varying, IN p_description character varying) OWNER TO postgres;

--
-- TOC entry 233 (class 1255 OID 16798)
-- Name: api_get_operations(integer); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.api_get_operations(p_user_id integer) RETURNS TABLE(operation_date date, account_name text, category_name text, operation_type text, amount numeric, description text)
    LANGUAGE sql
    AS $$
    SELECT
        o.operation_date,
        a.account_name,
        c.category_name,
        o.operation_type,
        o.amount,
        o.description
    FROM operations o
    JOIN accounts a ON o.account_id = a.account_id
    JOIN categories c ON o.category_id = c.category_id
    WHERE o.user_id = p_user_id
    ORDER BY o.operation_date;
$$;


ALTER FUNCTION public.api_get_operations(p_user_id integer) OWNER TO postgres;

--
-- TOC entry 234 (class 1255 OID 16799)
-- Name: check_account_owner(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.check_account_owner() RETURNS trigger
    LANGUAGE plpgsql SECURITY DEFINER
    AS $$
DECLARE
    acc_user_id INTEGER;
BEGIN
    SELECT user_id
    INTO acc_user_id
    FROM accounts
    WHERE account_id = NEW.account_id;

    IF acc_user_id IS NULL THEN
        RAISE EXCEPTION 'Счёт не существует';
    END IF;

    IF acc_user_id <> NEW.user_id THEN
        RAISE EXCEPTION 'Пользователь не является владельцем счёта';
    END IF;

    RETURN NEW;
END;
$$;


ALTER FUNCTION public.check_account_owner() OWNER TO postgres;

--
-- TOC entry 232 (class 1255 OID 16750)
-- Name: check_category_type(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.check_category_type() RETURNS trigger
    LANGUAGE plpgsql SECURITY DEFINER
    AS $$
BEGIN
    IF (SELECT operation_type FROM categories WHERE category_id = NEW.category_id)
       <> NEW.operation_type THEN
        RAISE EXCEPTION 'Тип операции не соответствует типу категории';
    END IF;
    RETURN NEW;
END;
$$;


ALTER FUNCTION public.check_category_type() OWNER TO postgres;

--
-- TOC entry 231 (class 1255 OID 16752)
-- Name: update_account_balance(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.update_account_balance() RETURNS trigger
    LANGUAGE plpgsql SECURITY DEFINER
    AS $$
BEGIN
    IF NEW.operation_type = 'income' THEN
        UPDATE accounts
        SET balance = balance + NEW.amount
        WHERE account_id = NEW.account_id;
    ELSE
        UPDATE accounts
        SET balance = balance - NEW.amount
        WHERE account_id = NEW.account_id;
    END IF;
    RETURN NEW;
END;
$$;


ALTER FUNCTION public.update_account_balance() OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 222 (class 1259 OID 16685)
-- Name: accounts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.accounts (
    account_id integer NOT NULL,
    user_id integer NOT NULL,
    account_name text NOT NULL,
    balance numeric(12,2) DEFAULT 0 NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    account_type text DEFAULT 'cash'::text NOT NULL
);


ALTER TABLE public.accounts OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16684)
-- Name: accounts_account_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.accounts_account_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.accounts_account_id_seq OWNER TO postgres;

--
-- TOC entry 4990 (class 0 OID 0)
-- Dependencies: 221
-- Name: accounts_account_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.accounts_account_id_seq OWNED BY public.accounts.account_id;


--
-- TOC entry 224 (class 1259 OID 16705)
-- Name: categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categories (
    category_id integer NOT NULL,
    category_name text NOT NULL,
    operation_type text NOT NULL,
    CONSTRAINT categories_operation_type_check CHECK ((operation_type = ANY (ARRAY['income'::text, 'expense'::text])))
);


ALTER TABLE public.categories OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16704)
-- Name: categories_category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.categories_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.categories_category_id_seq OWNER TO postgres;

--
-- TOC entry 4993 (class 0 OID 0)
-- Dependencies: 223
-- Name: categories_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.categories_category_id_seq OWNED BY public.categories.category_id;


--
-- TOC entry 226 (class 1259 OID 16718)
-- Name: operations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.operations (
    operation_id integer NOT NULL,
    user_id integer NOT NULL,
    account_id integer NOT NULL,
    category_id integer NOT NULL,
    operation_date date NOT NULL,
    amount numeric(12,2) NOT NULL,
    operation_type text NOT NULL,
    description text,
    payee_id integer,
    CONSTRAINT chk_payee_for_expense CHECK ((((operation_type = 'expense'::text) AND (payee_id IS NOT NULL)) OR (operation_type = 'income'::text))),
    CONSTRAINT operations_amount_check CHECK ((amount > (0)::numeric)),
    CONSTRAINT operations_operation_type_check CHECK ((operation_type = ANY (ARRAY['income'::text, 'expense'::text])))
);


ALTER TABLE public.operations OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16670)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    username text NOT NULL,
    password_hash text NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 16849)
-- Name: export_operations; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.export_operations AS
 SELECT o.user_id,
    u.username,
    a.account_name,
    a.account_type,
    o.operation_date,
    o.operation_type,
    c.category_name,
    o.amount,
    o.description
   FROM (((public.operations o
     JOIN public.users u ON ((o.user_id = u.user_id)))
     JOIN public.accounts a ON ((o.account_id = a.account_id)))
     JOIN public.categories c ON ((o.category_id = c.category_id)));


ALTER VIEW public.export_operations OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16717)
-- Name: operations_operation_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.operations_operation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.operations_operation_id_seq OWNER TO postgres;

--
-- TOC entry 4998 (class 0 OID 0)
-- Dependencies: 225
-- Name: operations_operation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.operations_operation_id_seq OWNED BY public.operations.operation_id;


--
-- TOC entry 227 (class 1259 OID 16757)
-- Name: operations_view; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.operations_view AS
 SELECT o.operation_id,
    o.operation_date,
    o.amount,
    o.operation_type,
    c.category_name,
    a.account_name
   FROM ((public.operations o
     JOIN public.categories c ON ((o.category_id = c.category_id)))
     JOIN public.accounts a ON ((o.account_id = a.account_id)));


ALTER VIEW public.operations_view OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 16764)
-- Name: payees; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.payees (
    payee_id integer NOT NULL,
    user_id integer NOT NULL,
    payee_name text NOT NULL
);


ALTER TABLE public.payees OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 16763)
-- Name: payees_payee_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.payees_payee_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.payees_payee_id_seq OWNER TO postgres;

--
-- TOC entry 5002 (class 0 OID 0)
-- Dependencies: 228
-- Name: payees_payee_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.payees_payee_id_seq OWNED BY public.payees.payee_id;


--
-- TOC entry 219 (class 1259 OID 16669)
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_user_id_seq OWNER TO postgres;

--
-- TOC entry 5004 (class 0 OID 0)
-- Dependencies: 219
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- TOC entry 4790 (class 2604 OID 16688)
-- Name: accounts account_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accounts ALTER COLUMN account_id SET DEFAULT nextval('public.accounts_account_id_seq'::regclass);


--
-- TOC entry 4794 (class 2604 OID 16708)
-- Name: categories category_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories ALTER COLUMN category_id SET DEFAULT nextval('public.categories_category_id_seq'::regclass);


--
-- TOC entry 4795 (class 2604 OID 16721)
-- Name: operations operation_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operations ALTER COLUMN operation_id SET DEFAULT nextval('public.operations_operation_id_seq'::regclass);


--
-- TOC entry 4796 (class 2604 OID 16767)
-- Name: payees payee_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payees ALTER COLUMN payee_id SET DEFAULT nextval('public.payees_payee_id_seq'::regclass);


--
-- TOC entry 4788 (class 2604 OID 16673)
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- TOC entry 4977 (class 0 OID 16685)
-- Dependencies: 222
-- Data for Name: accounts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.accounts (account_id, user_id, account_name, balance, created_at, account_type) FROM stdin;
3	2	Семейная карта	20000.00	2025-12-17 22:46:16.981823	card
1	1	Наличные отца	200000.00	2025-12-17 22:46:16.981823	cash
4	3	Карманные деньги	-48800.00	2025-12-17 22:46:16.981823	cash
2	1	Семейная карта	45000.00	2025-12-17 22:46:16.981823	card
\.


--
-- TOC entry 4979 (class 0 OID 16705)
-- Dependencies: 224
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categories (category_id, category_name, operation_type) FROM stdin;
1	Зарплата	income
2	Подарок	income
3	Продукты	expense
4	Развлечения	expense
\.


--
-- TOC entry 4981 (class 0 OID 16718)
-- Dependencies: 226
-- Data for Name: operations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.operations (operation_id, user_id, account_id, category_id, operation_date, amount, operation_type, description, payee_id) FROM stdin;
1	1	1	1	2025-11-01	100000.00	income	Зарплата за ноябрь	1
2	2	3	3	2025-11-02	5000.00	expense	Продукты	3
3	3	4	4	2025-11-03	800.00	expense	Кино	4
5	1	1	3	2025-12-17	10000.00	expense	Продукты	2
6	2	3	3	2025-12-17	5000.00	expense	Продукты	3
7	1	2	1	2025-12-17	5000.00	income	Zarplata	1
8	1	1	1	2025-12-17	50000.00	income		1
9	1	2	1	2025-12-17	5000.00	income	test4	5
13	1	1	1	2025-12-17	50000.00	income		1
15	3	4	4	2025-12-17	50000.00	expense	test	4
16	1	2	1	2025-12-17	5000.00	income	test2?	1
\.


--
-- TOC entry 4983 (class 0 OID 16764)
-- Dependencies: 229
-- Data for Name: payees; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.payees (payee_id, user_id, payee_name) FROM stdin;
1	1	Работодатель
2	1	Магазин
3	2	Магазин
4	3	Кинотеатр
5	1	Не указан
6	2	Не указан
7	3	Не указан
\.


--
-- TOC entry 4975 (class 0 OID 16670)
-- Dependencies: 220
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (user_id, username, password_hash, created_at) FROM stdin;
1	father	hash_father	2025-12-17 22:45:53.084711
2	mother	hash_mother	2025-12-17 22:45:53.084711
3	child	hash_child	2025-12-17 22:45:53.084711
\.


--
-- TOC entry 5006 (class 0 OID 0)
-- Dependencies: 221
-- Name: accounts_account_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.accounts_account_id_seq', 4, true);


--
-- TOC entry 5007 (class 0 OID 0)
-- Dependencies: 223
-- Name: categories_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categories_category_id_seq', 4, true);


--
-- TOC entry 5008 (class 0 OID 0)
-- Dependencies: 225
-- Name: operations_operation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.operations_operation_id_seq', 16, true);


--
-- TOC entry 5009 (class 0 OID 0)
-- Dependencies: 228
-- Name: payees_payee_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.payees_payee_id_seq', 7, true);


--
-- TOC entry 5010 (class 0 OID 0)
-- Dependencies: 219
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_user_id_seq', 3, true);


--
-- TOC entry 4806 (class 2606 OID 16698)
-- Name: accounts accounts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accounts
    ADD CONSTRAINT accounts_pkey PRIMARY KEY (account_id);


--
-- TOC entry 4808 (class 2606 OID 16716)
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (category_id);


--
-- TOC entry 4813 (class 2606 OID 16734)
-- Name: operations operations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operations
    ADD CONSTRAINT operations_pkey PRIMARY KEY (operation_id);


--
-- TOC entry 4815 (class 2606 OID 16774)
-- Name: payees payees_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payees
    ADD CONSTRAINT payees_pkey PRIMARY KEY (payee_id);


--
-- TOC entry 4802 (class 2606 OID 16681)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- TOC entry 4804 (class 2606 OID 16683)
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- TOC entry 4809 (class 1259 OID 16755)
-- Name: idx_operations_account_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_operations_account_id ON public.operations USING btree (account_id);


--
-- TOC entry 4810 (class 1259 OID 16756)
-- Name: idx_operations_date; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_operations_date ON public.operations USING btree (operation_date);


--
-- TOC entry 4811 (class 1259 OID 16754)
-- Name: idx_operations_user_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_operations_user_id ON public.operations USING btree (user_id);


--
-- TOC entry 4822 (class 2620 OID 16800)
-- Name: operations trg_check_account_owner; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER trg_check_account_owner BEFORE INSERT ON public.operations FOR EACH ROW EXECUTE FUNCTION public.check_account_owner();


--
-- TOC entry 4823 (class 2620 OID 16751)
-- Name: operations trg_check_category_type; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER trg_check_category_type BEFORE INSERT ON public.operations FOR EACH ROW EXECUTE FUNCTION public.check_category_type();


--
-- TOC entry 4824 (class 2620 OID 16753)
-- Name: operations trg_update_balance; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER trg_update_balance AFTER INSERT ON public.operations FOR EACH ROW EXECUTE FUNCTION public.update_account_balance();


--
-- TOC entry 4816 (class 2606 OID 16699)
-- Name: accounts accounts_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.accounts
    ADD CONSTRAINT accounts_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON DELETE CASCADE;


--
-- TOC entry 4817 (class 2606 OID 16740)
-- Name: operations operations_account_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operations
    ADD CONSTRAINT operations_account_id_fkey FOREIGN KEY (account_id) REFERENCES public.accounts(account_id);


--
-- TOC entry 4818 (class 2606 OID 16745)
-- Name: operations operations_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operations
    ADD CONSTRAINT operations_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.categories(category_id);


--
-- TOC entry 4819 (class 2606 OID 16780)
-- Name: operations operations_payee_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operations
    ADD CONSTRAINT operations_payee_id_fkey FOREIGN KEY (payee_id) REFERENCES public.payees(payee_id);


--
-- TOC entry 4820 (class 2606 OID 16735)
-- Name: operations operations_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.operations
    ADD CONSTRAINT operations_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- TOC entry 4821 (class 2606 OID 16775)
-- Name: payees payees_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payees
    ADD CONSTRAINT payees_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON DELETE CASCADE;


--
-- TOC entry 4989 (class 0 OID 0)
-- Dependencies: 222
-- Name: TABLE accounts; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT ON TABLE public.accounts TO finance_app;


--
-- TOC entry 4991 (class 0 OID 0)
-- Dependencies: 221
-- Name: SEQUENCE accounts_account_id_seq; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,USAGE ON SEQUENCE public.accounts_account_id_seq TO finance_app;


--
-- TOC entry 4992 (class 0 OID 0)
-- Dependencies: 224
-- Name: TABLE categories; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT ON TABLE public.categories TO finance_app;


--
-- TOC entry 4994 (class 0 OID 0)
-- Dependencies: 223
-- Name: SEQUENCE categories_category_id_seq; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,USAGE ON SEQUENCE public.categories_category_id_seq TO finance_app;


--
-- TOC entry 4995 (class 0 OID 0)
-- Dependencies: 226
-- Name: TABLE operations; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT ON TABLE public.operations TO finance_app;


--
-- TOC entry 4996 (class 0 OID 0)
-- Dependencies: 220
-- Name: TABLE users; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT ON TABLE public.users TO finance_app;


--
-- TOC entry 4997 (class 0 OID 0)
-- Dependencies: 230
-- Name: TABLE export_operations; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT ON TABLE public.export_operations TO PUBLIC;


--
-- TOC entry 4999 (class 0 OID 0)
-- Dependencies: 225
-- Name: SEQUENCE operations_operation_id_seq; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,USAGE ON SEQUENCE public.operations_operation_id_seq TO finance_app;


--
-- TOC entry 5000 (class 0 OID 0)
-- Dependencies: 227
-- Name: TABLE operations_view; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT ON TABLE public.operations_view TO finance_read;
GRANT SELECT ON TABLE public.operations_view TO finance_app;


--
-- TOC entry 5001 (class 0 OID 0)
-- Dependencies: 229
-- Name: TABLE payees; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,INSERT ON TABLE public.payees TO finance_app;
GRANT SELECT ON TABLE public.payees TO finance_read;


--
-- TOC entry 5003 (class 0 OID 0)
-- Dependencies: 228
-- Name: SEQUENCE payees_payee_id_seq; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,USAGE ON SEQUENCE public.payees_payee_id_seq TO finance_app;


--
-- TOC entry 5005 (class 0 OID 0)
-- Dependencies: 219
-- Name: SEQUENCE users_user_id_seq; Type: ACL; Schema: public; Owner: postgres
--

GRANT SELECT,USAGE ON SEQUENCE public.users_user_id_seq TO finance_app;


-- Completed on 2025-12-18 06:12:59

--
-- PostgreSQL database dump complete
--

\unrestrict 4XTjCDpGhcHVs6xmtF09tI19eath8gLChvZIbTaiVwvRGHfQnqlvWzBDMFxDiCH

