import random

stages = ["""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
""" ,
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
"""]


logo = ["""
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |
                   |___/    
"""]
print(logo[0])
print(stages[0])


word_list=["camel","elephant","cat","frog"]

lives=6
chose_word=random.choice(word_list)
print(chose_word)
placeholder=""
for letter in range(len(chose_word)):
    placeholder+="_"
print(placeholder)

game_over=False
correct_letter = []
while not game_over:
        print(f"******* {lives} LIFE REMINING *******")
        guess=input("Guess a letter : ").lower()
        if guess in correct_letter:
            print(f"You already guessed  {guess}")
        display=""
        for letter in chose_word:
            if letter == guess:
                display+=letter
                correct_letter.append(letter)
            elif letter in correct_letter:
                display+=letter
            else:
                display+="_"

        print(display)
        if guess not in chose_word:
            lives-=1
            print(f"Yoy had guessed {guess} ,that is not in the list ,You lost one life")
            print(stages[lives])
            if lives==0:
                game_over=True
                print(f"You loose,The correct word was {chose_word}")

        if display==chose_word:
            game_over==True
            print("You Win")

