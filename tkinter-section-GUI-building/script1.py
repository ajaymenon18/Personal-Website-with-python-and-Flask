from tkinter import *
window =Tk()

def km_to_miles():
    print(e1_value.get())  # Print() is to print the value in the command line
    miles = float(e1_value.get())*1.6
    t1.insert(END,miles)

#For the buttons and button processes
b1 = Button(window, text = "Execute", command= km_to_miles)
b1.grid(row=0,column=0)

# For determining the value and the entry position of the get 
e1_value = StringVar()
e1 = Entry(window, textvariable= e1_value)
e1.grid(row=0,column=1)

#For displaying the text entered
t1 = Text(window, height = 1, width = 20)
t1.grid(row = 0, column = 2)

window.mainloop()
