#!/usr/bin/env python3
from brain_games.cli import welcome_user
from random import randint
import prompt


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count != 3:
        num = randint(1, 10)
        correct_answer = "yes" if is_prime(num) else "no"
        print(f"Question: {num}")
        answer = prompt.string("Your answer: ")
        if correct_answer == answer:
            count += 1
            print("Correct!")
        else:
            print(f"{answer} is wrong answer! ;(")
            count = 0
            break
    if count == 3:
        print(f"Congratulations, {name}!")


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    main()