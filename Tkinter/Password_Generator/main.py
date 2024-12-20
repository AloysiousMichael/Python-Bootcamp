from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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

def save():

    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    new_data={
        website:{
            "email":email,
            "password":password,
        }
    }

    if(len(email) ==0 or len(password) ==0):
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty ! ")
    else:
        try:
            with open("data.json","r") as data_file:
                #Reading old data
                data=json.load(data_file)
        except FileNotFoundError:
               with open("data.json","w") as data_file:
                    json.dump(new_data,data_file,indent=4)
        else:
                #Updating old data with new data
                data.update(new_data)

                with open("data.json","w") as data_file:
                    #Saving Data
                    json.dump(data,data_file,indent=4)
        finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)

def find_password():
    website=website_entry.get()
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)

    except FileNotFoundError:
            messagebox.showinfo(title="Error",message="No Data File Found.")
    else:
        if website in data:
                email=data[website]["email"]
                password=data[website]["password"]
                messagebox.showinfo(title=website,message=f"Email : {email} \n Password : {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} found.")


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

website_entry=Entry(width=33)
website_entry.grid(row=1,column=1)
website_entry.focus()
email_entry=Entry(width=51)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"aloysiousmicheal@gmail.com")
password_entry=Entry(width=33)
password_entry.grid(row=3,column=1)

#Button

search_button=Button(text="Search",width=14,command=find_password)
search_button.grid(row=1,column=2)
generate_button=Button(text="Generate Password ",width=14,command=generate)
generate_button.grid(row=3,column=2)
add_button=Button(text="Add",width=43,command=save)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()

