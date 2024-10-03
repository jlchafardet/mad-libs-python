# Mad Libs Game
#================

# Import the json module to handle JSON data
import json
import random

# Define a function to load a story from a JSON file
def load_story(filename):
    """
    Loads a story from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        dict: The story data as a JSON object.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not a valid JSON file.
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file '{filename}' is not a valid JSON file.")
        return None

# Define a function to get user input
def get_user_input(prompt):
    """
    Prompts the user to enter some text.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        str: The user's input.

    Raises:
        ValueError: If the user enters an empty string.
    """
    while True:
        user_input = input(prompt)
        if user_input.strip() != "":
            return user_input
        else:
            print("Error: Please enter a non-empty string.")

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

    Raises:
        ValueError: If the number of placeholders does not match the number of user inputs.
    """
    if len(placeholders) != len(user_inputs):
        raise ValueError("Error: The number of placeholders does not match the number of user inputs.")
    index = 0
    for i, line in enumerate(story):
        while '___' in line:
            replaced_text = user_inputs[index]
            line = line.replace('___', f'\033[92m{replaced_text}\033[0m', 1)
            index += 1
        story[i] = line
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
    # Print the game title
    print("*************************************")
    print("*          Mad Libs Game          *")
    print("*************************************")
    print()
    print("Create a funny story by filling in the blanks!")
    print()

    # Define the filename of the JSON file
    filename = 'assets/stories.json'

    # Load the story data from the JSON file
    story_data = load_story(filename)
    if story_data is None:
        return

    # Pick a random story from the JSON file
    story_index = random.randint(0, len(story_data['stories']) - 1)
    story = story_data['stories'][story_index]

    # Extract the story and placeholders from the story data
    story_lines = story['story']
    placeholders = story['placeholders']

    # Initialize an empty list to store the user's input
    user_inputs = []

    # Loop through the placeholders and get the user's input
    for placeholder in placeholders:
        try:
            user_input = get_user_input(f"{placeholder['prompt']}: ")
            user_inputs.append(user_input)
        except ValueError as e:
            print(e)
            return

    # Replace the placeholders in the story with the user's input
    try:
        story_lines = replace_placeholders(story_lines, placeholders, user_inputs)
    except ValueError as e:
        print(e)
        return

    # Print the completed story
    print()
    print_story(story_lines)
    print()
    print("Hope you had fun!")

# Check if the script is being run directly
if __name__ == '__main__':
    # Run the main function
    main()