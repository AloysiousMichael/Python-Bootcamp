import random
print("What do you choose?")
user=int(input("0 for rock or 1 for paper or  2 for scissor\n"))
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

system=random.randint(0,2)
print(system)

if(user==0 and system==1):
    print("You fail")
else:
    print("You win")
if(user==0 and system==2):
    print("You win")
else:
    print("You fail")
if(user==0 and system==0):
    print("Continue")
