import random
import sys


def play_rps():
    players_choice = input("\nEnter....\n1 for Rock\n2 for Paper\n3 for Scissors \n")

    print("\nYour Choice : ", players_choice)

    if players_choice not in ["1", "2", "3"]:
        print("Your choice must be 1 , 2, or 3.")
        return play_rps()

    player = int(players_choice)
    computers_choice = random.choice("123")
    computer = int(computers_choice)
    print("Computers Choice : ", computers_choice)

    if player == 1 and computer == 3:
        print("\n 🎊 You WIN!")
    elif player == 2 and computer == 1:
        print("\n 🎊 You WIN!")
    elif player == 3 and computer == 2:
        print("\n 🎊 You WIN!")
    elif player == computer:
        print("\n 😮 TIE game !")
    else:
        print("\n 🫥 Computer WINS!!!")

    print("\nWant To Play Again?")
    while True:
        play_again = input("Y for Yes \nQ for Quit\n")
        if play_again.lower() not in ["y", "q"]:
            continue
        else:
            break
    if play_again.lower() == "y":
        return play_rps()
    else:
        print("Thank you for playing!!!!")
        sys.exit("\n👋 .. BYE")


print("Let's Play : ROCK PAPER SCISSORS\n")
play_rps()