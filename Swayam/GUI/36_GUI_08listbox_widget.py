import tkinter
parent_window = tkinter.Tk()
parent_window.title('Listbox widget ~ Demo')

list1 = tkinter.Listbox(parent_window)
list1.insert(tkinter.END, 'Python')
list1.insert(tkinter.END, 'C++')
list1.insert(tkinter.END, 'C')
list1.insert(tkinter.END, 'Java')
list1.insert(tkinter.END, 'Angular JS')

def get_item(event):
    # Read the listbox items and display the result
    index = list1.curselection()# get selected item index
    seltext = list1.get(index)# get the text at the index

    print("The item is :", seltext)

# Mouse double click on the List item to Display the List
list1.bind('<Double-Button-1>', get_item)

list1.pack()
parent_window.mainloop()