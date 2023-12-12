--     sellers info
INSERT INTO seller(title, fullname, rating, registration_date) VALUES('BestFest', 'Назар Шайнога', 3.9,'2023-02-17');
INSERT INTO seller(title, fullname, rating, registration_date) VALUES('Barsine', 'Андрій Матвіїв', 3.0,'2022-11-13');
INSERT INTO seller(title, fullname, rating, registration_date) VALUES('Erfurt', 'Олександр Якимів', 2.2,'2023-05-28');


--      example products
INSERT INTO products(seller_id, title, price) VALUES(1, 'Black pants', 669.99);
INSERT INTO products(seller_id, title, price) VALUES(1, 'Moody Shirt', 399.99);
INSERT INTO products(seller_id, title, price) VALUES(3, 'Example Jacket', 2000);
INSERT INTO products(seller_id, title, price) VALUES(2, 'White pants', 799.99);
INSERT INTO products(seller_id, title, price) VALUES(3, 'T-Shirt lalala', 349.99);
INSERT INTO products(seller_id, title, price) VALUES(2, 'FootweaRR', 349.99);
INSERT INTO products(seller_id, title, price) VALUES(1, 'Jack', 4999.99);



--   Shirt  T-Shirt  Pants  Jacket  Footwear
INSERT INTO types(description, product_id) VALUES ('Pants', 1);
INSERT INTO types(description, product_id) VALUES ('Pants', 4);
INSERT INTO types(description, product_id) VALUES ('Jacket', 3);
INSERT INTO types(description, product_id) VALUES ('Jacket', 7);
INSERT INTO types(description, product_id) VALUES ('T-Shirt',5);
INSERT INTO types(description, product_id) VALUES ('Shirt', 2);
INSERT INTO types(description, product_id) VALUES ('Footwear', 6);



--   «XS»   «S»   «M»   «L»   «XL»   «XXL»
INSERT INTO sizes(product_id, size, items_count) VALUES (1, 'L', 3 );
INSERT INTO sizes(product_id, size, items_count) VALUES (1, 'XL', 4 );
INSERT INTO sizes(product_id, size, items_count) VALUES (2, 'M', 12);
INSERT INTO sizes(product_id, size, items_count) VALUES (3, 'XS', 3);
INSERT INTO sizes(product_id, size, items_count) VALUES (3, 'S', 2);
INSERT INTO sizes(product_id, size, items_count) VALUES (3, 'L', 5);
INSERT INTO sizes(product_id, size, items_count) VALUES (4, 'XXL', 7 );
INSERT INTO sizes(product_id, size, items_count) VALUES (4, 'XL', 5 );
INSERT INTO sizes(product_id, size, items_count) VALUES (5, 'M', 2);
INSERT INTO sizes(product_id, size, items_count) VALUES (5, 'S', 2);
INSERT INTO sizes(product_id, size, items_count) VALUES (5, 'L', 4);
INSERT INTO sizes(product_id, size, items_count) VALUES (6, 'XS', 17);
INSERT INTO sizes(product_id, size, items_count) VALUES (7, 'M', 1 );
INSERT INTO sizes(product_id, size, items_count) VALUES (7, 'XL', 3 );

--   product colors
INSERT INTO color(product_id, color, items_count) VALUES (1, 'Black', 2 );
INSERT INTO color(product_id, color, items_count) VALUES (1, 'Grey', 1 );
INSERT INTO color(product_id, color, items_count) VALUES (2, 'White', 4 );
INSERT INTO color(product_id, color, items_count) VALUES (3, 'Orange', 5 );
INSERT INTO color(product_id, color, items_count) VALUES (3, 'Yellow', 11 );
INSERT INTO color(product_id, color, items_count) VALUES (4, 'Red', 7 );
INSERT INTO color(product_id, color, items_count) VALUES (4, 'Yellow', 2 );
INSERT INTO color(product_id, color, items_count) VALUES (4, 'Black', 10 );
INSERT INTO color(product_id, color, items_count) VALUES (5, 'Grey', 1 );
INSERT INTO color(product_id, color, items_count) VALUES (6, 'White', 6 );
INSERT INTO color(product_id, color, items_count) VALUES (7, 'Pink', 7 );
