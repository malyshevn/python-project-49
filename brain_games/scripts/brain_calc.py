#!/usr/bin/env python3
from brain_games.cli import welcome_user
from random import randint, choice
import prompt


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("What is the result of the expression?")
    count = 0
    while count != 3:
        result = random_numbers()
        answer = prompt.integer("Your answer ")
        if answer == result:
            print("Correct!")
            count += 1
        else:
            print(f"{answer} is wrong answer! Let's try again, {name}")
            count = 0
            break
    if count == 3:
        print(f"Congratulations, {name}!")


def random_numbers():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    operators = ["+", "-", "*"]
    operator = choice(operators)

    expression = f"{first_number} {operator} {second_number}"
    result = eval(expression)
    print(f"Question: {first_number} {operator} {second_number}")
    return result


if __name__ == "__main__":
    main()