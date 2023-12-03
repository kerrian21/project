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
