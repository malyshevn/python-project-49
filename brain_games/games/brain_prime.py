#!/usr/bin/env python3
from random import randint


description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_data():
    num = randint(1, 100)
    correct_answer = "yes" if is_prime(num) else "no"
    question = num
    return question, correct_answer


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
