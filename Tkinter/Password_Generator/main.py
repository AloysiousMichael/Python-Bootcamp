from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(4,6 )
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter=[random.choice(letters) for i in range(nr_letters)]
    password_symbol=[random.choice(symbols) for i in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for i in range(nr_numbers)]



    password_list=password_letter+password_symbol+password_numbers


    random.shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)
 #Labels

website_label=Label(text="Website:")
website_label.grid(row=1,column=0)
email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

#Entries

website_entry=Entry(width=45)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry=Entry(width=45)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"aloysiousmicheal@gmail.com")
password_entry=Entry(width=27)
password_entry.grid(row=3,column=1)



#Button

def save():

    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    if(len(email) ==0 or len(password) ==0):
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty ! ")
    else:

        is_ok =messagebox.askokcancel(title="Website",message=f"These are the details entered : \n Email : {email} \n Password :{password} \n Is it ok to save ?")

        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
        else:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


generate_button=Button(text="Generate Password ",width=14,command=generate)
generate_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()
