def format_recipe(raw_text):
    # Split the text into lines
    lines = raw_text.strip().split('\n')

    # Extract the title
    title = lines.pop(0).strip()

    # Extract the ingredients and instructions
    ingredients = []
    instructions = []
    current_list = None
    for line in lines:
        # Update the current list when a new category is encountered
        if 'Ingredients:' in line:
            current_list = ingredients
        elif 'Instructions:' in line:
            current_list = instructions
        # Add the current line to the current list
        elif current_list is not None:
            current_list.append(line.strip())

    # Format the ingredients and instructions
    formatted_ingredients = '\n'.join(f'- {ingredient}' for ingredient in ingredients)
    formatted_instructions = '\n'.join(f'{i + 1}. {instruction}' for i, instruction in enumerate(instructions))

    # Format the overall recipe
    formatted_recipe = f'*{title}*\n\n*Ingredients:*\n{formatted_ingredients}\n\n*Instructions:*\n{formatted_instructions}'

    return formatted_recipe