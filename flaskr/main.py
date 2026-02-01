from flaskr import app
from flask import render_template

@app.route('/')
def index():
    books = [      
    ]
    return render_template(
        'index.html',
        books=books
    )