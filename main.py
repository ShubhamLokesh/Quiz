from data import question_data
from ui import QuizInterface
import html


class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


class QuizBrain:

    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0
        self.current_question = None

    def still_question(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_no]
        self.question_no += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q{self.question_no}:- {q_text} (True/False)?: "
        # user_answer = input(f"Q{self.question_no}:- {q_text} (True/False)?: ")
        # self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False


question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)


print("Completed the Quiz")
print(f"Your Final Score {quiz.score}/{quiz.question_no}")
