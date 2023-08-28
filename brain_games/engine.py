import prompt


POINTS = 3


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")
    return name


def congratulationts(name):
    print(f"Congratulations, {name}!")
    return name


def defeat(answer, correct_answer, name):
    print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}")
    print(f"Let's try again, {name}!")


def engine(game):
    name = welcome_user()
    print(game.DESCRIPTION)

    count = 0
    while count != POINTS:
        question, correct_answer = game.get_question_and_right_answer()
        print(f"Question: {question}")
        answer = input("Your answer: ")
        if answer == str(correct_answer):
            count += 1
            print("Correct!")
        else:
            defeat(answer, correct_answer, name)
            count = 0
            return

    congratulationts(name)
