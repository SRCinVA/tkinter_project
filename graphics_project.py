from tkinter import *

window = Tk()

def km_to_miles():
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)  # pass an argument to put the string in the text field at the END of the field.

b1=Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0,column=0, rowspan=3)

# an entry widget:
e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

# one for text (with parameters for dimensions, and for iOS, to highlight the text box):
t1=Text(window, height=1, width=20, bd=1, relief='sunken')
t1.grid(row=0,column=2)

# should be at the end.
window.mainloop()