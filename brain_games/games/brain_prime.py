from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_right_answer():
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
