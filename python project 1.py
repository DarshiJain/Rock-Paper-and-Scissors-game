#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     24-04-2023
# Copyright:   (c) HP 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
user_choice = int(input("Enter your choice: type 0 for rock, 1 for paper and 2 for scissors"))
if user_choice >= 3 or user_choice < 0:
    print("You enterd invalid number , You Lose,")
else:
    computer_choice = random.randint(0,2)
    print("Computer chose:")
    print(computer_choice)
    if computer_choice== user_choice:
      print("It is a Draw.")
    elif computer_choice == 0 and user_choice ==2 :
      print("You Lose.")
    elif user_choice==0 and computer_choice==2 :
       print("You win.")
    elif computer_choice > user_choice:
        print("You lose.")
    elif user_choice > computer_choice:
        print("You Win.")
