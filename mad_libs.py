# Mad Libs Game
#================

# Import the json module to handle JSON data
import json

# Define a function to load a story from a JSON file
def load_story(filename):
    """
    Loads a story from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        dict: The story data as a JSON object.
    """
    with open(filename, 'r') as file:
        return json.load(file)

# Define a function to get user input
def get_user_input(prompt):
    """
    Prompts the user to enter some text.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        str: The user's input.
    """
    return input(prompt)

# Define a function to replace placeholders in the story with user input
def replace_placeholders(story, placeholders, user_inputs):
    """
    Replaces placeholders in the story with user input.

    Args:
        story (list): The story as a list of strings.
        placeholders (list): The placeholders as a list of dictionaries.
        user_inputs (list): The user's input as a list of strings.

    Returns:
        list: The modified story with placeholders replaced.
    """
    index = 0
    for line in story:
        if '___' in line:
            replaced_text = user_inputs[index]
            story[story.index(line)] = line.replace('___', f'\033[92m{replaced_text}\033[0m', 1)
            index += 1
    return story

# Define a function to print the story
def print_story(story):
    """
    Prints the story to the console.

    Args:
        story (list): The story as a list of strings.
    """
    for line in story:
        print(line)

# Define the main function
def main():
    """
    The main function that runs the Mad Libs game.
    """
    # Define the filename of the JSON file
    filename = 'assets/stories.json'

    # Load the story data from the JSON file
    story_data = load_story(filename)

    # Extract the story and placeholders from the story data
    story = story_data['story']
    placeholders = story_data['placeholders']

    # Initialize an empty list to store the user's input
    user_inputs = []

    # Loop through the placeholders and get the user's input
    for placeholder in placeholders:
        user_input = get_user_input(placeholder['prompt'])
        user_inputs.append(user_input)

    # Replace the placeholders in the story with the user's input
    story = replace_placeholders(story, placeholders, user_inputs)

    # Print the completed story
    print_story(story)

# Check if the script is being run directly
if __name__ == '__main__':
    # Run the main function
    main()