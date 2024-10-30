from flask import Flask, request
import sys
app = Flask(__name__)

print (sys.argv)
@app.route('/home', methods = sys.argv)
def my_func():
    print (request.method)
    if request.method == 'GET':
        return f'Hello from {sys.argv[1]} method'
    elif request.method == 'POST':
        return f'Hello from {sys.argv[2]} method'
    elif request.method == '02.FLASK.PY':
        return f'{request.method} is a funny method'
    else:
        return "enter a valid method"
    
    
app.run(debug = True)