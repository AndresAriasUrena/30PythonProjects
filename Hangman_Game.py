import random
import os


def clear():
    os.system("cls")

def print_hangman(values):
    print()
    print("\t +--------+")
    print("\t |       | |")
    print("\t {}       | |".format(values[0]))
    print("\t{}{}{}      | |".format(values[1], values[2], values[3]))
    print("\t {}       | |".format(values[4]))
    print("\t{} {}      | |".format(values[5], values[6]))
    print("\t         | |")
    print("  _______________|_|___")
    print("  `````````````````````")
    print()

def print_hangman_win():
    print()
    print("\t +--------+")
    print("\t         | |")

    print("\t         | |")
    print("\t O       | |")
    print("\t/|\\      | |")
    print("\t |       | |")
    print("  ______/_\\______|_|___")
    print("  `````````````````````")
    print()


def print_word(values):
    print()
    print("\t", end="")
    for x in values:
        print(x, end="")
    print()


def check_win(values):
    for char in values:
        if char == '_':
            return False
    return True

def hangman_game(word):
    clear()
    word_display = []
    correct_letters = []
    incorrect = []
    chances = 0
    hangman_values = ['O', '/', '|', '\\', '|', '/', '\\']
    show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    for char in word:
        if char.isalpha():
            word_display.append('_')
            correct_letters.append(char.upper())
        else:
            word_display.append(char)

    while True:
        print_hangman(show_hangman_values)
        print_word(word_display)
        print()
        print(f"Incorrect characters {str(len(incorrect))} : ", incorrect)
        print()

        inp = input("Enter a character = ")
        if len(inp) != 1:
            clear()
            print("Wrong choice!! Try Again")
            continue
        if not inp[0].isalpha():
            clear()
            print("Wrong choice!! Try Again")
            continue
        if inp.upper() in incorrect:
            clear()
            print("Already tried!!")
            continue
        if inp.upper() not in correct_letters:
            incorrect.append(inp.upper())
            show_hangman_values[chances] = hangman_values[chances]
            chances = chances + 1
            if chances == len(hangman_values):
                print()
                clear()
                print("\tGAME OVER!!!")
                print_hangman(hangman_values)
                print("The word was :", word.upper())
                break
        else:
            for i in range(len(word)):
                if word[i].upper() == inp.upper():
                    word_display[i] = inp.upper()
            if check_win(word_display):
                clear()
                print("\tCongratulations! ")
                print_hangman_win()
                print("The word was :", word.upper())
                break
        clear()


if __name__ == "__main__":
    clear()
    topics = {1: "DC characters", 2: "Marvel characters", 3: "Anime characters"}
    dataset = {
        "DC characters": ["SUPERMAN", "JOKER", "HARLEY QUINN", "GREEN LANTERN", "FLASH", "WONDER WOMAN", "AQUAMAN",
                          "MARTIAN MANHUNTER", "BATMAN"],
        "Marvel characters": ["CAPTAIN AMERICA", "IRON MAN", "THANOS", "HAWKEYE", "BLACK PANTHER", "BLACK WIDOW"],
        "Anime characters": ["UZUMAKI NARUTO", "ESCANOR", "LIGHT YAGAMI", "MIDORIYA IZUKU", "EREN JAEGER",
                             "KAMADO TANJIRO"]
    }

    while True:
        print()
        print("-----------------------------------------")
        print("\t\tGAME MENU")
        print("-----------------------------------------")
        for key in topics:
            print("Press", key, "to select", topics[key])
        print("Press", len(topics) + 1, "to quit")
        print()
        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            clear()
            print("Wrong choice!!! Try again")
            continue
        if choice > len(topics) + 1:
            clear()
            print("No such topic!!! Try again.")
            continue
        elif choice == len(topics) + 1:
            print()
            print("Thank you for playing!")
            break
        chosen_topic = topics[choice]
        ran = random.choice(dataset[chosen_topic])
        hangman_game(ran)
