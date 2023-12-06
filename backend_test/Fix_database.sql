DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS sells;
DROP TABLE IF EXISTS seller;
DROP TABLE IF EXISTS product_types;
DROP TABLE IF EXISTS product_sizes;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS address;
DROP TABLE IF EXISTS addition;
DROP TABLE IF EXISTS color;


create table address
(
    address_id INTEGER,
    address    TEXT,
    primary key (address_id autoincrement)
);

create table seller
(
    seller_id         INTEGER,
    title             TEXT,
    fullname          TEXT,
    rating            REAL,
    registration_date TEXT,
    primary key (seller_id autoincrement)
);

create table products
(
    product_id   INTEGER,
    seller_id    INTEGER,
    title        TEXT,
    price        REAL,
    rating       INTEGER,
    rating_count INTEGER,
    color        TEXT,
    primary key (product_id autoincrement),
    constraint products
        foreign key (seller_id) references seller
);

create table addition
(
    addition_id    INTEGER,
    product_id     INTEGER,
    seller_id      INTEGER,
    items_count    INTEGER,
    size           TEXT,
    date_of_adding REAL,
    is_written_of  INTEGER,
    primary key (addition_id autoincrement),
    constraint addition
        foreign key (product_id) references products
);

create table color
(
    color_id    integer,
    product_id  integer,
    color       text,
    items_count integer,
    primary key (color_id autoincrement),
    constraint color
        foreign key (product_id) references products
);

create table sells
(
    sell_id           INTEGER,
    product_id        INTEGER,
    seller_id         INTEGER,
    client_id         INTEGER,
    date_of_sale      TEXT,
    date_of_insertion TEXT,
    status_id         TEXT,
    items_count       INTEGER,
    address_id        INTEGER,
    primary key (sell_id autoincrement)
);

create table sizes
(
    size_id     INTEGER,
    product_id  INTEGER,
    size        TEXT,
    items_count INTEGER,
    primary key (size_id autoincrement),
    constraint sizes
        foreign key (product_id) references products
);

create table types
(
    type_id     INTEGER,
    description TEXT,
    product_id  INTEGER,
    primary key (type_id autoincrement),
    constraint types
        foreign key (product_id) references products
);

create table user
(
    user_id  INTEGER,
    login    TEXT,
    password TEXT,
    phone    INTEGER,
    email    TEXT,
    primary key (user_id autoincrement),
    unique (login)
);
