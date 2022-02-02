import tkinter
parent_window = tkinter.Tk() 
parent_window.title('Button Widget ~ DEMO')

def callMe():
    print("A button is being clicked ")

button = tkinter.Button(parent_window, text = 'Click Me', height=100, width=200, bg='red',command = callMe)
button.pack()
parent_window.mainloop()