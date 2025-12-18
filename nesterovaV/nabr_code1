CREATE TABLE people (
    id_p serial4 primary key,
    name varchar(100) not null,
    second_name varchar(100) not null,
    three_name varchar(100),
    data_hbd date not null,
    data_start date not null,
    data_accreditation date not null
);

CREATE TABLE otdel (
    id_ot serial4 primary key,
    name_otdel varchar(100) not null
);

CREATE TABLE post (
    id_post serial4 primary key,
    name_post varchar(100) not null
);

CREATE TABLE accreditation (
    id_acc serial4 primary key,
    type_acc varchar(100) not null
);

CREATE TABLE cval (
    id_cval serial4 primary key,
    type_cval varchar(100) not null
);

CREATE OR REPLACE FUNCTION get_people()
RETURNS TABLE (
    name varchar,
    second_name varchar,
    three_name varchar,
    data_hbd date,
    data_start date,
    data_accreditation date
)
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        name,
        second_name,
        three_name,
        data_hbd,
        data_start,
        data_accreditation
    FROM people;
END;
$$ LANGUAGE plpgsql;
