from tkinter import *

#creates an empty tkinter window
window =Tk()

def Kg_to_gram_pound_punces():
    #gets user value from the input box and multiplies it by 1000
    gram = float(e1_value.get())*1000

    #gets user value from the input box and multiplies it by 2.20462
    pound = float(e1_value.get())*2.20462

    #gets user value from the input box and multiplies it by 35.274
    ounce = float(e1_value.get())*35.274
    
    # Empty the Text boxes if they had text from the previous use and fill them again
    t1.delete("1.0", END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END,pound)
    t3.delete("1.0", END)
    t3.insert(END,ounce)    


b1 = Button(window, text = "Convert", command = Kg_to_gram_pound_punces)
b1.grid(row=0,column=3)

#For displaying the label 

e0 = Label(window, text = "Kg")
e0.grid(row =0, column = 0)

# For determining the value and the entry position of the get 

e1_value = StringVar()
e1 = Entry(window, textvariable= e1_value)
e1.grid(row=0,column=2)

#For displaying the text entered


t1 = Text(window, height = 1, width = 20)
t1.grid(row = 1, column = 0)

t2 = Text(window, height = 1, width = 20)
t2.grid(row =1, column = 1)

t3 = Text(window, height = 1, width = 20)
t3.grid(row =1, column = 2)

window.mainloop()
