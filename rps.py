import random
import sys
print("Let's Play : ROCK PAPER SCISSORS")
print("")
players_choice = input("Enter....\n1 for Rock\n2 for Paper\n3 for Scissors \n\n")
print("")
print("")
print("Your Choice : ", players_choice)

player = int(players_choice)

computers_choice = random.choice("123")
computer = int(computers_choice)
print("Computers Choice : ", computers_choice)

if player < 1 or player > 3:
    sys.exit("Your choice must be 1 , 2, or 3.")

if player == 1 and computer == 3:
    print(" 🎊 You WIN!")
elif player == 2 and computer == 1:
    print(" 🎊 You WIN!")
elif player == 3 and computer == 2:
    print(" 🎊 You WIN!")
elif player == computer:
    print(" 😮 TIE game !")
else:
    print(" 🫥 Computer WINS!!!")
