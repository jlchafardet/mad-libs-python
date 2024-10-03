import random

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
    story = random.choice(story_data['stories'])

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