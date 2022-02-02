import tkinter
parent_window = tkinter.Tk() 
parent_window.title('Message Widget ~ DEMO')

message1 = tkinter.Message(parent_window, text ='''This is a message widget box. 
It provides a multiline and non-editable text.''', relief= 'raised')
message2 = tkinter.Message(parent_window, text ='''This is a message widget box. 
It provides a multiline and non-editable text.''', relief= 'sunken')
message3 = tkinter.Message(parent_window, text ='''This is a message widget box. 
It provides a multiline and non-editable text.''', relief= 'groove')

message1.pack()
message2.pack()
message3.pack()

parent_window.mainloop()