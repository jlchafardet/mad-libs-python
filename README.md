# Mad Libs Game
================

A word game where the user has to fill in the blanks with words to create a funny story.

## Description

This project aims to create a Mad Libs game in Python, following a structured workflow to ensure a well-documented and maintainable codebase.

## Features

### MVP Version

* Story Template: A pre-defined story template with blank spaces for words.
* Word Input: A user interface to input words (e.g., noun, verb, adjective, etc.) to fill in the blank spaces.
* Story Generation: A function to generate the completed story by replacing the blank spaces with the user-inputted words.
* Story Display: A way to display the generated story to the user.
* Validation and Error Handling: The code includes input validation and error handling to ensure the user enters words in the correct format and to handle any errors that may occur.

### Implemented Features

* Story Themes: The game now includes multiple story themes, allowing the user to choose from different story templates.
* Word Categories: The game now includes word categories (e.g., noun, verb, adjective, etc.) to guide the user's input.
* Input Validation: The game includes basic input validation to ensure the user enters words in the correct format.
* Enhanced Title Presentation: The title is displayed in a styled box with top, bottom, and side borders, printed in light blue color.
* Improved Theme Selection: The enumeration of story themes is printed in green, and the theme titles are printed in red, with a blank line added for separation.
* Output Formatting: A blank line is printed before the story output to separate it from the last prompt.

# Implementation Plan
======================

### Story Sharing

* Create a function to save the generated story to a .txt file
* Create a function to generate a text-based version of the story that can be copied and pasted
* Add a prompt at the end of the game, asking the player if they want to save their story to a .txt file

### Story Statistics

* Create a dictionary to store story generation statistics (e.g., number of stories generated, most popular story themes, etc.)
* Create a function to update the statistics dictionary each time a story is generated
* Create a function to write the statistics dictionary to a JSON file

### Word of the Day

* Create a function to generate a list of random words with their corresponding parts of speech (e.g., noun, verb, adjective, etc.)
* Add a command-line argument or special flag that, when passed to the game, triggers the word list generation
* Store the generated word list in a JSON file
* Create a function to select a random word from the list
* Display the selected word to the player at the start of the game

### To-Do

The following features are planned for incremental improvements:

#### Easiest (1-3 days of development)

* Word Suggestions: Provide word suggestions or hints to help users who are stuck.
* User Profiles: Implement user profiles to save and load previous stories.

#### Moderate (3-7 days of development)

* AI-powered Word Suggestions: Integrate AI-powered word suggestions based on the user's input and story context.
* Multi-player Mode: Develop a multi-player mode where users can play together, taking turns to input words.
* Story Analytics: Implement analytics to track user behavior, story popularity, and word usage.

#### Hardest (7+ days of development)

* Advanced Story Generation: Implement advanced story generation techniques, such as using machine learning algorithms to generate stories based on user input.
* Story Sharing: Allow users to share their generated stories on social media or via email.
* Story Customization: Allow users to customize the story template by adding or removing blank spaces.

## Getting Started

To run the game, simply execute the `mad_libs.py` file using Python.

## Contributing

To contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.