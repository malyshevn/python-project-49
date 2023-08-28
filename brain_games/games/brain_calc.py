from random import randint, choice


DESCRIPTION = "What is the result of the expression?"


def get_question_and_right_answer():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    operators = ["+", "-", "*"]
    operator = choice(operators)

    if operator == "+":
        correct_answer = first_number + second_number
    elif operator == "-":
        correct_answer = first_number - second_number
    elif operator == "*":
        correct_answer = first_number * second_number

    question = f"{first_number} {operator} {second_number}"
    return question, correct_answer
