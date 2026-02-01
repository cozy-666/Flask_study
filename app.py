from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

@app.route('/api/user/<name>')
def user(name):
    return {'name': name, 'message': f'Hello, {name}!'}

if __name__ == '__main__':
    app.run(debug=True)