#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  playagain = "Y"

  while playagain == "Y":
    #Create a loop that continues as long as the user wants to play.
    #User can play as many games as they wish.
    computer = random.choice( ["R", "P", "S"] )
    player = input("Pick your weapon ( R, P, S): ")
    #Randomly choose the computer between 'R', 'P', or 'S'
    #Prompt the user for their RPS selection

    #Determine winner and state what happened to the user
    if computer == "R":
      print("Computer chose Rock")
    elif computer == "P":
      print("Computer chose Paper")
    elif computer == "S":
      print("Computer chose scissors")


    if player == "R":
      print("player chose Rock")
    elif player == "P":
      print("player chose Paper")
    elif player == "S":
      print("player chose scissors")

    if player == "R" and computer == "R" :
      print("Tie")
      ties = ties + 1
    if player == "R" and computer == "P" :
      print("Computer Wins")
      losses = losses + 1 
    if player == "R" and computer == "S":
      print("You win.")
      wins = wins + 1 
    if player == "P" and computer == "R":
      print("You win.")
      wins = wins + 1
    if player == "P" and computer == "P":
      print("Tie")
      ties = ties + 1
    if player == "P" and computer == "S":
      print("Computer Wins.")
      losses = losses + 1 
    if player == "S" and computer == "R":
      print("Computer Wins")
      losses = losses + 1 
    if player == "S" and computer == "P":
      print("You Win.")
      wins = wins + 1 
    if player == "S" and computer == "S":
      print ("Tie")
      ties = ties + 1 
    #Ask the user if they would like to play again.
    playagain = input("Play Again? (Y/N): ")
    #In the end, print the stats
    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(wins, "\t", ties , "\t", losses)
    
if __name__ == '__main__':
  main()
