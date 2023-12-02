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
    return render_template('index.html', template2='search.html')

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
        query = request.form['query']
        cursor.execute('SELECT title, price FROM products WHERE title = ?', [query])
        results = cursor.fetchall()
        print(results)
        return render_template('search_results.html', results=results)

@app.route('/catalog', methods=['POST','GET'])
def catalog():
        if request.method == 'POST':
            name = request.form['clothes']
            if name == 'Shirt':
                cursor.execute("SELECT title, price FROM products WHERE title = 'Moody Shirt'")
                result = cursor.fetchall()
                return render_template('shirt.html', result=result)

            elif name == 't-shirt':
                    cursor.execute("SELECT title, price FROM products WHERE title = 'T-Shirt lalala'")
                    result = cursor.fetchall()
                    return render_template('t-shirt.html', result=result)
            elif name == 'Jacket':
                    cursor.execute("SELECT title, price FROM products WHERE title IN ('Example Jacket', 'Jack')")
                    result = cursor.fetchall()
                    return render_template('jacket.html', result=result)
            elif name == 'pants':
                    cursor.execute("SELECT title, price FROM products WHERE title IN ('White pants', 'Black pants')")
                    result = cursor.fetchall()
                    return render_template('pants.html', result=result)
            elif name == 'Footwear':
                    cursor.execute("SELECT title, price FROM products WHERE title = 'FootweaRR'")
                    result = cursor.fetchall()
                    return render_template('footwear.html', result=result)



               
@app.route('/range', methods=['POST','GET'])
def _range_():
        if request.methods == 'POST':
            category = request.foorm['Category']
            name = request.form['Name products']
            color = requst.form['Color']
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
                    return 'Udated'
            else:
                    return 'Not found'
 


if __name__ == '__main__':
    app.run(debug=True)
