#!/usr/bin/env python3
from brain_games.cli import welcome_user
from random import randint, choice
import prompt

text = "What is the result of the expression?"


def random_numbers():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    operators = ["+", "-", "*"]
    operator = choice(operators)

    expression = f"{first_number} {operator} {second_number}"
    correct_answer = eval(expression)
    question = (f"Question: {first_number} {operator} {second_number}")
    return correct_answer, question