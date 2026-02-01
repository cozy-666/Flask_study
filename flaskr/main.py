from flaskr import app
from flask import render_template

@app.route('/')
def index():
    books = [
        {
        'title': 'はらぺこあおむし',
        'price': 1200,
        'arrival_day': '2026年2月1日'
        },
        {
        'title': 'グリとグラ',
        'price': 950,
        'arrival_day': '2026年2月2日'
        },       
    ]
    return render_template(
        'index.html',
        books=books
    )