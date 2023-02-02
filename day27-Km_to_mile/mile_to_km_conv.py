from tkinter import *

FONT = "Courier"

window = Tk()
window.title("Mile to Km")
window.minsize(width=270, height=100)
window.config(padx=10, pady=10)

main_label = Label(text="Converter: Km/Mile", font=(FONT, 12))
main_label.place(x=10, y=0)

# ==================== KILOMETER
km_sign = Label(text="Kilometer", font=(FONT, 8))
km_sign.place(x=10, y=30)

km_input = Entry(text="Km")
km_input.config(width=15)
km_input.place(x=10, y=50)

# ==================== MILE
mile_sign = Label(text="Mile", font=(FONT, 8))
mile_sign.place(x=150, y=30)

mile_output = Label(text=0, font=(FONT, 12))
mile_output.place(x=150, y=50)

# ====================  ARROWS
center_arrows = Label(text="<>", font=(FONT, 12, "bold"))
center_arrows.place(x=115, y=50)

# =================== BUTTON
def calculate():
    miles = float(km_input.get()) * 0.6213712
    miles = format(result, ".5f")
    mile_output.config(text=miles)

calc_button = Button(text="Calculate", command=calculate)
calc_button.place(x= 100, y=100)

window.mainloop()