import tkinter
parent_window = tkinter.Tk() 
parent_window.title('Checkbutton Widget ~ DEMO')

label = tkinter.Label(parent_window, text = 'Choose your Favourite Language :')


checkbutton1 = tkinter.Checkbutton(parent_window, text = 'Java',  width=200)
checkbutton2 = tkinter.Checkbutton(parent_window, text = 'C++',  width=200)
checkbutton3 = tkinter.Checkbutton(parent_window, text = 'Python',  width=200)

label.pack()
checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()

parent_window.mainloop()