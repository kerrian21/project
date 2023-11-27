from flask import Flask, render_template

app = Flask(__name__)

def sort_clothing_by_rating(clothing):
    return sorted(clothing, key=lambda x: x['rating'], reverse=True)

clothing = [
        {'name': 'T-Short', 'rating': 4.5},
        {'name': 'Footwear', 'rating': 3.9},
        {'name': 'Coat', 'rating': 4.2},
        {'name': 'Shirt', 'rating': 4.9},
]

sorted_clothing = sort_clothing_by_rating(clothing)

if __name__ == '__main__':
    app.run(debug=True)
