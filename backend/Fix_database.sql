DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS sells;
DROP TABLE IF EXISTS seller;
DROP TABLE IF EXISTS product_types;
DROP TABLE IF EXISTS product_sizes;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS address;
DROP TABLE IF EXISTS addition;

CREATE TABLE products (
product_id INTEGER PRIMARY KEY AUTOINCREMENT ,
seller_id INTEGER,
title TEXT,
price INTEGER,
rating INTEGER,
rating_count INTEGER
);

CREATE TABLE sells(
sell_id INTEGER PRIMARY KEY AUTOINCREMENT ,
product_id INTEGER,
seller_id INTEGER,
client_id INTEGER,
date_of_sale TEXT,
date_of_insertion TEXT,
status_id TEXT,
items_count INTEGER,
address_id INTEGER
);

CREATE TABLE seller(
seller_id INTEGER PRIMARY KEY AUTOINCREMENT ,
title TEXT,
first_name TEXT,
last_name TEXT,
rating REAL,
registration_date TEXT
);

CREATE TABLE user(
user_id INTEGER PRIMARY KEY AUTOINCREMENT ,
login TEXT UNIQUE,
password TEXT,
phone INTEGER,
email TEXT
);

CREATE TABLE addition(
addition_id INTEGER PRIMARY KEY AUTOINCREMENT ,
product_id INTEGER,
seller_id INTEGER,
items_count INTEGER,
size TEXT,
date_of_adding REAL,
is_written_of INTEGER
);

CREATE TABLE address(
address_id INTEGER PRIMARY KEY AUTOINCREMENT ,
address TEXT
);

CREATE TABLE product_sizes(
size_id INTEGER PRIMARY KEY AUTOINCREMENT ,
product_id INTEGER,
size TEXT,
items_count INTEGER
);
CREATE TABLE product_types(
type_id INTEGER PRIMARY KEY AUTOINCREMENT ,
description TEXT,
product_id INTEGER
);


-- Ключ з size до продуктс(product_id)
create table product_sizes_dg_tmp
(
    size_id     INTEGER
        primary key autoincrement,
    product_id  INTEGER
        constraint product_sizes
            references products,
    size        TEXT,
    items_count INTEGER
);

insert into product_sizes_dg_tmp(size_id, product_id, size, items_count)
select size_id, product_id, size, items_count
from product_sizes;

drop table product_sizes;

alter table product_sizes_dg_tmp
    rename to product_sizes;


-- Ключ з type до продуктс(product_id)
create table product_types_dg_tmp
(
    type_id     INTEGER
        primary key autoincrement,
    description TEXT,
    product_id  INTEGER
        constraint product_types
            references products
);

insert into product_types_dg_tmp(type_id, description, product_id)
select type_id, description, product_id
from product_types;

drop table product_types;

alter table product_types_dg_tmp
    rename to product_types;


-- Ключ з addition до продуктс(product_id)
create table addition_dg_tmp
(
    addition_id    INTEGER
        primary key autoincrement,
    product_id     INTEGER
        constraint addition
            references products,
    seller_id      INTEGER,
    items_count    INTEGER,
    size           TEXT,
    date_of_adding REAL,
    is_written_of  INTEGER
);

insert into addition_dg_tmp(addition_id, product_id, seller_id, items_count, size, date_of_adding, is_written_of)
select addition_id, product_id, seller_id, items_count, size, date_of_adding, is_written_of
from addition;

drop table addition;

alter table addition_dg_tmp
    rename to addition;


--Ключ з продуктс до seller(seller_id)
create table products_dg_tmp
(
    product_id   INTEGER
        primary key autoincrement,
    seller_id    INTEGER
        constraint products
            references seller,
    title        TEXT,
    price        INTEGER,
    rating       INTEGER,
    rating_count INTEGER
);

insert into products_dg_tmp(product_id, seller_id, title, price, rating, rating_count)
select product_id, seller_id, title, price, rating, rating_count
from products;

drop table products;

alter table products_dg_tmp
    rename to products;
