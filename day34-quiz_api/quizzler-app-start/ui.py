from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
GREEN = "#29B677"
RED = "#EE665D"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=340, height=400)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)      

        #Question Text
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150, 
            125,
            width=280,
            text="Question goes here!",
            fill=THEME_COLOR,
            font=("Arial", 15, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        #Score
        self.score_text = Label(text=f"Score: 0", font=("Arial"), bg=THEME_COLOR, fg="white", padx=20)
        self.score_text.grid(column=0, row=0, sticky="W")

        #Buttons
        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=self.true_img, command=self.true_pressed, highlightthickness=0, bd=0, bg=THEME_COLOR, activebackground=THEME_COLOR)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=self.false_img, command=self.false_pressed, highlightthickness=0, bd=0, bg=THEME_COLOR, activebackground=THEME_COLOR)
        self.false_button.grid(column=1, row=2)  

        self.get_next_question()              

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=GREEN)
            self.score_text.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg=RED)
        self.window.after(1000, self.get_next_question)