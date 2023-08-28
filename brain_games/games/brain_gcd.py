from random import randint
from math import gcd


DESCRIPTION = "Find the greatest common divisor of given numbers."


def get_question_and_right_answer():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    correct_answer = gcd(first_number, second_number)
    question = f"{first_number} {second_number}"
    return question, correct_answer
