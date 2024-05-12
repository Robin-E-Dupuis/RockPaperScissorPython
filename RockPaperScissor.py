import random

PlayerScore = 0
CompScore = 0

def choice():
    choice = input("Rock, Papers or Scissors or q to quit: ").lower()
    return choice

def comp():
    gameList = ["Rock", "Papers", "Scissors"]
    comp = random.choice(gameList)
    return comp

def winner():
  global PlayerScore, CompScore
  while PlayerScore<3 or CompScore<3:
    player = choice()
    computer = comp()
    if player=="rock" and computer=="Scissors" or player=="paper" and computer=="Rock" or player=="scissors" and computer=="Papers":
       PlayerScore = PlayerScore+1
       print("The Player wins the round ! Score is : "+str(PlayerScore))
       print("The Computer loses the round... Score is : "+str(CompScore))
    elif player=="rock" and computer=="Papers" or player=="paper" and computer=="Scissors" or player=="scissors" and computer=="Rock":
       CompScore = CompScore +1
       print("The Computer wins the round ! Score is : "+str(CompScore))
       print("The Player loses the round... Score is : "+str(PlayerScore))
    else:
        print("No one wins this round. Draw.")

    if PlayerScore == 3 and PlayerScore > CompScore:
        print("The Player wins the game!")
        exit()
    elif CompScore == 3 and CompScore > PlayerScore:
        print("The computer wins the game")
        exit()

winner()
