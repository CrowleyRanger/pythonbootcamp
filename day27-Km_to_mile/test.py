from tkinter import *

window = Tk()
window.title("Test GUI")
window.minsize(width=500, height=300)
window.config(padx=50, pady=200)

# LABEL
label = Label(text="Write below, and change this bullshit here >;(", font=("Courier", 12, "bold"))
label.grid(column=0, row=0)

# # KWARGS
# class Car:

#     # Use .get, because if the value is not specified, it's returned none
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")

# my_car = Car(make="Nissan", model="GT-R")
# Label(text=my_car.model, font=("Courier", 16, "normal")).pack()

label_text = "Button clicked"
def button_clicked():
    get_input = input.get()
    label.config(text=get_input)

input = Entry(width=10)
input.grid(column=0, row=1)

button = Button(text="Click here", command=button_clicked)
button.grid(column=0, row=2)

window.mainloop()