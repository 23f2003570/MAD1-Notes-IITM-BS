from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from models import db,User, Role, Association

app = Flask(__name__)
app.config['SQLALCHEMY DATABASE URI'] = 'sqlite:///database.sqlite3'

db.init(app)

app.app_context().push()

@app.route('/')
def all_roles():
    roles = Role.query().all()
    print(roles)
    return render_template('index.html', roles=roles)

@app.route('/create_role', methods=['GET', 'POST'])
def create_role():
    if request.method == 'POST':
        role = request.form.get('role')
        new_role = Role(role_name = role)
        db.session.add(new_role)
        db.session.commit()
    return render_template('create_role.html')

if __name__ == '__main__':
    app.run(debug=True)