from flask import Flask, jsonify, request
import bs4, requests
from recipe_database import RecipeDatabase


app = Flask(__name__)

recipes = RecipeDatabase()
lasagna = {
  "_id": 1,
  "title": "The Best Homemade Lasagna",
  "summary": """
    Ingredients:
    - 2 teaspoons extra virgin olive oil
    - 1 pound ground beef chuck
    - 1/2 medium onion, diced
    - 1/2 large bell pepper (green, red, or yellow), diced
    - 2 cloves garlic, minced
    - 1 (28-ounce) can good-quality tomato sauce
    - 3 ounces tomato paste
    - 1 (14 ounce) can crushed tomatoes
    - 2 tablespoons chopped fresh oregano, or 2 teaspoons dried oregano
    - 1/4 cup chopped fresh parsley
    - 1 tablespoon Italian seasoning
    - 1 pinch garlic powder and/or garlic salt
    - 1 tablespoon red or white wine vinegar
    - 1 tablespoon to 1/4 cup sugar (to taste, optional)
    - Salt
    - 1/2 pound dry lasagna noodles (requires 9 lasagna noodles - unbroken)
    - 15 ounces ricotta cheese
    - 1 1/2 pounds (24 ounces) mozzarella cheese, grated or sliced
    - 1/4 pound (4 ounces) freshly grated Parmesan cheese

    Steps:
    1. Brown the ground beef in olive oil, then cook bell pepper, onions, and garlic.
    2. Make the sauce by adding crushed tomatoes, tomato sauce, tomato paste, herbs, and seasonings.
    3. Boil lasagna noodles until al dente, then drain and set aside.
    4. Preheat the oven to 375°F.
    5. Assemble the lasagna in layers: sauce, noodles, cheese. Repeat for three layers.
    6. Cover with foil and bake for 45 minutes at 375°F.
    7. Allow the lasagna to cool for at least 15 minutes before serving.

    Enjoy your homemade lasagna!
  """
}

@app.route("/RecipeList")
def RecipeList():
    recipes = RecipeDatabase()
    return recipes.recipeTitles()

@app.route("/submitURL", methods=['GET', 'POST'])
def submit_url():
    data = request.json
    recipe_url = data.get('recipeURL')
    response = requests.get(f'{recipe_url}', headers={'User-Agent': 'Mozilla/5.0'})
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    print(soup.body.get_text('', strip=True))

    response_data = {'message': 'Data received successfully'}
    return jsonify(response_data), 200    

@app.route("/retrieveRecipe", methods=['GET', 'POST'])
def retrieveRecipe():
    recipe_database = RecipeDatabase()
    data = request.json
    return recipe_database.findRecipe(data.get('recipeTitle'))


app.run(debug=True)

# print(recipes.recipeTitles())
# recipes.DeleteRecipe("The Best Homemade Lasagna")

# recipes.AddRecipe(lasagna)

# print(recipes.findRecipe("Keema"))