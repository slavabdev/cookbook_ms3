import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists('env.py'):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    pop_recipes = list(mongo.db.recipes.find().sort([('count', -1)]))
    return render_template('home.html', pop_recipes=pop_recipes)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # check if username already exists
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})

        if existing_user:
            flash('This username is already exists')
            return redirect(url_for('register'))

        register = {
            'username': request.form.get('username').lower(),
            'password': generate_password_hash(request.form.get('password'))
        }
        mongo.db.users.insert_one(register)

        # put the new user into session cookie
        session['user'] = request.form.get('username').lower()
        flash('Registration successful')
        return redirect(url_for('recipes', username=session['user']))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # check if user exists in db
        existing_user = mongo.db.users.find_one(
            {'username': request.form.get('username').lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user['password'], request.form.get('password')):
                session['user'] = request.form.get('username').lower()
                flash('Welcome, {}'.format(
                    request.form.get('username')))
                return redirect(
                    url_for('recipes', username=session['user']))

            else:
                # invalid password match
                flash('Username and/or password is incorrect')
                return redirect(url_for('login'))

        else:
            # username doesn't exists
            flash('Username and/or password is incorrect')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    flash("You've been logged out")
    session.pop('user')
    return redirect(url_for('login'))



@app.route('/recipes')
def recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template('recipes.html', recipes=recipes)

# 

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug = True)

