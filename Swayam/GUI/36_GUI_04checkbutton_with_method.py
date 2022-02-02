import tkinter
parent_window = tkinter.Tk() 
parent_window.title('Checkbutton Widget ~ DEMO')

label = tkinter.Label(parent_window, text = 'Choose your Favourite Language :')

def var_status():
    print("The options are : ")
    print("Java %d,\nC++ %d, \nPython %d, "%(var1.get(), var2.get(), var3.get()))

var1 = tkinter.IntVar()
var2 = tkinter.IntVar()
var3 = tkinter.IntVar()

checkbutton1 = tkinter.Checkbutton(parent_window, text = 'Java',  width=200, variable = var1)
checkbutton2 = tkinter.Checkbutton(parent_window, text = 'C++',  width=200, variable = var2)
checkbutton3 = tkinter.Checkbutton(parent_window, text = 'Python',  width=200,variable = var3)

button = tkinter.Button(parent_window, text='Click to see choices : ', command=var_status)

label.pack()
button.pack()
checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()

parent_window.mainloop()