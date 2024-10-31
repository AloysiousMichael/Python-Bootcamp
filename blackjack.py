import random
def blackjack():

    iscontinue=True
    user=[]
    system=[]
    while iscontinue:
        choices=input("If you want to continue type 'Y' or otherwise type'N'")
        yesorno=choices.upper()
        if yesorno=="Y":
            cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
            value=random.choice(cards)
            digit=random.choice(cards)
            system.append(digit)
            user.append(value)
            summ=sum(user)
            print(f"Your card : {user}   Current score : {summ}")
            systemsum=sum(system)
            print(f"Computers first hand  : {system[0]}")
            if systemsum >21:
                print(f"The Computers final hand is {system} and score is {systemsum}")
                print("You Loss")

        else:
            iscontinue = False
            if summ > systemsum and summ <=21:
                print(f"The Computers final hand is {system} and score is {systemsum}")
                print("You win")
            elif(systemsum==summ):
                print("Its a draw")
            else:
                print(f"The Computers final hand is {system} and score is {systemsum}")
                print("You loss")

blackjack()
