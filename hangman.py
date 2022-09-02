import random
import re

input_letters_list = []
games_won = 0
games_lost = 0

def print_welcome_message(first_line):
    print(first_line)

def take_user_input():
    user_input = input("Input a letter:")
    processed_input = user_input

    return processed_input

def has_guessed_word(expected_word, input_word):
    return expected_word == input_word

def choose_random_word():
    word_list = ["python", "java", "swift", "javascript"];
    chosen_word = random.choice(word_list)

    return chosen_word

def hide_word(word):
    char_array = []
    for char in word:
        char_array.append("-")

    return "".join(char_array)

def reveal_characters(original_word, word_to_display, character_to_reveal):
    char_array = []
    for i in range(0, len(word_to_display)):
        if word_to_display[i] == "-":
            if character_to_reveal == original_word[i]:
                char_array.append(character_to_reveal)
            else:
                char_array.append(word_to_display[i])
        else:
            char_array.append(word_to_display[i])

    return "".join(char_array)

def contains_character(input_word, character):
    return character in input_word

def has_already_suggested_letter(character, input_letter_list):
    return len(input_letter_list) > 0 and character in input_letter_list

def check_user_input(input):
    maximum_size = 1

    if len(input) != maximum_size:
        print("Please, input a single letter")
        return -1

    has_special_chars = re.match(r"[^a-z]", input)

    if has_special_chars:
        print("Please, enter a lowercase letter from the English alphabet.")
        return -1

    return 0

def run_game(original_word):
    user_input = ""
    word_to_display = hide_word(original_word)
    attempts_left = 8
    global games_won
    global games_lost

    while attempts_left > 0:
        print()
        print(word_to_display)
        user_input = take_user_input()

        if check_user_input(user_input) == -1:
            continue

        if contains_character(original_word, user_input):
            if not contains_character(word_to_display, user_input):
                current_word = reveal_characters(original_word, word_to_display, user_input)
                word_to_display = current_word
            else:
                print("You've already guessed this letter.")
        elif has_already_suggested_letter(user_input, input_letters_list):
            print("You've already guessed this letter.")
        else:
            print("That letter doesn't appear in the word.")
            attempts_left -= 1;

        # Keeps track of the letters introduced by the user to check whether they repeat or not
        input_letters_list.append(user_input)

        if word_to_display == original_word:
            print(f"You guessed the word {original_word}!")
            print("You survived!")
            games_won += 1
            input_letters_list.clear()
            break;

    if attempts_left == 0:
        print()
        print("You lost!")
        games_lost += 1
        input_letters_list.clear()

def manage_game():
    print_welcome_message("H A N G M A N")
    while True:
        user_choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
        if user_choice == "play":
            word_to_guess = choose_random_word()
            run_game(word_to_guess)
        elif user_choice == "results":
            print(f"You won: {games_won} times")
            print(f"You lost: {games_lost} times")
            continue
        elif user_choice == "exit":
            break
        else:
            continue


def hangman_app():
    manage_game()

hangman_app()