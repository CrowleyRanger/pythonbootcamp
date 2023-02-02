from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import os

def clear_screen():
    os.system("cls")

clear_screen()

question_bank = []
for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions(question_bank):
    quiz.next_question()
    print(f"SCORE: {quiz.SCORE}/{quiz.question_number}")

