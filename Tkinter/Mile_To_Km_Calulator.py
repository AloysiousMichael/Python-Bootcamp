from tkinter import *

windows=Tk()
windows.title("Miles To Kilo Meter")
windows.minsize(width=300,height=300)

#entry

inputmile=Entry(width=7)
inputmile.grid(column=5,row=0)

#label
my_label1=Label(text="Miles")
my_label1.grid(column=6,row=0)
my_label1.config(padx=10,pady=10)



#label2

my_label2=Label(text="is equal to")
my_label2.grid(column=0,row=1)
my_label2.config(padx=10,pady=10)


#label3

my_label3=Label(text="0")
my_label3.grid(column=5,row=1)
my_label3.config(padx=10,pady=10)


#label4

my_label4=Label(text="Km")
my_label4.grid(column=6,row=1)
my_label4.config(padx=10,pady=10)


def calculate_km():

    miles = float(inputmile.get())
    km=round(miles*1.609)
    my_label3.config(text=f"{km}")


button=Button(text="Calculate",command=calculate_km)
button.grid(column=5,row=3)









# def output():
#     val=inputmile.get()
#



windows.mainloop()