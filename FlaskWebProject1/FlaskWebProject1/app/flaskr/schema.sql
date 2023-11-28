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

INSERT INTO seller(title, first_name, last_name, rating, registration_date) VALUES('BestFest', 'Назар', 'Шайнога', 3.9,'2023-02-17');
INSERT INTO seller(title, first_name, last_name, rating, registration_date) VALUES('Barsine', 'Андрій', 'Матвіїв', 3.0,'2022-11-13');
INSERT INTO seller(title, first_name, last_name, rating, registration_date) VALUES('Erfurt', 'Олександр', 'Якимів', 2.2,'2023-05-28');



INSERT INTO products(seller_id, title, price) VALUES(1, 'Black pants', 669.99);
INSERT INTO products(seller_id, title, price) VALUES(1, 'Moody Shirt', 399.99);
INSERT INTO products(seller_id, title, price) VALUES(3, 'Example Jacket', 2000);
INSERT INTO products(seller_id, title, price) VALUES(2, 'White pants', 799.99);
INSERT INTO products(seller_id, title, price) VALUES(3, 'T-Shirt lalala', 349.99);
INSERT INTO products(seller_id, title, price) VALUES(2, 'FootweaRR', 349.99);
INSERT INTO products(seller_id, title, price) VALUES(1, 'Jack', 4999.99);



--   Shirt  T-Shirt  Pants  Jacket  Footwear
INSERT INTO product_types(description, product_id) VALUES ('Pants', 11);
INSERT INTO product_types(description, product_id) VALUES ('Pants', 14);
INSERT INTO product_types(description, product_id) VALUES ('Jacket', 13);
INSERT INTO product_types(description, product_id) VALUES ('Jacket', 17);
INSERT INTO product_types(description, product_id) VALUES ('T-Shirt',15);
INSERT INTO product_types(description, product_id) VALUES ('Shirt', 12);
INSERT INTO product_types(description, product_id) VALUES ('Footwear', 16);



--   «XS»   «S»   «M»   «L»   «XL»   «XXL»
INSERT INTO product_sizes(product_id, size, items_count) VALUES (11, 'L', 3 );
INSERT INTO product_sizes(product_id, size, items_count) VALUES (11, 'XL', 4 );
INSERT INTO product_sizes(product_id, size, items_count) VALUES (12, 'M', 12);
INSERT INTO product_sizes(product_id, size, items_count) VALUES (13, 'XS', 3);
INSERT INTO product_sizes(product_id, size, items_count) VALUES (13, 'S', 2);
INSERT INTO product_sizes(product_id, size, items_count) VALUES (13, 'L', 5);
INSERT INTO product_sizes(product_id, size, items_count) VALUES (14, 'XXL', 7 );
INSERT INTO product_sizes(product_id, size, items_count) VALUES (14, 'XL', 5 );
INSERT INTO product_sizes(product_id, size, items_count) VALUES (15, 'M', 2);
INSERT INTO product_sizes(product_id, size, items_count) VALUES (15, 'S', 2);
INSERT INTO product_sizes(product_id, size, items_count) VALUES (15, 'L', 4);
INSERT INTO product_sizes(product_id, size, items_count) VALUES (16, 'XS', 17);
INSERT INTO product_sizes(product_id, size, items_count) VALUES (17, 'M', 1 );
INSERT INTO product_sizes(product_id, size, items_count) VALUES (17, 'XL', 3 );
