from pymongo import MongoClient
import json

class RecipeDatabase: 
    def __init__(self):
        self.client = MongoClient("localhost", 27017)
        self.database = self.client["recipes"]
        self.collection = self.database["recipes"]

    def BuildRecipe(self, recipe_draft):
        self.keema = {recipe_draft}

    def AddRecipe(self, recipe):
        self.collection.insert_one(recipe)
        print(recipe)

    def DeleteRecipe(self, recipe_title):
        self.collection.delete_one({"title":recipe_title})
        for document in self.collection.find():
            print(document)

    def findRecipe(self, recipe_title):
        recipe =  self.collection.find_one({"title": recipe_title})
        # for recipe in self.collection.find():         
        recipe["id"] = recipe["_id"]
        del recipe["_id"]
        return json.dumps(recipe)
        
    def recipeTitles(self):
        recipes = {}
        mongo_recipes = self.collection.find()
        for recipe in mongo_recipes:
            recipes[recipe['_id']] = recipe['title']  
        return json.dumps(recipes)
    

