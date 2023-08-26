#!/usr/bin/env python3
from random import randint, choice


description = "What is the result of the expression?"


def game_data():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    operators = ["+", "-", "*"]
    operator = choice(operators)

    expression = f"{first_number} {operator} {second_number}"
    correct_answer = eval(expression)
    question = (f"{first_number} {operator} {second_number}")
    return question, correct_answer
