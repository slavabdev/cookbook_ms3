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

# Routes


# Home

@app.route('/')
@app.route('/home')
def home():
    '''
    Function renders home page
    '''
    pop_recipes = list(
        mongo.db.recipes.find().sort(
            [('count', -1)]).limit(3))
    return render_template('home.html', pop_recipes=pop_recipes)


# Register

@app.route('/register', methods=['GET', 'POST'])
def register():
    '''
    Function renders register page;
    add new user to the database;
    '''
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


# Login

@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Function renders login page;
    check if the user in database and flash the appropriate message
    redirect to login page if error occured
    '''
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

# Logout

@app.route('/logout')
def logout():
    '''
    Function pop the user from the session
    redirect to login page
    '''
    flash("You've been logged out")
    session.pop('user')
    return redirect(url_for('login'))

# Profile page

@app.route('/profile/<username>', methods=['GET','POST'])
def profile(username):
    '''
    function grab the session user's username from the db
    render profile page
    redirect to login page if session user is False
    '''
    username = mongo.db.users.find_one(
        {'username': session['user']})['username']
    user_recipes = list(
            mongo.db.recipes.find({"author": username}).sort([("_id", -1)]))
    if session['user']:
        return render_template('profile.html', 
        username=username, user_recipes=user_recipes)
    return redirect(url_for('login'))

# Recipes page

@app.route('/recipes')
def recipes():
    '''
    function render recipes page
    '''
    query = request.args.get('query')
    category = request.args.get('category')
    #check if search query
    if query:
        recipes = list(mongo.db.recipes.find(
            {"$text": {"$search": query}}))
        print(query)
    #check if filtered by category
    elif category:
        recipes = list(mongo.db.recipes.find({'category': category}))
    #check all recipes
    else:
        recipes = list(mongo.db.recipes.find())

    return render_template('recipes.html', recipes=recipes, category=category)

# Single recipe

@app.route('/recipe-page/<recipe_id>')
def recipe_page(recipe_id):
    '''
    This function renders the recipe-page
    It takes data grom db and put it on the page using recipe id
    '''
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    count = int(recipe['count'])
    mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)},
        {'$set': {'count': count +1 }})
    print(count)
    return render_template('recipe-page.html', recipe=recipe, recipe_id=recipe_id)


# Add recipe 

@app.route('/new-recipe', methods=['GET', 'POST'])
def new_recipe():
    '''
    This function renders the new recipe page
    It push the recipe data to db if session user is true
    otherwise it redirects user to register page and show an appropriate message
    and redirects to recipes page
    '''
    try:
        if session['user']:
             username = mongo.db.users.find_one(
                {"username": session["user"]})["username"]

    except KeyError:
        flash("Only registered users can add recipes.")
        return redirect(url_for("register"))

    finally:
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
            flash('Recipe successfully added!')
            return redirect(url_for("recipes"))
    return render_template('new-recipe.html', username=username)


# Edit recipe

@app.route('/edit-recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    '''
    This function renders the edit recipe page
    It updates the recipe data in db using recipe id and
    flash appropriate message, and redirects to profile page
    '''
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    username = mongo.db.users.find_one(
        {'username': session['user']})['username']
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
            return redirect(url_for('profile', username=username))
    return render_template('edit-recipe.html', recipe=recipe)


# Delete recipe

@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    '''
    fuction remove recipe with particular id from the db 
    and redirect to profile page
    '''
    username = mongo.db.users.find_one(
        {'username': session['user']})['username']
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})

    flash("Recipe Successfully Deleted")
    return redirect(url_for('profile', username=username))


#404 page 

@app.errorhandler(404)
def page_not_found(e):
    '''
    If a 404 error occured Page_not_found function will render the 404 page
    '''
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug = True)