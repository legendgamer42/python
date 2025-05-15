#this project i already made it
# author fenil bhimajiyani
import random

def Game():
  randomNum = random.randint(1,100)
  userNum = int(input("Guess a number from 1 to 100: "))
  guess = 1
  while(randomNum != userNum):
    guess += 1
    if randomNum > userNum:
      userNum = int(input("Higher Number Please: "))
    
    elif userNum > randomNum:
      userNum = int(input("Lower Number Please: "))
      
  print("Congratulations! You won the game.") 
  print(f"You have guessed the correct number in {guess} guesses.")
  onceMore = input("Do you want to play this game again(Yes/No): ")
  onceMore = onceMore.lower()
  if onceMore == "yes":
    Game()
  else:
    print("Thank you for playing.")
        
Game() 


