# This is my last assignment for CNE 330. It's Mad Lib.
# Author: Tim Nguyen
# Created on 10-15-24
# A Mad Lib is a fun, interactive word game where players fill in blanks with specific types of words
# (like nouns, verbs, adjectives, etc.) to create a humorous or surprising story.
# The structure of the story is pre-written, but key parts are left blank for the player to fill in
# without knowing the full context. Once all the blanks are filled, the story is revealed,
# often resulting in funny or unexpected outcomes.

# How it works:
# 1. The Setup: A short story is written with blanks where key words should be
#    (e.g., the name of a person, a place, or an action).
# 2. Prompting for Words: The player is asked to provide words to fill in the blanks without knowing the full story.
#    For example:
#       - "Give me a noun."
#       - "Give me an adjective."
#       - "Give me a verb."
# 3. Creating the Story: Once all the words are filled in, they are inserted into the story's template,
#    creating a unique and often humorous final story.

# Example:
# Story Template: One day, a {adjective} {noun} decided to {verb} to the {place}.
# User Input:
#     - Adjective: "happy"
#     - Noun: "dog"
#     - Verb: "run"
#     - Place: "park"
# Final Story: One day, a happy dog decided to run to the park.

# Assignment:
# Create a Python program that asks the user for various inputs and generates a fun Mad Lib story using
# input(), print(), and f-strings.

# Deliverables:
# 1. Pick a Mad Lib from https://www.thewordfinder.com/wordlibs/.
# 2. Use the input() function to gather words from the user in the console and save them to variables.
# 3. Create a template using your chosen Mad Lib and generate a fun story using f-strings to print the final result.

# Mad Lib Game - Interactive Story Generator

# Function to gather user inputs
def get_user_inputs():
    print("Let's write a story! Please provide the following words:")

    adjective1 = input("Please give me an adjective: ")
    noun1 = input("Please give me a noun: ")
    verb = input("Please give me a verb: ")
    place = input("Please give me a place: ")
    noun2 = input("Please give me another noun: ")
    adjective2 = input("One more adjective please: ")

    return adjective1, noun1, verb, place, noun2, adjective2


# Function to create the story using the user inputs
def create_story(adjective1, noun1, verb, place, noun2, adjective2):
    story = (
        f"Last year, a {adjective1} {noun1} decided to {verb} to the {place}. "
        f"On his journey, the {noun1} tripped over the {adjective2} {noun2} who was laying in the middle of the road. "
        f"They both had to go to the {place}."

    )
    return story
# Main function to run
def main():
    # Gather inputs from the user
    adjective1, noun1, verb, place, noun2, adjective2 = get_user_inputs()

    # Generate the story
    final_story = create_story(adjective1, noun1, verb, place, noun2, adjective2)

    # Display the final story
    print("\nHere is your story:\n")
    print(final_story)


# Start the program
if __name__ == "__main__":
    main()

