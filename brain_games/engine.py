from cli import welcome_user
import prompt


def congratulationts(name):
    print(f"Congratulations, {name}!")
    return name


def defeat(answer, correct_answer, name):
    print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}")
    print(f"Let's try again, {name}!")


def engine(description, question_and_answer):
    name = welcome_user()
    print(description)

    count = 0
    while count != 3:
        question, correct_answer = question_and_answer
        print(question)
        answer = input("Your answer: ")

        if answer == correct_answer:
            count += 1
            print("Correct!")
        else:
            defeat(answer, correct_answer, name)
            count = 0
            break

    if count == 3:
        print(f"Congratulations, {name}!")
