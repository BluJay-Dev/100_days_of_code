from art import logo
import replit
from word_dict import words


def dict_extractor():
    a = words.get('a')
    b = words.get('b')
    return a, b


def game():
    score = 0
    should_play = True
    print(logo)
    while should_play:
        a, b = dict_extractor()
        print(f"Current score: {score}.")
        print(f'Compare A: {a.get("name")} a {a.get("job")} from {a.get("location")}')
        print('vs')
        print(f'Against B: {b.get("name")} a {b.get("job")} from {b.get("location")}')
        answer = input("Who has more followers? 'A' or 'B': ")
        if answer == 'A':
            if a.get('score') > b.get('score'):
                print('You Win good job!')
                score += 1
                should_play = True
                replit.clear()
            elif b.get('score') > a.get('score'):
                print('Better luck next time')
                should_play = False

        elif answer == 'B':
            if b.get('score') > a.get('score'):
                print('You win!')
                score += 1
                should_play = True
                replit.clear()
            elif a.get('score') > b.get('score'):
                print('Better luck next time')
                should_play = False


game()
