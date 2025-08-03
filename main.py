import hangman
from scores import ScoreTracker
import os


# Check if the leaderboard file exists. 
if not os.path.exists("leaderboard.txt"):
    with open("leaderboard.txt", "w") as file:
        file.write("{:<15}{:^10}{:^20}\n".format("Username", "Streak", "Accumulated Score"))

def username_exists(username):
    try:
        with open("leaderboard.txt", "r") as file:
            for line in file:
                existing_username = line[:15].strip()
                if existing_username == username:
                    return True
    except FileNotFoundError:
        pass 
    return False

while True:

    username = str(input("Please enter your username : ")).strip()
    if username_exists(username):
        print("That username already exists. Please choose a different one.")
    else:
        break

score = ScoreTracker(username)

print("Welcome to Hangman!\n")

hangman.hangman(score)

while True:

    play_again = input("\nDo you want to play again? (Y/N): ").strip().lower()
    
    if play_again in ('y', 'n'):
        if play_again == 'y':
            hangman.hangman(score)
        else:
            print("Thanks for playing!")
            score.leaderboard()
            break

    else:
        print("Please enter 'Y' or 'N'.")