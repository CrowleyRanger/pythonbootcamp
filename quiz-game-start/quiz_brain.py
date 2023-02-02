class QuizBrain():

    def __init__(self, q_list):

        self.question_number = 0
        self.question_list = q_list
        self.SCORE = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}\n[1] True\n[2] False\n>")
        if user_answer == "1":
            user_answer = "True"
        else:
            user_answer = "False"
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self, q_list):
        if self.question_number < len(q_list):
            return True
        return False

    def check_answer(self, usr_answer, correct_answer):
        if usr_answer == correct_answer:
            self.SCORE += 1
            print("CORRECT")
        else:
            print("INCORRECT")