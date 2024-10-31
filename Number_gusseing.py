import random
logo = r'''
  ________                                __  .__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/             \/     \/          \/            \/    \/     \/       
'''

print(logo)


def guessnum(level):
    for i in range(level,0,-1):
        print(f"You have {i} attempts remaining to guess the number")
        guess=int(input("Make a guess"))
        if guess > number:
            print("Too High >>>>")
        elif guess < number:
            print("Too Low  <<<<")
        else:
            print(f"You Got it! The answer is {number} ")
            return
    print("You have run out of guess You Loose")

print("Welcome to the number gusseing game")
print("I am thinking of a number between 1 and 100")
number=random.randint(1,100)
print(number)
level_choose=input("Choose a difficulty level :'easy' or 'hard' ")
level_choose.lower()
if level_choose=="easy":
    guessnum(10)
else:
    guessnum(5)
