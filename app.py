import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from lists import recipe_ingredients, recipe_steps
from os import path
if path.exists("env.py"):
    import env

MONGODB_URI = os.environ.get('MONGO_URI')

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'frankie_recipes'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


# Landing Main page

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template('initial.html',
                           recipes=mongo.db.recipes.find())


# Create recipe page

@app.route('/add_recipe')
def add_recipe():
    return render_template('create_recipe.html',
                           recipes=mongo.db.recipes.find())


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    rec = request.form

    name = rec["recipe_name"]
    description = rec["recipe_description"]
    prep_time = rec["preparation_time"]
    cook_time = rec["cooking_time"]
    skill = rec["skill"]
    portions = rec["portions"]

    """
    Below is the Ingredients and Steps which were
    predeterment in the function before
    """
    ingredient_list = recipe_ingredients(rec)
    steps_list = recipe_steps(rec)

    new_recipe = {
        "recipe_name": name,
        "recipe_description": description,
        "recipe_prep_time": int(prep_time),
        "recipe_cooking_time": int(cook_time),
        "recipe_skill": skill,
        "recipe_portions": int(portions),
        "recipe_steps": steps_list,
        "recipe_ingredients": ingredient_list,
    }

    recipe = mongo.db.recipes
    recipe.insert_one(new_recipe)
    return redirect(url_for('get_recipes'))


# Read Recipe Page

@app.route("/recipe/<recipe_id>/<recipe_name>")
def gt_recipe(recipe_id, recipe_name):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html", recipe=the_recipe)


# Update / Edit Recipe

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe=the_recipe)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipes
    rec = request.form

    name = rec["recipe_name"]
    description = rec["recipe_description"]
    prep_time = rec["preparation_time"]
    cook_time = rec["cooking_time"]
    skill = rec["skill"]
    portions = rec["portions"]

    """
    Below is the Ingredients and Steps which were
    predeterment in the file lists.py
    """
    ingredient_list = recipe_ingredients(rec)
    steps_list = recipe_steps(rec)

    recipe.update_one({'_id': ObjectId(recipe_id)},
                      {
        "$set": {
            "recipe_name": name,
            "recipe_description": description,
            "recipe_prep_time": int(prep_time),
            "recipe_cooking_time": int(cook_time),
            "recipe_skill": skill,
            "recipe_portions": int(portions),
            "recipe_steps": steps_list,
            "recipe_ingredients": ingredient_list
        }
    }
    )

    return redirect(url_for('get_recipes'))


# Delete Recipe
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


# Search Recipe by name form
@app.route('/search', methods=["POST"])
def get_search():
    return redirect(url_for('search_recipes',
                            search_term=request.form.get("search_field")))


# Search Results Page
@app.route('/search/<search_term>')
def search_recipes(search_term):

    recipe = mongo.db.recipes

    # Create a index for recipe name search.

    recipe.create_index([
        ("recipe_name", "text")])

    search_result = recipe.find({"$text": {"$search": search_term}})

    # Counts the number of recipes which match the search

    search_count = recipe.count_documents({"$text":
                                           {"$search": search_term}})

    return render_template("search.html", search_term=search_term,
                           search_result=search_result,
                           count=search_count)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
