from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_cards={}
to_learn={}

try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

def next_card():
    global current_cards,flip_timer
    window.after_cancel(flip_timer)
    current_cards=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_name,text=current_cards["French"])
    canvas.itemconfig(card_background,image=card_front)
    flip_timer=window.after(3000,func=flip_card)


def flip_card():
    canvas.itemconfig(card_title,text="English")
    canvas.itemconfig(card_name,text=current_cards["English"])
    canvas.itemconfig(card_background,image=card_back)


def is_known():
    to_learn.remove(current_cards)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

window=Tk()
window.title("Card flash game")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip_card)
canvas=Canvas(width=800,height=526)
card_front=PhotoImage(file="images/card_front.png")
card_back=PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400,263,image=card_front)
card_title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_name=canvas.create_text(400,256,text="",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_image=PhotoImage(file="images/wrong.png")
unkown_button=Button(image=cross_image,highlightthickness=0,command=next_card)
unkown_button.grid(row=1,column=0)
check_image=PhotoImage(file="images/right.png")
unkown_button2=Button(image=check_image,highlightthickness=0,command=is_known)
unkown_button2.grid(row=1,column=1)

next_card()

window.mainloop()