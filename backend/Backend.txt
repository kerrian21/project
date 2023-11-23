from flask import Flask, render_template, request, redirect
import sqlite3


app = Flask(__name__)


conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def search_database(query):
    cursor.execute('''
        SELECT * FROM users
        WHERE name LIKE ? OR email LIKE ?
    ''', ('%' + query + '%', '%' + query + '%'))
    results = cursor.fetchall()
    return results


def check_user_exists(username, email, phone_number, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ? OR email = ? OR phone_number = ? OR password = ?', (username, email, phone_number, password))
    result = cursor.fetchone()

    conn.close()

    return result is not None


@app.route('/')
def index():
    return render_template('index.html', template2='search.html')

@app.route('/register', methods=['GET'])
def register():
    if request.method == 'GET':
        username = request.form['username']
        email = request.form['email']
        phone_number = request.form['phone_number']
        password = request.form['password']

        if check_user_exists(username, email, phone_number, password):
            return "Sorry, your information was not saved. Please enter your information again." and redirect('/')
        else:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            cursor.execute('INSERT INTO users (username, email, phone_number, password) VALUES (?, ?, ?, ?)',
                           (username, email, phone_number, password))

            conn.commit()
            conn.close()

            return "Your information was successfully saved" and redirect('/')

@app.route('/search', methods=['GET'])
def search():
   query = request.form['query']
   results = search_database(query)
   return render_template('search_results.html', results=results)

@app.route('/catalog')
    def catalog():
        if request.form['T-Short']:
                conn = sqlite3.connect('database.db')
                cursor = conn.cursor()
                cursor.execute("SELECT T-Shorts FROM products")
                T-Shorts = cursor.fetchall()
                conn.close()
             return render_template('catalog.html', T_Short=T_Short)
        elif request.form['Footwear']:
                conn = sqlite3.connect('database.db')
                cursor = conn.cursor()
                cursor.execute("SELECT Footwear FROM products")
                Footwear = cursor.fetchall()
                conn.close()
                return render_template('catalog.html', Footwear=Footwear)
        elif request.form['Coat']:
                conn = sqlite3.connect('database.db')
                cursor = conn.cursor()
                cursor.execute("SELECT Coat FROM products")
                Coat = cursor.fetchall()
                conn.close()
                return render_template('catalog.html', Coat=Coat)
        elif request.form['Shirt']:
                conn = sqlite3.connect('database.db')
                cursor = conn.cursor()
                cursor.execute("SELECT Shirts FROM products")
                Shirts = cursor.fetchall()
                conn.close()
                return render_template('catalog.html', Shirts=Shirts)



if __name__ == '__main__':
    app.run(debug=True)
