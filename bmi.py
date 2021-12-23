from tkinter import *
from tkinter import ttk as lk


def calculate(*args):
    value1 = float(h1.get())
    value2 = float(w1.get())
    bmi1.set(float(value1/(value2 * value2)))


root = Tk()
root.title("Westeros")
#root.geometry("500x200")

frame = lk.Frame(root, padding="4 4 16 16")
frame.grid(column=4, row=8,sticky=(W,E))
root.columnconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

lk.Label(frame, text="BMI INDEX CLACULATOR",font=("helvetica", 15)).grid(columnspan=5)
lk.Label(frame,text="Weight (KG)").grid(column=2, row=2)
lk.Label(frame,text="Height (KG)").grid(column=3, row=2)
lk.Label(frame,text="Robert").grid(column=1, row= 2)
lk.Label(frame,text="Cersei").grid(column=1, row= 3)
lk.Label(frame,text="Lucifer").grid(column=1, row= 4)
lk.Label(frame,text="Targeryan").grid(column=1, row= 5)
lk.Label(frame,text="Thomas").grid(column=1, row= 6)

w1 = StringVar()
w1_enter = lk.Entry(frame, width =10, textvariable=w1)
w1_enter.grid(column= 2,row = 3)

h1 = StringVar()
h1_enter = lk.Entry(frame, width =10, textvariable=h1)
h1_enter.grid(column= 3,row = 3)

bmi1 = StringVar()
lk.Label(frame,textvariable= bmi1).grid(column=4, row= 3)


lk.Button(frame, text="Calculate", command= calculate).grid(column= 4,row = 8)

for x in frame.winfo_children():
    x.grid_configure(padx = 5, pady= 5)
 
w1_enter.focus()
root.bind("<Return>",calculate)


root.mainloop()








