# Mad Libs Game Script
=====================

## Overview
-----------

This script is a Mad Libs game that loads a story from a JSON file, replaces placeholders with user input, and prints the completed story.

## Functions
------------

### `load_story(filename)`
------------------------

Loads a story from a JSON file.

*   **Parameters:** `filename` (str) - the path to the JSON file
*   **Returns:** the story data as a JSON object

def load_story(filename):
    with open(filename, 'r') as file:
        return json.load(file)

### `get_user_input(prompt)`
-------------------------

Prompts the user to enter some text.

*   **Parameters:** `prompt` (str) - the prompt to display to the user
*   **Returns:** the user's input as a string

def get_user_input(prompt):
    return input(prompt)

### `replace_placeholders(story, placeholders)`
--------------------------------------

Replaces placeholders in the story with user input.

*   **Parameters:**
    *   `story` (list) - the story as a list of strings
    *   `placeholders` (list) - the placeholders as a list of dictionaries
*   **Returns:** the modified story with placeholders replaced

def replace_placeholders(story, placeholders):
    for placeholder in placeholders:
        user_input = get_user_input(placeholder['prompt'])
        story[placeholder['line']] = story[placeholder['line']].replace('___', user_input)
    return story

### `print_story(story)`
----------------------

Prints the completed story.

*   **Parameters:** `story` (list) - the story as a list of strings

def print_story(story):
    for line in story:
        print(line)

## Main Function
----------------

The `main` function is the entry point of the script.

*   **Loads the story data from the file**
*   **Extracts the story and placeholders from the story data**
*   **Replaces the placeholders in the story**
*   **Prints the completed story**

def main():
    filename = 'assets/stories.json'
    story_data = load_story(filename)
    story = story_data['story']
    placeholders = story_data['placeholders']
    story = replace_placeholders(story, placeholders)
    print_story(story)

if __name__ == '__main__':
    main()