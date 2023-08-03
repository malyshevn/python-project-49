#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
import prompt
from brain_games.dialog.defeat import defeat


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string("Your answer ")
        answer = answer.lower()
        if answer == "yes" and is_even(random_number):
            print("Correct")
            count += 1
        elif answer == "no" and not is_even(random_number):
            print("Correct!")
            count += 1
        else:
            defeat(answer, random_number, name)
            break

    if count == 3:
        print(f"Congratulations, {name}!")


def is_even(number):
    return number % 2


if __name__ == '__main__':
    main()
