# i already made this game before
#author: fenil
#snake, water and gun game
#i made a little bit of changes
 
import random

randomNum = random.randint(1, 3)
print(randomNum)

computerChoice = ""

if(randomNum == 1):
    computerChoice = "rock"
elif(randomNum == 2):
    computerChoice = "paper"
else:
    computerChoice = "scissors"

userChoice = ""
userWon = 0
computerWon = 0
quit = False
while not quit:
    choose = input("choose one:\nrock(r)\npaper(p)\nscissors(s)\nor Q to quit: ")
    if(choose.lower() == "r"):
        userChoice = "rock"
    elif(choose.lower() == "p"):
        userChoice = "paper"
    elif(choose.lower() == "s"):
        userChoice = "scissors" 
    elif (choose.lower() == "q"):
        print(f"You won {userWon} times")
        print(f"The Computer won {computerWon} times")
        quit = True
    else:
        print("that's not a valid option!")    

    gameWon = False


    if(computerChoice == "rock" and userChoice == "paper" or computerChoice == "paper" and userChoice == "scissors" or computerChoice == "scissors" and userChoice == "rock"):
        gameWon = True
        userWon += 1
    # elif(computerChoice == "snake" and userChoice == "gun"):
    #     gameWon = True
    # elif(computerChoice == "gun" and userChoice == "water"):
    #     gameWon = True
    elif(computerChoice == userChoice):
        gameWon = "tie"

    if not quit:
        print("You chose:", userChoice)
        print("The computer chose:", computerChoice)

        if(gameWon == "tie"):
            print("its a tie!")
        elif(not gameWon):
            print("You Lose!")
            computerWon += 1
        else:
            print("Congrats, You Win!")
