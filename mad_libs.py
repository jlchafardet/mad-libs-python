# Author: José Luis Chafardet G.
# Email: jose.chafardet@icloud.com
# Github: https://github.com/jlchafardet
#
# File Name: mad_libs.py
# Description: A Mad Libs game in Python.
# Created: Wednesday, October 2, 2024
# Last Modified: Thursday, October 3, 2024

# Mad Libs Game
#================

# Import the json module to handle JSON data
import json
import random

# Constant for placeholder
PLACEHOLDER = '___'

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
    # Try to open the file and load the JSON data
    try:
        with open(filename, 'r') as file:
            story_data = json.load(file)
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except json.JSONDecodeError:
        # Handle the case where the file is not a valid JSON file
        print(f"Error: The file '{filename}' is not a valid JSON file.")
        return None

    # Get the list of story themes
    story_themes = list(story_data['themes'].keys())

    # Ask the user to select a story theme
    print("Select a story theme:")
    for i, theme in enumerate(story_themes):
        print(f"{i + 1}. {theme}")

    while True:
        choice = input("Enter the number of your chosen theme: ")
        if choice.isdigit() and 1 <= int(choice) <= len(story_themes):
            theme = story_themes[int(choice) - 1]
            break
        else:
            print("Error: Invalid choice. Please try again.")

    # Get the list of stories for the selected theme
    stories = story_data['themes'][theme]['stories']

    # Ask the user to select a story
    print("Select a story:")
    for i, story in enumerate(stories):
        print(f"{i + 1}. {story['title']}")

    while True:
        choice = input("Enter the number of your chosen story: ")
        if choice.isdigit() and 1 <= int(choice) <= len(stories):
            story = stories[int(choice) - 1]
            break
        else:
            print("Error: Invalid choice. Please try again.")

    return story

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
    # Loop until the user enters a non-empty string
    while True:
        user_input = input(prompt)
        if user_input.strip() != "":
            return user_input
        else:
            # Handle the case where the user enters an empty string
            print("Error: Please enter a non-empty string.")

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
    # Check if the number of placeholders matches the number of user inputs
    if len(placeholders) != len(user_inputs):
        raise ValueError("Error: The number of placeholders does not match the number of user inputs.")
    
    index = 0
    for i, line in enumerate(story):
        # Loop until all placeholders have been replaced
        while PLACEHOLDER in line:
            replaced_text = user_inputs[index]
            line = line.replace(PLACEHOLDER, f'\033[92m{replaced_text}\033[0m', 1)
            index += 1
        story[i] = line
    return story

def print_story(story):
    """
    Prints the story to the console.

    Args:
        story (list): The story as a list of strings.
    """
    # Loop through the story and print each line
    for line in story:
        print(line)

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

    # Extract the story and placeholders from the story data
    story_lines = story_data['story']
    placeholders = story_data['placeholders']

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
    modified_story = replace_placeholders(story_lines, placeholders, user_inputs)

    # Print the modified story
    print_story(modified_story)

if __name__ == "__main__":
    main()