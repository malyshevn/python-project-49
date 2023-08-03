#!/usr/bin/env python3
from brain_games.dialog.defeat import defeat
from brain_games.cli import welcome_user
from random import randint, choice
import prompt


def main():
    name = welcome_user()
    print("What number is missing in the progression?")
    count = 0
    while count != 3:
        right_answer = random()
        answer = prompt.integer("Your answer ")
        if answer == right_answer:
            print("Correct!")
            count += 1
        else:
            defeat(answer, right_answer, name)
            count = 0
            break
    if count == 3:
        print(f"Congratulations, {name}!")

def random():
    length = randint(5, 10)
    d = randint (2, 5)
    progression_start = randint(5, 30)
    my_list = [progression_start]
    for i in range(length):
        progression_start += d
        my_list.append(progression_start)
    index = randint(1, length)
    right_answer = my_list[index]
    my_list.insert(index, "..")
    my_list.pop(index + 1)
    question_string = " ".join(str(element) for element in my_list)
    print(f"Question: {question_string}")
    return right_answer


if __name__ == "__main__":
    main()