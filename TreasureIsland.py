print("Welocome to Treasure Island.Your mission us to find the treasure.")
direction=input("Move left(L) or right(R)\n ")
if(direction.upper()=="R"):
    print("Game Over")
elif(direction.upper()=="L"):
    action=input("Action is Swim(S) or Wait(W)\n")
    if(action.upper()=="S"):
        print("Game over")
    elif(action.upper()=="W"):
        door=input("Which door ? Blue(B) or Red(R) or Yellow(Y)\n")
        if(door.upper()=="Y"):
            print("You Win")
        elif(door.upper()=="B" or "R"):
            print("Game Over")
        else:
             print("Invalid entry...Terminated")
    else:
        print("Invalid entry...Terminated")
else:
     print("Invalid entry...Terminated")