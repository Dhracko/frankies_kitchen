"""
Takes the Ingredients and the Method Steps and create a list
 to be added as a form of array
"""


def recipe_ingredients(rec):
    ingredient_list = []

    for key in rec.keys():
        if key == "ingredients":
            for value in rec.getlist(key):
                ingredient_list.append(value)

    return ingredient_list


def recipe_steps(rec):
    steps_list = []

    for key in rec.keys():
        if key == "step":
            for value in rec.getlist(key):
                steps_list.append(value)

    return steps_list
