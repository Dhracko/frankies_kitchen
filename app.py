import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
