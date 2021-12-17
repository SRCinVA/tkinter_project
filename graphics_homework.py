from tkinter import *

window = Tk()

T = Text(window, height = 1, width = 2)
T.insert(INSERT, "Kg")
T.grid(row=0,column=0)

def do_conversion():
    grams = float(e1_value.get())*1000
    t1.insert(END, grams)  # pass an argument to put the string in the text field at the END of the field.
    pounds = float(e1_value.get())*2.20462
    t2.insert(END, pounds)  # pass an argument to put the string in the text field at the END of the field.
    ounces = float(e1_value.get())*35.274
    t3.insert(END, ounces)  # pass an argument to put the string in the text field at the END of the field.

b1=Button(window, text="Convert", command=do_conversion)
b1.grid(row=0,column=2, rowspan=3)

# an entry widget:
e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

# one for text (with parameters for dimensions, and for iOS, to highlight the text box):
t1=Text(window, height=1, width=20, bd=1, relief='sunken')
t1.grid(row=3,column=0)

t2=Text(window, height=1, width=20, bd=1, relief='sunken')
t2.grid(row=3,column=1)

t3=Text(window, height=1, width=20, bd=1, relief='sunken')
t3.grid(row=3,column=2)

# should be at the end.
window.mainloop()