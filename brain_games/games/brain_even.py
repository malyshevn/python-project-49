#!/usr/bin/env python3
from random import randint


description = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_data():
    random_number = randint(1, 100)
    question = random_number
    correct_answer = "yes" if question % 2 == 0 else "no"
    return question, correct_answer
