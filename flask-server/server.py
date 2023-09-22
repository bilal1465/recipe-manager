from flask import Flask, jsonify, request
import bs4, requests
from recipe_database import RecipeDatabase


app = Flask(__name__)

recipes = RecipeDatabase()


x = {"_id": 1,
"title": "Keema",
"ingredients": ["1 pound ground mutton or lamb, chicken, or beef",
"3 tablespoons ghee or oil",
"1 ¼ cup yellow onion, finely diced",
"1 green chili pepper, finely diced",
"5 cloves garlic, minced",
"1 ½ teaspoons grated ginger",
"1 ½ cups tomato, finely chopped",
"½ cup green peas, frozen",
"2 tablespoons plain yogurt (full-fat)",
"¼ cup water",
"½ teaspoon garam masala",
"1 teaspoon lime or lemon juice",
"Cilantro for garnish",
],
"spices": ["1 teaspoon coriander powder (Dhaniya powder)",
"1 teaspoon Kashmiri red chili powder",
"½ teaspoon ground cumin (Jeera powder)",
"½ teaspoon ground turmeric (Haldi powder)",
"1 teaspoon salt (adjust to taste)",
],
"whole-Spices": ["1 stick cinnamon (Dalchini, about 1.5 inches)",
"1 teaspoon cumin seeds (Jeera)",
"½ teaspoon black peppercorns (optional)",
"1 bay leaf (Tej Patta)",
],
"instructions": ["Heat a medium-sized pan on medium-high heat and add ghee (or oil). Add all the whole spices (cinnamon, cumin seeds, black peppercorns, bay leaf) and sauté them for 30 seconds.",
"Add finely diced onions and green chili peppers, sauté for 4-5 minutes until they turn golden. Then add minced ginger and garlic, sauté for an additional 2 minutes until the raw smell is gone.",
"Add finely chopped tomatoes and all the spices (coriander powder, Kashmiri red chili powder, ground cumin, ground turmeric, salt). Sauté for 4-5 minutes until the liquid from the tomatoes dries up and the oil starts to separate.",
"Add the ground meat (mutton, lamb, chicken, or beef) and mix it well with the other ingredients to prevent lumps.",
"Cook the meat for 4-5 minutes until it changes color. Then reduce the heat, cover with a lid, and cook for another 4-5 minutes. Continue to cook uncovered until the meat is fully cooked, and fat starts to separate (approximately 10-12 minutes). Stir at regular intervals.",
"Add the frozen green peas, yogurt, and water. Stir and cook for an additional 3-4 minutes.",
"Finally, add garam masala and lime or lemon juice. Mix well.",
"Garnish the dish with cilantro.",
"Serve hot with naan, roti, paratha, or your preferred side dish.",
]
}

lasagna = {
    "_id" : 2,
    "title": "The Best Homemade Lasagna",
    "Description": "This classic lasagna recipe is made with an easy meat sauce as the base. Layer the sauce with noodles and cheese, then bake until bubbly! This is great for feeding a big family and freezes well, too.",
    "Ingredients": {
        "For the meat sauce": [
            "2 teaspoons extra virgin olive oil",
            "1 pound ground beef chuck",
            "1/2 medium onion, diced (about 3/4 cup)",
            "1/2 large bell pepper (green, red, or yellow), diced (about 3/4 cup)",
            "2 cloves garlic, minced",
            "1 (28-ounce)can good-quality tomato sauce",
            "3 ounces tomato paste (half a 6-ounce can)",
            "1 (14 ounce) can crushed tomatoes",
            "2 tablespoons chopped fresh oregano, or 2 teaspoons dried oregano",
            "1/4 cup chopped fresh parsley (preferably flat leaf), packed",
            "1 tablespoon Italian seasoning",
            "1 pinch garlic powder and/or garlic salt",
            "1 tablespoon red or white wine vinegar",
            "1 tablespoon to 1/4 cup sugar (to taste, optional)",
            "Salt"
        ],
        "To assemble the lasagna": [
            "1/2 pound dry lasagna noodles (requires 9 lasagna noodles - unbroken)",
            "15 ounces ricotta cheese",
            "1 1/2 pounds (24 ounces) mozzarella cheese, grated or sliced",
            "1/4 pound (4 ounces) freshly grated Parmesan cheese"
        ]
    },
    "Method": {
        "Put pasta water on to boil": [
            "Put a large pot of salted water (1 tablespoon of salt for every 2 quarts of water) on the stovetop on high heat. It can take a while for a large pot of water to come to a boil, so prepare the sauce in the next steps while the water is heating."
        ],
        "Brown the ground beef": [
            "In a large skillet heat 2 teaspoons of olive oil on medium-high heat.",
            "Add the ground beef and cook until it is lightly browned on all sides.",
            "Remove the beef with a slotted spoon to a bowl. Drain off all but a tablespoon of fat."
        ],
        "Cook the bell pepper, onions, and garlic; add back the beef": [
            "Add the diced bell pepper and onions to the skillet.",
            "Cook for 4 to 5 minutes, until the onions are translucent and the peppers softened.",
            "Add the minced garlic and cook half a minute more.",
            "Return the browned ground beef to the pan.",
            "Stir to combine, reduce the heat to low, and cook for another 5 minutes."
        ],
        "Make the sauce": [
            "Transfer the beef mixture to a medium-sized (3- to 4-quart) pot.",
            "Add the crushed tomatoes, tomato sauce, and tomato paste to the pot.",
            "Add the parsley, oregano, and Italian seasonings, adjusting the amounts to taste.",
            "Sprinkle with garlic powder and/or garlic salt, to taste.",
            "Sprinkle with red or white wine vinegar. Stir in sugar, a tablespoon at a time, tasting after each addition, to taste. (The amount of sugar needed will vary, depending on how acidic the tomatoes are that you are using.)",
            "Add salt to taste, and note that you will later be adding Parmesan, which is salty.",
            "Bring the sauce to a simmer and then lower the heat to maintain a low simmer. Cook for 15 to 45 minutes, stirring often. Scrape the bottom of the pot every so often so nothing sticks to the bottom and scorches. Remove from heat."
        ],
        "Boil and drain the lasagna noodles": [
            "By now the salted water you started heating in step one should be boiling.",
            "Add the dry lasagna noodles and cook them to al dente, per package directions. (Note noodles may be cooked in advance.)",
            "Stir often to prevent from sticking. Make sure that water remains at a full rolling boil during the entire cooking to prevent noodles from sticking.",
            "When ready, drain in a colander and rinse with cool water, gently separating any noodles that may be sticking together.",
            "Spread a little olive oil on a large rimmed baking sheet, and lay out the cooked noodles on this sheet, turning them over so that they get coated with a little of the olive oil. This will prevent them from sticking together."
        ],
        "Preheat the oven to 375°F.": [],
        "Assemble the lasagna": [
            "In a 9x13-inch casserole or lasagna dish, ladle a cup of sauce and spread it over the bottom of the dish.",
            "Arrange one layer of lasagna noodles lengthwise (about 3 long noodles, the edges may overlap, depending on your pan) over the sauce.",
            "Ladle a third of the remaining sauce over the noodles.",
            "Sprinkle a layer of a third of the grated mozzarella on top of the lasagna sauce.",
            "Add half of the ricotta cheese, by placing cheese dollops every couple of inches.",
            "Sprinkle half the grated parmesan cheese evenly over the top of the ricotta cheese.",
            "Apply the second layer of noodles and top it with half of the remaining sauce.",
            "Add half of the remaining mozzarella, the remaining ricotta cheese, and another the remaining Parmesan.",
            "Finish with another layer of noodles. Spread the remaining sauce over the top layer of noodles and sprinkle with the remaining mozzarella cheese."
        ],
        "Bake": [
            "Cover the lasagna pan with aluminum foil, tented slightly so it doesn't touch the noodles or sauce).",
            "Bake at 375°F for 45 minutes. Uncover in the last 10 minutes if you'd like more of a crusty top or edges."
        ],
        "Cool and serve": [
            "Allow the lasagna to cool for at least 15 before serving.",
            "Leftovers will keep for about 5 days. You can reheat it in a conventional oven or microwave.",
            "Leave the aluminum tent on for storage. (Try to keep the aluminum foil from touching the sauce.)"
        ]
    }
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



app.run(debug=True)
# print(recipes.recipeTitles())
# recipes.DeleteRecipe("The Best Homemade Lasagna")

# recipes.AddRecipe(lasagna)