#!/usr/bin/env python3
from random import randint


description = "What number is missing in the progression?!"


def game_data():
    length = randint(5, 10)
    d = randint(2, 5)
    progression_start = randint(5, 30)
    my_list = [progression_start]
    for i in range(length):
        progression_start += d
        my_list.append(progression_start)
    index = randint(1, length)
    correct_answer = my_list[index]
    my_list.insert(index, "..")
    my_list.pop(index + 1)
    question_string = " ".join(str(element) for element in my_list)
    question = question_string
    return question, correct_answer
