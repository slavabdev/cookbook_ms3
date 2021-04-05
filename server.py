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
    pop_recipes = list(
        mongo.db.recipes.find().sort([('count', -1)]).limit(3))
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


@app.route('/profile/<username>', methods=['GET','POST'])
def profile(username):
    # grab the session user's username from the db
    username = mongo.db.users.find_one(
        {'username': session['user']})['username']
    user_recipes = list(
            mongo.db.recipes.find().sort([("author", -1)]))
    if session['user']:
        return render_template('profile.html', username=username, user_recipes=user_recipes)
    return redirect(url_for('login'))



@app.route('/recipes')
def recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template('recipes.html', recipes=recipes)

@app.route('/recipe-page/<recipe_id>')
def recipe_page(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipe-page.html', recipe=recipe, recipe_id=recipe_id)

@app.route('/new-recipe', methods=['GET', 'POST'])
def new_recipe():
    if request.method == 'POST':
            recipe = {
                'category': request.form.get('category_name'),
                'recipe_title': request.form.get('recipe_title'),
                'cook_time': request.form.get('cook_time'),
                'description': request.form.get('description'),
                'ingredients': request.form.get('ingredients'),
                'method': request.form.get('method'),
                'image_url': request.form.get('image_url'),
                'count': 0,
                'author': session['user']
            }
            mongo.db.recipes.insert_one(recipe)
            flash('Your recipe successfully added!')
            return redirect(url_for("recipes"))
    return render_template('new-recipe.html')

@app.route('/edit-recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if request.method == 'POST':
            submit = {
                'category': request.form.get('category_name'),
                'recipe_title': request.form.get('recipe_title'),
                'cook_time': request.form.get('cook_time'),
                'description': request.form.get('description'),
                'ingredients': request.form.get('ingredients'),
                'method': request.form.get('method'),
                'image_url': request.form.get('image_url'),
                'count': 0,
                'author': session['user']
            }
            mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
            flash('Your recipe successfully updated!')
            return redirect(url_for('recipes'))
    return render_template('edit-recipe.html', recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    username = mongo.db.users.find_one(
        {'username': session['user']})['username']
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})

    flash("Recipe Successfully Deleted")
    return redirect(url_for('profile', username=username))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug = True)

