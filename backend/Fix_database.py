DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS sells;
DROP TABLE IF EXISTS seller;
DROP TABLE IF EXISTS product_types;
DROP TABLE IF EXISTS product_sizes;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS address;
DROP TABLE IF EXISTS addition;

CREATE TABLE products (
product_id INT PRIMARY KEY,
seller_id INT,
title VARCHAR(20),
type INT,
size INT,
price INT,
rating INT,
rating_count INT
);

CREATE TABLE sells(
sell_id INT PRIMARY KEY,
product_id INT,
seller_id INT,
client_id INT,
date_of_sale DATE,
date_of_insertion DATE,
status_id VARCHAR(15),
items_count INT,
address_id INT
);

CREATE TABLE seller(
seller_id INT PRIMARY KEY,
title VARCHAR(30),
first_name VARCHAR (15),
last_name VARCHAR (20),
rating INT,
registration_date DATE
);

CREATE TABLE user(
user_id INT PRIMARY KEY,
login VARCHAR(20) UNIQUE,
password VARCHAR(30),
phone INT,
email VARCHAR(20)
);

CREATE TABLE addition(
addition_id INT PRIMARY KEY,
product_id INT,
seller_id INT,
items_count INT,
size VARCHAR(4),
date_of_adding DATE,
is_written_of INT
);

CREATE TABLE address(
address_id INT PRIMARY KEY,
address VARCHAR(40)
);

CREATE TABLE product_sizes(
size_id INT PRIMARY KEY,
product_id INT,
size VARCHAR(4),
items_count INT
);
CREATE TABLE product_types(
type_id INT PRIMARY KEY,
description VARCHAR(200),
product_id INT
);


-- Ключ з size до продуктс(product_id)
create table product_sizes_dg_tmp
(
    size_id     INT
        primary key,
    product_id  INT
        constraint product_sizes
            references products,
    size        VARCHAR(4),
    items_count INT
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
    type_id     INT
        primary key,
    description VARCHAR(200),
    product_id  INT
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
    addition_id    INT
        primary key,
    product_id     INT
        constraint addition
            references products,
    seller_id      INT,
    items_count    INT,
    size           VARCHAR(4),
    date_of_adding DATE,
    is_written_of  INT
);

insert into addition_dg_tmp(addition_id, product_id, seller_id, items_count, size, date_of_adding, is_written_of)
select addition_id, product_id, seller_id, items_count, size, date_of_adding, is_written_of
from addition;

drop table addition;

alter table addition_dg_tmp
    rename to addition;



-- Ключ з продуктс до size(size_id)
create table products_dg_tmp
(
    product_id   INT
        primary key,
    seller_id    INT,
    title        VARCHAR(20),
    type         INT,
    size         INT
        constraint products
            references product_sizes,
    price        INT,
    rating       INT,
    rating_count INT
);

insert into products_dg_tmp(product_id, seller_id, title, type, size, price, rating, rating_count)
select product_id,
       seller_id,
       title,
       type,
       size,
       price,
       rating,
       rating_count
from products;

drop table products;

alter table products_dg_tmp
    rename to products;



-- Ключ з продуктс до types(type_id)
create table products_dg_tmp
(
    product_id   INT
        primary key,
    seller_id    INT,
    title        VARCHAR(20),
    type         INT
        constraint products
            references product_types,
    size         INT
        constraint products
            references product_sizes,
    price        INT,
    rating       INT,
    rating_count INT
);

insert into products_dg_tmp(product_id, seller_id, title, type, size, price, rating, rating_count)
select product_id,
       seller_id,
       title,
       type,
       size,
       price,
       rating,
       rating_count
from products;

drop table products;

alter table products_dg_tmp
    rename to products;


-- Ключ з продуктс до seller(seller_id)
create table products_dg_tmp
(
    product_id   INT
        primary key,
    seller_id    INT
        constraint products
            references seller,
    title        VARCHAR(20),
    type         INT
        constraint products
            references product_types,
    size         INT
        constraint products
            references product_sizes,
    price        INT,
    rating       INT,
    rating_count INT
);

insert into products_dg_tmp(product_id, seller_id, title, type, size, price, rating, rating_count)
select product_id,
       seller_id,
       title,
       type,
       size,
       price,
       rating,
       rating_count
from products;

drop table products;

alter table products_dg_tmp
    rename to products;

