from tkinter import *
import time

FONT_NAME = "Courier"
BLUE = "#2d4059"
PINK = "#ea5455"
ORANGE = "#f07b3f"
YELLOW = "#ffd460"
CHECK_MARK = "✔"

WORKING_MIN = 25
BREAK_MIN = 5
BIG_BREAK_MIN = 15
reps = 0
mark = ""
timer = None

# ==================== TIMER RESET ==================== #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    todo_sign.config(text="Timer", font=(FONT_NAME, 36), bg=BLUE, fg=ORANGE)
    check_marks.config(text="")
    global reps
    reps = 0

# ==================== TIMER MECHANISM ==================== #
def start_timer():
    global reps
    global mark
    reps += 1
    working_sec = WORKING_MIN * 60
    break_sec = BREAK_MIN * 60
    big_break_sec = BIG_BREAK_MIN * 60
 
    if reps == 8:
        todo_sign.config(text="BIG BREAK", fg=PINK)
        count_down(big_break_sec)
    elif reps % 2 == 0:
        todo_sign.config(text="BREAK", fg=PINK)
        mark += CHECK_MARK
        check_marks.config(text=mark)
        count_down(break_sec)
    else:
        todo_sign.config(text="WORK", fg="green")
        count_down(working_sec)

# ==================== COUNTDOWN MECHANISM ==================== #
def count_down(count):

    minutes = count // 60
    seconds = count % 60
    if len(str(seconds)) == 1:
        seconds = "0" + str(seconds)

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ==================== UI SETUP ==================== #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=BLUE)

# Image dimension: 200x223
canvas = Canvas(width=200, height= 224, bg=BLUE, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill=BLUE, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

todo_sign = Label(text="Timer", font=(FONT_NAME, 36), bg=BLUE, fg=ORANGE)
todo_sign.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg="green", bg=BLUE)
check_marks.grid(column=1, row=3)

window.mainloop()