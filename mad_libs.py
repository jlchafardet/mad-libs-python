# Mad Libs Game
#================

import json

def load_story(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def get_user_input(prompt):
    return input(prompt)

def replace_placeholders(story, placeholders, user_inputs):
    # Modified to correctly replace placeholders with user input
    for i, placeholder in enumerate(placeholders):
        for j, line in enumerate(story):
            if '___' in line:
                story[j] = line.replace('___', user_inputs[i], 1)
                break
    return story

def print_story(story):
    for line in story:
        print(line)

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