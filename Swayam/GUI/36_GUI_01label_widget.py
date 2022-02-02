import tkinter
parent_window = tkinter.Tk() 
parent_window.title('Label Widget ~ DEMO')

label = tkinter.Label(parent_window, text = 'Hello world', height=100, width=200, bg='red', fg='blue')
label.pack()
parent_window.mainloop()