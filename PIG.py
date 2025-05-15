import random

def roll():
    num = random.randint(1,6)
    return num

player_names = []

while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            for i in range(1,players + 1):
                player = input(f"Player {i}: ")
                player_names.append(player)
            break   
        else:
            print("Must be between 2-4 players")
    else:
        print("Invalid,try again")

max_score = 50
player_scores = [0 for i in range(players)]

while max(player_scores) < max_score:
    for i,player in enumerate(player_names):    
        current_score = 0
        print(f"{player}'s turn has just started")
        while True:
            should_roll = input(f"{player}, Would you like to roll?(y/n): ")
            if should_roll.lower() != "y":
                print(f"{player} ended the turn with {current_score} points.")
                break
            value = roll()
            print(f"{player} rolled a: {value}")

            if value == 1:
                print(f"{player} rolled a 1. Turn done!")
                current_score = 0
                break
            else:
                current_score += value
            print(f"{player}'s score is: {current_score}")
            if current_score + player_scores[i] >= max_score:
                break
        player_scores[i] += current_score
        print(f"{player}'s total score is {player_scores[i]}")

        if player_scores[i] >= max_score:
            print(f"\n🎉 {player} wins the game with {player_scores[i]} points! 🎉")
            
            break

print("\nFinal Scores:")
for name, score in zip(player_names, player_scores):
    print(f"{name}: {score}")