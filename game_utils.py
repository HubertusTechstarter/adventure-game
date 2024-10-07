def solve_riddle(riddle, answer):
    print(riddle['question'])
    user_answer = input("Deine Antwort: ").strip().lower()
    if user_answer == answer.lower():
        print("Richtig!")
        return True
    else:
        print("Falsch!")
        return False

def end_game():
    print("Danke fürs Spielen! Auf Wiedersehen.")
    exit()
