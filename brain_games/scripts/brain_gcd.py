#!/usr/bin/env python3
from brain_games.dialog.defeat import defeat
from brain_games.cli import welcome_user
from random import randint
from math import gcd
import prompt


def main():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    count = 0
    while count != 3:
        correct_answer = gcd_fun()
        answer = prompt.integer("Your answer ")
        if answer == correct_answer:
            print("Correct!")
            count += 1
        else:
            defeat(answer, correct_answer, name)
            count = 0
            break
    if count == 3:
        print(f"Congratulations, {name}!")


def gcd_fun():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    right_answer = gcd(first_number, second_number)
    print(f"Question: {first_number} {second_number}")
    return right_answer


if __name__ == "__main__":
    main()
