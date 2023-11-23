CREATE TABLE products (
product_id INT PRIMARY KEY,
seller_id INT,
title VARCHAR(20),
price INT,
rating INT,
rating_count INT,
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
CREATE TABLE clients(
client_id INT PRIMARY KEY,
login VARCHAR(20),
passwrd VARCHAR(30),
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
adress_id INT PRIMARY KEY,
adress VARCHAR(40)
);

CREATE TABLE product_sizes(
size_id INT PRIMARY KEY,
product_id INT,
size VARCHAR(4),
items_count INT
);
CREATE TABLE product_types(
type_id INT PRIMARY KEY,
descriptionn VARCHAR(200),
product_id INT
);


ALTER TABLE product_sizes
ADD FOREIGN KEY(product_id)
REFERENCES  products(product_id)
ON DELETE SET NULL;


ALTER TABLE addition
ADD FOREIGN KEY(product_id)
REFERENCES  products(product_id)
ON DELETE SET NULL;


ALTER TABLE addition
ADD FOREIGN KEY(seller_id)
REFERENCES  seller(seller_id)
ON DELETE SET NULL;


ALTER TABLE products
ADD FOREIGN KEY(size)
REFERENCES  product_sizes(size_id)
ON DELETE SET NULL;



ALTER TABLE products
ADD FOREIGN KEY(type)
REFERENCES  product_types(type_id)
ON DELETE SET NULL;
ALTER TABLE products
ADD FOREIGN KEY(seller_id)
REFERENCES  seller(seller_id)
ON DELETE SET NULL;


ALTER TABLE sells
ADD FOREIGN KEY(seller_id)
REFERENCES  seller(seller_id)
ON DELETE SET NULL;


ALTER TABLE sells
ADD FOREIGN KEY(client_id)
REFERENCES  clients(client_id)
ON DELETE SET NULL;


ALTER TABLE sells
ADD FOREIGN KEY(address_id)
REFERENCES  address(adress_id)
ON DELETE SET NULL;


ALTER TABLE sells
ADD FOREIGN KEY(product_id)
REFERENCES products(product_id)
ON DELETE SET NULL;
