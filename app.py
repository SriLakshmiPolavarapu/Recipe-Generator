from flask import Flask, render_template, request
from ingredients import parse_ingredients, get_recipes

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get ingredients from the form
        ingredients = request.form['ingredients']
        ingredient_list = parse_ingredients(ingredients)

        # Fetch recipes using the Edamam Recipe Search API
        recipes = get_recipes(ingredient_list)

        return render_template('result.html', ingredients=ingredient_list, recipes=recipes)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
