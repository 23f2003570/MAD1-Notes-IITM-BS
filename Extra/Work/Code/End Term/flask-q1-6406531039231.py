from flask import Flask

app = Flask(__name__)

movies = {
    "Spider man1": ["action", 5, "Sam Raimi"],
    "Batman": ["action", 3, "Matt Reeves"],
    "Joker": ["thriller", 4, "Todd Philips"],
    "Ted": ["comedy", 3, "Seth MacFarlane"]
}

def doSomething(g):
    l = []
    for key in movies:
        if movies[key][0] == g:
            l.append(key)
    return l

@app.route("/<genre>")
def home(genre):
    return doSomething(genre)


if __name__ == '__main__':
    app.run(debug=True)
    
    
'''
Q6406531039232:
    which of the following urls will display [Joker] on the browser ?
    1. http://127.0.0.1:5000/action
    2. http://127.0.0.1:5000/thriller
    3. http://127.0.0.1:5000/comedy
    4. http://127.0.0.1:5000?genre=thriller

curl http://127.0.0.1:5000/comedy [Ted]
curl http://127.0.0.1:5000/thriller [Joker]

6406531039233:
    What will be displayed by 
    
    curl http://127.0.0.1:5000?genre=action

    -> 404 NOTA
'''