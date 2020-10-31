"""Module for receipe app"""
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from lists import recipe_ingredients, recipe_steps


if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get('MONGO_URI')

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'frankie_recipes'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    """Gets the recipe in Mongodb.
    Args:
        recipes: Find the recipes
    Returns:
        Rendered initial.html containing the recipes
    """
    return render_template('initial.html',
                           recipes=mongo.db.recipes.find())


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    """
    Create a new recipe in Mongodb.

    By defining the different fields of input
    using the request.form methods and then
    creating an array in JSON to be inserted in Mongodb.

    Args:
        recipe_ingredients: Recall the list of ingredients.
        recipe_steps: Recall the list pf steps.
        new_recipe: Create a JSON style data.
    Returns:
        recipe.insert_one(new_recipe): Insert the recipe with the data.
    """
    if request.method == "POST":

        req = request.form

        name = request.form.get("recipe_name")
        image = request.form.get("recipe_image")
        description = request.form.get("recipe_description")
        prep_time = request.form.get("preparation_time")
        cook_time = request.form.get("cooking_time")
        skill = request.form.get("skill")
        portions = request.form.get("portions")

        ingredient_list = recipe_ingredients(req)
        steps_list = recipe_steps(req)

        if image == "":
            image = "../static/images/generic_logo.png'"

        new_recipe = {
            "recipe_name": name,
            "recipe_image": image,
            "recipe_description": description,
            "recipe_prep_time": int(prep_time),
            "recipe_cooking_time": int(cook_time),
            "recipe_skill": skill,
            "recipe_portions": int(portions),
            "recipe_steps": steps_list,
            "recipe_ingredients": ingredient_list,
        }

        mongo.db.recipes.insert_one(new_recipe)
        return redirect(url_for('get_recipes'))
    return render_template('create_recipe.html')


@app.route("/recipe/<recipe_id>")
def get_recipe(recipe_id):
    """Display the recipe selected.
    Args:
        recipe_id: Finds a recipe with the specific id.
    Returns:
        Rendered recipe.html containing the recipes.
    """
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html", recipe=the_recipe)


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    """Gets the recipe by id to be edited.
    Args:
        recipe_id: Unique ID of the given recipe.
        the_recipe: Finds the recipe with the recipe_id.
    Returns:
        Rendered edit_recipe.html containing the recipe.
    """
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe=the_recipe)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    """
    Edit and Update a recipe in Mongodb.

    By defining the different fields of input
    using the request.form methods and then
    creating an array in JSON to be inserted in Mongodb.

    Args:
        recipe_ingredients: Recall the list of ingredients.
        recipe_steps: Recall the list pf steps.
        recipe_id: Specify a recipe using the unique id.
    Returns:
        recipe.update_one({'_id': ObjectId(recipe_id)},{"$set"):
        Update the recipe with $set data.
    """
    recipe = mongo.db.recipes
    req = request.form

    name = req["recipe_name"]
    image = req["recipe_image"]
    description = req["recipe_description"]
    prep_time = req["preparation_time"]
    cook_time = req["cooking_time"]
    skill = req["skill"]
    portions = req["portions"]

    ingredient_list = recipe_ingredients(req)
    steps_list = recipe_steps(req)

    recipe.update_one({'_id': ObjectId(recipe_id)},
                      {
        "$set": {
            "recipe_name": name,
            "recipe_image": image,
            "recipe_description": description,
            "recipe_prep_time": int(prep_time),
            "recipe_cooking_time": int(cook_time),
            "recipe_skill": skill,
            "recipe_portions": int(portions),
            "recipe_steps": steps_list,
            "recipe_ingredients": ingredient_list
        }
    })

    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    """Delete a recipe
    Arg:
        recipe_id: Unique ID of a recipe.
    Returns:
        Removes the recipe with the unique ID.
    """
    mongo.db.recipes.delete_one({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


@app.route('/search', methods=["POST"])
def get_search():
    """Defines the funtion get_search.
    Arg:
        search_field: Input the searching text.
    Returns:
        search_term: The values for the search.
    """
    return redirect(url_for('search_recipes',
                            search_term=request.form.get("search_field")))


@app.route('/search/<search_term>')
def search_recipes(search_term):
    """Searches recipe by name
    Args:
        search_term: Search text to match recipes
    Returns:
        Rendered search.html containing recipes matching search_term
    """
    recipe = mongo.db.recipes

    recipe.create_index([
        ("recipe_name", "text")])

    search_result = recipe.find({"$text": {"$search": search_term}})

    # Counts the number of recipes which match the search

    search_count = recipe.count_documents({"$text":
                                           {"$search": search_term}})

    return render_template("search.html", search_term=search_term,
                           search_result=search_result,
                           count=search_count)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def handle_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
