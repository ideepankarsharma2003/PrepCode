import tkinter
parent_window = tkinter.Tk() 
parent_window.title('Radiobutton Widget ~ DEMO')

label = tkinter.Label(parent_window, text = 'Choose your Favourite Language :')

def var_status():
    print("You've choosen : ", var1.get())

var1 = tkinter.IntVar()


radiobutton1 = tkinter.Radiobutton(parent_window, text = 'Java', command=var_status, width=200, variable = var1, value=1)
radiobutton2 = tkinter.Radiobutton(parent_window, text = 'C++', command=var_status, width=200, variable = var1, value=2)
radiobutton3 = tkinter.Radiobutton(parent_window, text = 'Python', command=var_status, width=200,variable = var1, value=3)



label.pack()

radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()

parent_window.mainloop()