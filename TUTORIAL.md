# Mad Libs Game Script
=====================

## Overview
-----------

This script is a Mad Libs game that loads a story from a JSON file, replaces placeholders with user input, and prints the completed story.

## Functions
------------

### `load_story(filename)`

Loads a story from a JSON file.

*   **What does it do?** This function opens a file and reads its contents.
*   **What does it need?** It needs the path to the file, which is a string.
*   **What does it return?** It returns the contents of the file as a JSON object.

The function is defined as follows:
def load_story(filename):
    with open(filename, 'r') as file:
        return json.load(file)

### `get_user_input(prompt)`

Prompts the user to enter some text.

*   **What does it do?** This function asks the user to type something and waits for their response.
*   **What does it need?** It needs a prompt, which is a string that tells the user what to type.
*   **What does it return?** It returns the user's input as a string.

The function is defined as follows:
def get_user_input(prompt):
    return input(prompt)

### `replace_placeholders(story, placeholders, user_inputs)`

Replaces placeholders in the story with user input.

*   **What does it do?** This function replaces the placeholders in the story with the user's input.
*   **What does it need?** It needs the story, the placeholders, and the user's input.
*   **What does it return?** It returns the modified story with the placeholders replaced.

The function is defined as follows:
def replace_placeholders(story, placeholders, user_inputs):
    index = 0
    for line in story:
        if '___' in line :
            replaced_text = user_inputs[index]
            story[story.index(line)] = line.replace('___', f'\033[92m{replaced_text}\033[0m', 1)
            index += 1
    return story

### `print_story(story)`

Prints the completed story.

*   **What does it do?** This function prints the story to the console.
*   **What does it need?** It needs the story, which is a list of strings.
*   **What does it return?** It doesn't return anything, it just prints the story.

The function is defined as follows:
def print_story(story):
    for line in story:
        print(line)

## Main Function
----------------

The `main` function is the entry point of the script.

*   **What does it do?** This function loads the story data from the file, extracts the story and placeholders, replaces the placeholders, and prints the completed story.
*   **What does it need?** It doesn't need anything, it just runs the script.

The function is defined as follows:
def main():
    filename = 'assets/stories.json'
    story_data = load_story(filename)
    story = story_data['story']
    placeholders = story_data['placeholders']
    user_inputs = []
    for placeholder in placeholders:
        user_input = get_user_input(placeholder['prompt'])
        user_inputs.append(user_input)
    story = replace_placeholders(story, placeholders, user_inputs)
    print_story(story)

if __name__ == '__main__':
    main()