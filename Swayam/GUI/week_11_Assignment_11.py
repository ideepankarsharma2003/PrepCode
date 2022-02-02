
# Using tkinter module, write a Python GUI program to create a label and change the label font style to your own choice
import tkinter
parent_window = tkinter.Tk()
parent_window.title('Assignment 11')
label = tkinter.Label(parent_window, text = 'Hello world', height=100, width=200, font=("Comic Sans MS", 20, "bold"), bg='red', fg='blue')
label.pack()
parent_window.mainloop()