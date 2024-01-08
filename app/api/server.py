from flask import Flask, render_template, request, redirect, url_for
import sqlite3


app = Flask(__name__)

conn = sqlite3.connect('identifier.sqlite', check_same_thread=False)
cursor = conn.cursor()

ratings_data = {}

def store_rating(product_id, rating):
    if product_id in ratings_data:
        ratings_data[product_id].append(rating)
    else:
        ratings_data[product_id] = [rating]

def calculate_average_rating():
    all_ratings = [rating for ratings_list in ratings_data.values() for rating in ratings_list]
    return sum(all_ratings) / len(all_ratings) if len(all_ratings) > 0 else 0

def check_user_exists(username, email, phone_number, password):
    conn = sqlite3.connect('schema.sql')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ? OR email = ? OR phone_number = ? OR password = ?', (username, email, phone_number, password))
    result = cursor.fetchone()

    conn.close()

    return result is not None

def group_by_product_key(results):
    grouped_results = {}
    for item in results:
        product_key = (item[0], item[1], item[2], item[3], item[4])
        if product_key not in grouped_results:
            grouped_results[product_key] = []
        grouped_results[product_key].append(item[5])
    return grouped_results

@app.route('/')
def index():
    cursor.execute('''
                    SELECT products.product_id, products.title, products.color, products.price, products.rating, sizes.size
                    FROM products
                    JOIN sizes ON products.product_id = sizes.product_id
                    ORDER BY products.price ASC
                ''')
    result = cursor.fetchall()
    return render_template('index.html', result=result)

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        phone_number = request.form['phone_number']
        password = request.form['password']

        if check_user_exists(username, email, phone_number, password):
            return "Sorry, your information was not saved. Please enter your information again." and redirect('/')
        else:
            conn = sqlite3.connect('schema.sql')
            cursor = conn.cursor()

            cursor.execute('INSERT INTO users (username, email, phone_number, password) VALUES (?, ?, ?, ?)',
                           (username, email, phone_number, password))

            conn.commit()
            conn.close()

            return "Your information was successfully saved" and redirect('/')

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        query = request.form.get('query')

        try:
            product_id_query = int(query)
        except ValueError:
            product_id_query = None

        base_sql_query = '''
            SELECT products.product_id, products.title, products.color, products.price, products.rating, sizes.size
            FROM products
            JOIN sizes ON products.product_id = sizes.product_id
            '''

        if product_id_query is not None:
            id_sql_query = base_sql_query + 'WHERE products.product_id = ?'
            id_params = (product_id_query,)
            cursor.execute(id_sql_query, id_params)
            id_results = cursor.fetchall()
        else:
            id_results = []

        title_sql_query = base_sql_query + 'WHERE products.title LIKE ? COLLATE NOCASE'
        title_params = (f'%{query}%',)
        cursor.execute(title_sql_query, title_params)
        title_results = cursor.fetchall()

        color_sql_query = base_sql_query + 'WHERE products.color LIKE ? COLLATE NOCASE'
        color_params = (f'%{query}%',)
        cursor.execute(color_sql_query, color_params)
        color_results = cursor.fetchall()

        price_sql_query = base_sql_query + 'WHERE products.price LIKE ? COLLATE NOCASE ORDER BY products.price ASC'
        price_params = (f'%{query}%',)
        cursor.execute(price_sql_query, price_params)
        price_results = cursor.fetchall()

        rating_sql_query = base_sql_query + 'WHERE products.rating LIKE ? COLLATE NOCASE'
        rating_params = (f'%{query}%',)
        cursor.execute(rating_sql_query, rating_params)
        rating_results = cursor.fetchall()

        size_sql_query = base_sql_query + 'WHERE sizes.size LIKE ? COLLATE NOCASE'
        size_params = (f'%{query}%',)
        cursor.execute(size_sql_query, size_params)
        size_results = cursor.fetchall()

        all_results = id_results + title_results + color_results + price_results + rating_results + size_results
        grouped_results = {}

        for result in all_results:
            product_id, title, color, price, rating, size = result[:6] + (None,) * (6 - len(result))

            if product_id not in grouped_results:
                grouped_results[product_id] = {'product_id': product_id, 'title': title, 'color': color, 'price': price, 'rating': rating, 'sizes': []}

            if size:
                grouped_results[product_id]['sizes'].append(size)

        unique_results = list(grouped_results.values())

        return render_template('search_results.html', results=unique_results)


@app.route('/catalog', methods=['POST','GET'])
def catalog():
    if request.method == 'POST':
        name = request.form['clothes']

        query = """
            SELECT products.product_id, products.title, products.color, products.price, products.rating, sizes.size
            FROM products
            JOIN sizes ON products.product_id = sizes.product_id
            JOIN types ON products.product_id = types.product_id
            WHERE types.description = ?
            ORDER BY products.price ASC;
        """

        cursor.execute(query, (name,))
        result = cursor.fetchall()

        template_name = f'{name.lower()}.html'
        return render_template(template_name, result=result)

@app.route('/filter_price', methods=['POST', 'GET'])
def filter_price():
    if request.method == 'GET':
        name = request.args.get('name')

        if name:
            cursor.execute('''
                SELECT products.product_id, products.title, products.color, products.price, products.rating, sizes.size
                FROM products
                JOIN sizes ON products.product_id = sizes.product_id
                WHERE products.price LIKE ? COLLATE NOCASE
                ORDER BY products.price ASC
            ''', ('%' + name + '%',))
            exact_result = cursor.fetchall()

            if exact_result:
                # Assuming you have a function to group results by product key
                grouped_results = group_by_product_key(exact_result)
                message = f"Here is what was found for your query '{name}'."
                return render_template('results.html', message=message, results=exact_result, grouped_results=grouped_results)
            else:
                cursor.execute('''
                    SELECT products.product_id, products.title, products.color, products.price, products.rating, sizes.size
                    FROM products
                    JOIN sizes ON products.product_id = sizes.product_id
                    WHERE products.price LIKE ? COLLATE NOCASE
                    ORDER BY products.price ASC
                ''', ('%' + name + '%',))
                similar_result = cursor.fetchall()

                if similar_result:
                    message = f"Unfortunately, no prices were found for your request '{name}', but similar ones were found."
                    return render_template('results.html', message=message, results=similar_result)
                else:
                    message = f"Sorry, nothing was found for your request '{name}'."
                    return render_template('results.html', message=message)


@app.route('/add_to_basket', methods=['GET', 'POST'])
def add_to_basket():
    if request.method == 'POST':
        product_id = request.json.get('product_id')
        print(product_id)

        cursor.execute('SELECT product_id, title, color, price FROM products WHERE product_id = ?',
                       (product_id,))
        product = cursor.fetchone()
        print(product)

        if product:

            cursor.execute(
                'INSERT INTO basket (product_id, title, color, price) VALUES (?, ?, ?, ?)',
                (product[0], product[1], product[2], product[3]))
            conn.commit()
        return redirect('/')


@app.route('/basket', methods=['GET', 'POST'])
def view_basket():
    if request.method == 'GET':
        product_ids = request.args.get('product_id', '').split(',')

        cursor = conn.cursor()

        cursor.execute('SELECT * FROM basket WHERE product_id IN ({})'.format(','.join(['?'] * len(product_ids))), product_ids)
        basket_items = cursor.fetchall()
        print(basket_items)


        return render_template('besket.html', basket_items=basket_items)

    elif request.method == 'POST':
        product_ids_to_remove = request.form.getlist('product_id')

        cursor = conn.cursor()

        placeholders = ','.join(['?'] * len(product_ids_to_remove))
        cursor.execute('DELETE FROM basket WHERE product_id IN ({})'.format(placeholders), product_ids_to_remove)
        conn.commit()
        return redirect('/basket')

@app.route('/title', methods = ['POST', 'GET'])
def title():
    if request.method == 'GET':
        product_ids = request.args.getlist('product_id')
        cursor.execute('''
            SELECT products.seller_id, products.title, products.color, products.price, products.rating, sizes.size
            FROM products
            JOIN sizes ON products.product_id = sizes.product_id
            WHERE products.product_id IN ({})
        '''.format(','.join(['?'] * len(product_ids))), product_ids)
        result_title = cursor.fetchall()
        print(result_title)
        return render_template('title.html', result=result_title)

@app.route('/rating', methods = ['POST', 'GET'])
def rating():
    if request.method == 'POST':
        product_id = request.form['product_id']
        rating = int(request.form['rating'])

        store_rating(product_id, rating)

        average_rating = calculate_average_rating()

        average_rating = round(average_rating, 1)

        cursor.execute('''
                   SELECT product_id FROM products WHERE product_id = ?
               ''', (product_id,))
        result = cursor.fetchone()

        if result:
            cursor.execute('''
                       UPDATE products SET rating = ? WHERE product_id = ?
                   ''', (average_rating, product_id))
        return redirect('/')

@app.route('/filter_rating', methods=['POST', 'GET'])
def filter_rating():
    if request.method == 'GET':
        name = request.args.get('name')

        if name:
            cursor.execute('''
                SELECT products.product_id, products.title, products.color, products.price, products.rating, sizes.size
                FROM products
                JOIN sizes ON products.product_id = sizes.product_id
                WHERE products.rating LIKE ? COLLATE NOCASE
                ORDER BY products.price ASC
            ''', ('%' + name + '%',))
            exact_result = cursor.fetchall()

            if exact_result:
                grouped_results = group_by_product_key(exact_result)
                message = f"Here is what was found for your query '{name}'."
                return render_template('rating.html', message=message, results=exact_result, grouped_results=grouped_results)
            else:
                cursor.execute('''
                    SELECT products.product_id, products.title, products.color, products.price, products.rating, sizes.size
                    FROM products
                    JOIN sizes ON products.product_id = sizes.product_id
                    WHERE products.rating LIKE ? COLLATE NOCASE
                    ORDER BY products.price ASC
                ''', ('%' + name + '%',))
                similar_result = cursor.fetchall()

                if similar_result:
                    message = f"Unfortunately, no ratings were found for your request '{name}', but similar ones were found."
                    return render_template('rating.html', message=message, results=similar_result)
                else:
                    message = f"Sorry, nothing was found for your request '{name}'."
                    return render_template('rating.html', message=message)


@app.route('/filter_size', methods=['POST', 'GET'])
def filter_size():
    if request.method == 'POST':
        query = request.form.get('query')
        parts = query.split()

        if not parts:
            return render_template('sizes.html', results=[])

        placeholders = ','.join(['?' for _ in parts])

        sql_query = f'''
                SELECT products.product_id, products.title, products.color, products.price, products.rating, sizes.size
                FROM products
                JOIN sizes ON products.product_id = sizes.product_id
                WHERE sizes.size IN ({placeholders})
            '''

        cursor.execute(sql_query, parts)
        size_results = cursor.fetchall()
        return render_template('sizes.html', results=size_results)

@app.route('/search_basket', methods=['GET', 'POST'])
def search_basket():
    if request.method == 'POST':
        query = request.form.get('query')

        title_sql_query = 'SELECT product_id, title, color, price FROM products WHERE title LIKE ? COLLATE NOCASE'
        title_params = (f'%{query}%',)
        cursor.execute(title_sql_query, title_params)
        title_results = cursor.fetchall()

        color_sql_query = 'SELECT product_id, title, color, price FROM products WHERE color LIKE ? COLLATE NOCASE'
        color_params = (f'%{query}%',)
        cursor.execute(color_sql_query, color_params)
        color_results = cursor.fetchall()

        price_sql_query = 'SELECT product_id, title, color, price FROM products WHERE price LIKE ? COLLATE NOCASE'
        price_params = (f'%{query}%',)
        cursor.execute(price_sql_query, price_params)
        price_results = cursor.fetchall()

        unique_results = []

        all_results = title_results + color_results + price_results

        unique_titles_set = set()
        for result in all_results:
            product_id, title, color, price = result[:4] + (None,) * (4 - len(result))

            title_lower = title.lower()

            if title_lower not in unique_titles_set:
                unique_titles_set.add(title_lower)
                unique_results.append({'product_id': product_id, 'title': title, 'color': color, 'price': price})

        return render_template('search_basket.html', results=unique_results)

@app.route('/authorization', methods=['GET', 'POST'])
def authorization():
        conn = sqlite3.connect('identifier.sqlite', check_same_thread=False)
        cursor = conn.cursor()

        if request.method == 'POST':
            login = request.form.get('login')
            password = request.form.get('password')
            phone = request.form.get('phone')
            email = request.form.get('email')

            cursor.execute('SELECT * FROM user WHERE login = ? OR email = ?', (login, email))
            existing_user = cursor.fetchone()

            if existing_user:
                return render_template('error.html', message='User already exists')

            cursor.execute('INSERT INTO user (login, password, phone, email) VALUES (?, ?, ?, ?)',
                           (login, password, phone, email))
            conn.commit()
            conn.close()
            return render_template('success.html', message='Registration completed successfully')

        conn.close()
        return render_template('authorization.html')

@app.route('/profile', methods=['GET', 'POST'])
def portfolio():
    if request.method == 'GET':
        login = request.args.get('login')
        password = request.args.get('password')

        # Assuming 'login' and 'password' are passed as query parameters in the URL

        cursor.execute('SELECT login, email, phone FROM user WHERE login = ? AND password = ?', (login, password))
        result = cursor.fetchall()


        return render_template('profile.html', result=result)

    return render_template('profile_result.html')




@app.route('/profile_result', methods=['GET', 'POST'])
def profile_result():
    if request.method == 'GET':
        login = request.args.get('login')
        password = request.args.get('password')
        cursor.execute('SELECT login, email, phone FROM user WHERE login = ? AND password = ?', (login, password))
        result = cursor.fetchall()
        return render_template('profile_result.html', result=result)

@app.route('/profile_delete', methods=['GET', 'POST'])
def profile_delete():
        return render_template('profile_delete.html')

@app.route('/profile_delete_result', methods=['GET', 'POST'])
def profile_delete_result():
    if request.method == 'GET':
        login = request.args.get('login')
        password = request.args.get('password')
        cursor.execute('DELETE FROM user WHERE login = ? AND password = ?', (login, password))
        conn.commit()
        return render_template('profile_delete_result.html', message='Removed profile')
if __name__ == '__main__':
    app.run(debug=True)
