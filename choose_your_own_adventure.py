name = input("Enter your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You are on a dirt road, it has come to a end you can go left or right.Which way would you like to go?(left/right): ")

if "left" in answer.lower():
    answer = input("You come to a river and you can walk around it or swim across?(walk/swim): ")

    if "walk" in answer.lower():
        answer = input("You walked for miles and find a cabin. Do you knock or sneak in?(knock/sneak): ")

        if "knock" in answer.lower():
            print("An old lady invites you in, but it's a trap. She's a witch who turns you into a garden gnome.YOU LOSE!")
        elif "sneak" in answer.lower():
            print("You sneak in and find gold—but it's cursed. You're now allergic to air.YOU LOSE!")
        else:
            print("Invalid Answer!")

    elif "swim" in answer.lower():
        answer = input("Halfway through, something brushes your leg. Do you keep swimming or go back?(swim/go back): ")

        if "swim" in answer.lower():
            print("A river monster pulls you under. Your last thought: 'I should've walked…'YOU LOSE!")
        elif "back" in answer.lower():
            print("You make it to shore, but a wild raccoon steals your supplies and map. Lost forever in the wilderness.YOU LOSE!")
        else:
            print("Invalid Answer!")
    else:
        print("Invalid Answer!")
        
elif "right" in answer.lower():
    answer = input("You come acrross a bridge it looks wobbly, do you want to cross it or head back?(cross/back): ")

    if "cross" in answer.lower():
        answer = input("The bridge creaks but holds. On the other side, you see a shiny object in the bushes. Do you investigate or ignore it?(investigate/ignore): ")

        if "investigate" in answer.lower():
            print("It's a magical gem that teleports you to a hidden kingdom where you're crowned the Puzzle King/Queen. Snacks, sparkly robes, and eternal fame.YOU WIN!")
        elif "ignore" in answer.lower():
            print("You walk away, missing your chance. You live a quiet life… but always wonder what if.YOU LOSE!")
        else:
            print("Invalid Answer!")
    elif "back" in answer.lower():
        answer = input("As you turn back, you hear footsteps behind you. Do you run or hide?(run/hide): ")
        if "run" in answer.lower():
            print("You trip over your own feet and fall into a ditch. A goat mocks you. Repeatedly.YOU LOSE!")
        elif "hide" in answer.lower():
            print("You hide... forever. People think you became a tree. You didn’t, but still.YOU LOSE!")
        
    else:
        print("Invalid Answer!")

else:
    print("Invalid Answer!")
print(f"Thank you for playing {name}")