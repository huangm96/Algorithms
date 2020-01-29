#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = math.inf
  # loop items in recipe

  for item in recipe:
    # if the item is not in ingredients, return 0
    if not item in ingredients:
      return 0
    # if the item is in ingredients, compare them, return get the smallest batches num
    else:
      batch_num = ingredients[item] // recipe[item]
      if batch_num < batches:
        batches = batch_num
  return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
