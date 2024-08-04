from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

# Function to generate a recipe using a pre-trained language model
def generate_recipe(ingredients):
    try:
        # Load pre-trained GPT-2 model and tokenizer
        model_name = 'gpt2'
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        recipe_generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

        # Create a refined prompt for the model to generate a recipe
        prompt = (f"Create a detailed recipe using the following ingredients: "
                  f"{', '.join(ingredients)}. The recipe should include preparation instructions, "
                  "cooking time, and any special tips or variations.")

        # Generate recipe text
        response = recipe_generator(prompt, max_length=300, num_return_sequences=1)
        return response[0]['generated_text']
    except Exception as e:
        print(f"Error generating recipe: {e}")
        return "An error occurred while generating the recipe."
