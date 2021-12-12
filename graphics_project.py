from tkinter import *

# for iOS, have to put the function first
def km_to_miles():
    print("Success!") # printing out a statment helps you highlight where problems are happening

window = Tk()

b1=Button(window, text="Execute", command=km_to_miles()) # .. AND you need the brackets for iOS.
b1.grid(row=0,column=0, rowspan=3)

# an entry widget:
e1=Entry(window)
e1.grid(row=0,column=1)

# one for text (with parameters for dimensions, and for iOS, to highlight the text box):
t1=Text(window, height=1, width=20, bd=1, relief='sunken')
t1.grid(row=0,column=2)

# should be at the end.
window.mainloop()