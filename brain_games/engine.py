from brain_games.utils import defeat, congratulationts, welcome_user


def engine(game=None):
    name = welcome_user()
    if game is None:
        return
    print(game.description)

    count = 0
    while count != 3:
        question, correct_answer = game.game_data()
        print(f"Question: {question}")
        answer = input("Your answer: ")
        if answer == str(correct_answer):
            count += 1
            print("Correct!")
        else:
            defeat(answer, correct_answer, name)
            count = 0
            break
        if count == 3:
            congratulationts(name)
