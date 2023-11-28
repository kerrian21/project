from flask import Flask, render_template, request, redirect
import sqlite3


app = Flask(__name__)


conn = sqlite3.connect('schema.sql')
cursor = conn.cursor()



def search_database(query):
    cursor.execute('''
        SELECT name, color, name_designer FROM T-Shorts, Footwear
        WHERE name LIKE ? OR color LIKE ? OR name_designer LIKE ?
    ''', ('%' + query + '%', '%' + query + '%', '%' + query + '%' ))
    results = cursor.fetchall()
    return results


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
   if request.methods == 'POST':
        query = request.form['query']
        results = search_database(query)
        return render_template('search_results.html', results=results)

@app.route('/catalog', methods=['POST','GET'])
def catalog():
        if request.methods == 'POST':
                category = request.form['Category']
                name = request.form['Name']
                years = request.form['Years']
                color = request.form['Color']
                prace = request.form['Prace']

                conn = sqlite3.connect('schema.sql')
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM products WHERE types = ? name = ? Color = ? Prace = ? Years = ?", (category, name, color, prace, years))
                result = cursor.fetchall() 
                conn.close()
                return render_template('t-short.html', result=result)
               
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
