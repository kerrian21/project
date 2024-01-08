
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

product_id = input()
conn = sqlite3.connect('identifier.sqlite', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('SELECT seller_id, title, color, price, rating, rating_count FROM products WHERE product_id = ?',
                       (product_id,))

product = cursor.fetchone()
print(product)
if product:
    cursor.execute(
                'INSERT INTO products (seller_id, title, color, price, rating, rating_count) VALUES (?, ?, ?, ?, ?, ?)',
                (product[0], product[1], product[2], product[3], product[4], product[5]))
    conn.commit()
product_id_tuple = (product_id,)
cursor.execute('SELECT * FROM products WHERE product_id IN ({})'.format(','.join(['?'] * len(product_id_tuple))), product_id_tuple)
basket_items = cursor.fetchall()
print(basket_items)
placeholders = ','.join(['?'] * len(product_id))
cursor.execute('DELETE FROM products WHERE product_id IN ({})'.format(placeholders),product_id)
conn.commit()











