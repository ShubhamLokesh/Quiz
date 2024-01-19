from tkinter import *

THEME_COLOR = '#375362'
FONT = ('Ariel', 20, 'italic')


class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.screen = Tk()
        self.screen.title('Quizzler')
        self.screen.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f'Score: 0', bg=THEME_COLOR, fg='White')
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg='white')
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.question = self.canvas.create_text(150, 125, width=250, text="", font=FONT)

        self.true_image = PhotoImage(file='images/true.png')
        self.true = Button(image=self.true_image, bg=THEME_COLOR, command=self.true_pressed)
        self.true.grid(row=2, column=0)
        self.false_image = PhotoImage(file='images/false.png')
        self.false = Button(image=self.false_image, bg=THEME_COLOR, command=self.false_pressed)
        self.false.grid(row=2, column=1)

        self.get_next_question()

        self.screen.mainloop()

    def get_next_question(self):
        if self.quiz.still_question():
            q_text = self.quiz.next_question()
            self.canvas.config(bg='White')
            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.config(bg='White')
            self.canvas.itemconfig(self.question, text='You have reach the end of quiz')
            self.true.config(state='disabled')
            self.false.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.screen.after(1000, self.get_next_question)
