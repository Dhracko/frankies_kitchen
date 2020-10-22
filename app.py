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


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template('recipes.html',
                           recipes=mongo.db.recipes.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_recipe', methods=['GET', 'POST'])
def insert_recipe():
    if request.method == 'POST':
        rec = request.form

        name = rec["recipe_name"]
        course = rec["course_name"]
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
            "recipe_course": course,
            "recipe_description": description,
            "recipe_prep_time": int(prep_time),
            "recipe_cooking_time": int(cook_time),
            "recipe_skill": skill,
            "recipe_portions": portions,
            "recipe_steps": steps_list,
            "recipe_ingredients": ingredient_list,
        }

    recipe = mongo.db.recipes
    recipe.insert_one(new_recipe)
    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
