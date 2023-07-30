#!/usr/bin/env python3
from random import randint
import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string("Your answer ")
        answer = answer.lower()
        if answer == "yes" and random_number%2 == 0:
            print("Correct")
            count += 1
        elif answer == "yes" and random_number%2 != 0:
            print(f"{answer} is a wrong answer!")
            count = 0
            break
        elif answer == "no" and random_number%2 != 0:
            print("Correct!")
            count += 1
        elif answer == "no" and random_number%2 == 0:
            print(f"{answer} is a wrong answer!")
            count = 0
            break
        else:
            print(f"{answer} is a wrong answer! Try again")
            break

    if count == 3:
        print(f"Congratulations, {name}")

if __name__ == '__main__':
    main()
