# Mad Libs Game
#================

import json

def load_story(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def get_user_input(prompt):
    return input(prompt)

def replace_placeholders(story, placeholders):
    for placeholder in placeholders:
        user_input = get_user_input(placeholder['prompt'])
        story[placeholder['line']] = story[placeholder['line']].replace('___', user_input)
    return story

def print_story(story):
    for line in story:
        print(line)

def main():
    filename = 'assets/stories.json'
    story_data = load_story(filename)
    story = story_data['story']
    placeholders = story_data['placeholders']
    story = replace_placeholders(story, placeholders)
    print_story(story)

if __name__ == '__main__':
    main()