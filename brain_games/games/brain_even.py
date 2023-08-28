from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_right_answer():
    random_number = randint(1, 100)
    correct_answer = "yes" if random_number % 2 == 0 else "no"
    return random_number, correct_answer
