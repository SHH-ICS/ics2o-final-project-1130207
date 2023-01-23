# rock, paper, scissors game 
from random import randint

moves= ["rock", "paper", "scissors"]

while True:
  computer = moves[randint(0,2)]
  player = input("rock, paper or scissors? (orend the game)")
  if player == "end the game":
    print("the game has ended.")
    break
  elif player == "computer":
      print("end tie")
  elif player == "rock":
    if computer == "paper": 
      print("you lose", computer, "bests", player)
    else:
      print("you win", player, "bests", computer)
  elif player == "paper":
    if computer == "scissors":
      print("you lose", computer, "bests", player)
    else:
      print("you win", player, "bests", computer)
  elif player == "scissors":
    if computer == "rock":
      print("you lose", computer, "bests", player)
    else:
      print("you win", player, "bests", computer)
else:
    print("try agin")
