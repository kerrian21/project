from flask import Flask, render_template, request, redirect
import sqlite3


app = Flask(__name__)


conn = sqlite3.connect('identifier.sqlite', check_same_thread=False)
cursor = conn.cursor()



def check_user_exists(username, email, phone_number, password):
    conn = sqlite3.connect('schema.sql')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ? OR email = ? OR phone_number = ? OR password = ?', (username, email, phone_number, password))
    result = cursor.fetchone()

    conn.close()

    return result is not None


@app.route('/')
def index():
    cursor.execute('SELECT title, color, price FROM products ORDER BY price ASC')
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

@app.route('/search', methods=['POST','GET'])
def search():
    if request.method == 'POST':
        query = request.form.get('query')
        parts = query.split()

        title_query = ' '.join(parts)
        title_sql_query = 'SELECT title, color, price FROM products WHERE title LIKE ? COLLATE NOCASE'
        title_params = (f'%{title_query}%',)
        cursor.execute(title_sql_query, title_params)
        title_results = cursor.fetchall()

        color_query = parts[-1]
        color_sql_query = 'SELECT title, color, price FROM products WHERE color LIKE ? COLLATE NOCASE'
        color_params = (f'%{color_query}%',)
        cursor.execute(color_sql_query, color_params)
        color_results = cursor.fetchall()

        price_sql_query = 'SELECT title, color, price FROM products WHERE price LIKE ? COLLATE NOCASE'
        price_params = (f'%{query}%',)
        cursor.execute(price_sql_query, price_params)
        price_results = cursor.fetchall()

        combined_sql_query = 'SELECT title, color, price FROM products WHERE title LIKE ? COLLATE NOCASE AND color LIKE ? COLLATE NOCASE AND price LIKE ? COLLATE NOCASE'
        combined_params = (f'%{title_query}%', f'%{color_query}%', f'%{query}%')
        cursor.execute(combined_sql_query, combined_params)
        combined_results = cursor.fetchall()

        if len(parts) >= 2:
            multi_title_query = ' '.join(parts)
            multi_title_sql_query = 'SELECT title, color, price FROM products WHERE title LIKE ? COLLATE NOCASE'
            multi_title_params = (f'%{multi_title_query}%',)
            cursor.execute(multi_title_sql_query, multi_title_params)
            multi_title_results = cursor.fetchall()
        else:
            multi_title_results = []

        all_results = title_results + color_results + price_results + combined_results + multi_title_results
        unique_results = []
        unique_titles_set = set()
        for result in all_results:
            title, color, price = result[:3] + (None,) * (3 - len(result))

            title_lower = title.lower()

            if title_lower not in unique_titles_set:
                unique_titles_set.add(title_lower)
                unique_results.append({'title': title, 'color': color, 'price': price})

        return render_template('search_results.html', results=unique_results)



@app.route('/catalog', methods=['POST','GET'])
def catalog():
        if request.method == 'POST':
            name = request.form['clothes']
            if name == 'Shirt':
                cursor.execute("""SELECT title, color, price FROM products 
                                        JOIN types ON products.product_id = types.product_id WHERE types.description = ?""",
                            (name,))
                result = cursor.fetchall()
                return render_template('shirt.html', result=result)

            elif name == 'T-Shirt':
                    cursor.execute("""SELECT title, color, price FROM products 
                                            JOIN types ON products.product_id = types.product_id WHERE types.description = ?""",
                                (name,))
                    result = cursor.fetchall()
                    return render_template('t-shirt.html', result=result)
            elif name == 'Jacket':
                    cursor.execute("""SELECT title, color, price FROM products 
                                            JOIN types ON products.product_id = types.product_id WHERE types.description = ?""",
                                (name,))
                    result = cursor.fetchall()
                    return render_template('jacket.html', result=result)
            elif name == 'Pants':
                    cursor.execute("""SELECT title, color, price FROM products 
                                           JOIN types ON products.product_id = types.product_id WHERE types.description = ?""",
                               (name,))
                    result = cursor.fetchall()
                    return render_template('pants.html', result=result)
            elif name == 'Footwear':
                    cursor.execute("""SELECT title, color, price FROM products 
                                           JOIN types ON products.product_id = types.product_id WHERE types.description = ?""",
                               (name,))
                    result = cursor.fetchall()
                    return render_template('footwear.html', result=result)



               
@app.route('/range', methods=['POST','GET'])
def _range_():
        if request.methods == 'POST':
            category = request.foorm['Category']
            name = request.form['Name products']
            color = request.form['Color']
            _range_ = request.form['Range']

            conn = sqlite3.connect('schema.sql')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products WHERE types = ? name = ? OR color = ?", (category, name, color))
            results_t_shirts = cursor.fetchall()  
            if results_t_shirts:
                    conn = sqlite3.connect('schema.sql')
                    cursor = conn.cursor()
                    cursor.execute("UPDATE products SET Range = ? WHERE types = ? name = ? OR color = ?", (_range_, category, name ,color ))
                    conn.commit()
                    conn.close()
                    return 'Updated'
            else:
                    return 'Not found'
 
@app.route('/filter_price', methods=['POST', 'GET'])
def filter_price():
    if request.method == 'GET':
        name = request.args.get('name')

        if name:
            cursor.execute('SELECT title, color, price FROM products WHERE price = ?', (name,))
            exact_result = cursor.fetchall()

            if exact_result:
                message = f"Here is what was found for your query '{name}'."
                return render_template('results.html', message=message, results=exact_result)
            else:
                cursor.execute('SELECT title, color, price FROM products WHERE price LIKE ? COLLATE NOCASE ORDER BY price ASC', ('%' + name + '%',))
                similar_result = cursor.fetchall()

                if similar_result:
                    message = f"Unfortunately, no prices were found for your request '{name}', but similar ones were found."
                    return render_template('results.html', message=message, results=similar_result)
                else:
                    message = f"Sorry, nothing was found for your request '{name}'."
                    return render_template('results.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
