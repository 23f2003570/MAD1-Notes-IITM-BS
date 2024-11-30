from flask import Flask, abort, request, url_for
import html

app = Flask(__name__)

@app.route('/home')
def home():
    return "/home"

@app.route('/home/')
def home2():
    return '/home/'
@app.errorhandler(404)
def f404(e):
    return "404 and not found"

@app.route('/validate/<int:number>')
def validate(number):
    if number % 2 == 0 and number % 3 == 1:
        abort(400, f'bad request number={number}')
    return f'<h1>Valid number {number}</h1>'

@app.route('/test')
def test():
    return url_for('home2')

@app.route('/mypathroute/<path:url_path>')
def mypathroute(url_path):   
    return 'The path is: ' +url_path

@app.route('/aboutpage')
def Homea():
    return 'This is my home page'

@app.route('/projectpage/')
def projects():
    return 'The project page'

@app.route('/aboutpage/projectpage//')
def result():
    return 'This is about the project page'

@app.route('/process')
def process():
    user_name = request.args.get('uname', 'MAD-1')
    if user_name.isnumeric():
        abort(400, f'Bad Request uname={user_name}')
    return f'<h1>Valid User Name {user_name}, Type: {html.escape(str(type(user_name)))}'


app.run()