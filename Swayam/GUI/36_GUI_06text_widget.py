import tkinter
parent_window = tkinter.Tk() 
parent_window.title('Text Widget ~ DEMO')

text = tkinter.Text(parent_window, height =100, width=200)

text.grid()
parent_window.mainloop()