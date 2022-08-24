from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.score_label = Label(text='Score: 0', background=THEME_COLOR, foreground='white')
        self.score_label.grid(column=1, row=0)

        self.question_box = Canvas(height=250, width=300, bg='white')
        self.question_text = self.question_box.create_text(
            150,
            125,
            text='Question goes here',
            font=('Arial', 20, 'italic')
        )
        self.question_box.grid(column=0, row=1, columnspan=2, pady=50)

        tru_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=tru_image, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()