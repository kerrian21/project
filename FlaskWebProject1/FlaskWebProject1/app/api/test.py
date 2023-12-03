from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('identifier.sqlite', check_same_thread=False)
cursor = conn.cursor()

@app.route('/', methods=['POST', 'GET'])
def filter_price():
    if request.method == 'GET':
        name = request.args.get('name')

        if name:
            cursor.execute('SELECT title, price FROM products WHERE price = ?', (name,))
            exact_result = cursor.fetchall()

            if exact_result:
                message = f"Here is what was found for your query '{name}'."
                return render_template('results.html', message=message, results=exact_result)
            else:
                cursor.execute('SELECT title, price FROM products WHERE price LIKE ? COLLATE NOCASE ORDER BY price ASC', ('%' + name + '%',))
                similar_result = cursor.fetchall()

                if similar_result:
                    message = f"Unfortunately, no prices were found for your request '{name}', but similar ones were found."
                    return render_template('results.html', message=message, results=similar_result)
                else:
                    message = f"Sorry, nothing was found for your request '{name}'."
                    return render_template('results.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)








