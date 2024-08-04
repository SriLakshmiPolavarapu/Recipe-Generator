import requests

# Function to parse the ingredients entered by the user into a list


def parse_ingredients(ingredients):
    # Strip whitespace and ensure the list is non-empty
    return [ingredient.strip() for ingredient in ingredients.split(',') if ingredient.strip()]

# Function to fetch recipes using the Edamam Recipe Search API


def get_recipes(ingredients):
    url = "https://api.edamam.com/api/recipes/v2"

    app_id = '32b26e41'
    app_key = '181d8d5fdf017fae168d4aaa6d6df848'

    query = ','.join(ingredients)

    params = {
        'type': 'public',
        'q': query,
        'app_id': app_id,
        'app_key': app_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        recipes = []

        for hit in data.get('hits', []):
            recipe_info = hit.get('recipe', {})

            recipe = {
                'label': recipe_info.get('label', 'N/A'),
                'url': recipe_info.get('url', 'N/A'),
                'image': recipe_info.get('image', 'N/A'),
                'ingredients': recipe_info.get('ingredientLines', []),
                'calories': recipe_info.get('calories', 'N/A'),
                'totalTime': recipe_info.get('totalTime', 'N/A'),
            }

            recipes.append(recipe)

        return recipes
    else:
        print(f"Error fetching recipes: {response.status_code}")
        return []
