import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiple-Choice Quiz Game")
        self.root.configure(bg="black")  # Set background color to black
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Rome", "Berlin"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Jupiter", "Saturn", "Neptune"],
                "correct_answer": "Mars"
            },
            {
                "question": "What is 20% of 150?",
                "options": ["30", "20", "25", "15"],
                "correct_answer": "30"
            },
            {
                "question": "What comes next in the series: 2, 5, 10, 17, ___?",
                "options": ["25", "26", "27", "28"],
                "correct_answer": "26"
            },
            {
                "question": "Which country is known as the 'Land of the Rising Sun'?",
                "options": ["China", "Japan", "India", "South Korea"],
                "correct_answer": "Japan"
            },
            {
                "question": "What is the square root of 64?",
                "options": ["6", "7", "8", "9"],
                "correct_answer": "8"
            },
            {
                "question": "Who is the author of the book 'To Kill a Mockingbird'?",
                "options": ["Harper Lee", "J.K. Rowling", "Charles Dickens", "Mark Twain"],
                "correct_answer": "Harper Lee"
            },
            {
                "question": "Which is the longest river in the world?",
                "options": ["Nile", "Amazon", "Yangtze", "Mississippi"],
                "correct_answer": "Nile"
            },
            {
                "question": "If 'CAT' is coded as '23-1-20', how is 'DOG' coded?",
                "options": ["5-15-7", "4-15-7", "4-16-7", "4-15-6"],
                "correct_answer": "4-15-7"
            },
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Fe", "Cu"],
                "correct_answer": "Au"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"],
                "correct_answer": "Leonardo da Vinci"
            },
            {
                "question": "Which is the largest organ in the human body?",
                "options": ["Liver", "Skin", "Heart", "Brain"],
                "correct_answer": "Skin"
            },
            {
                "question": "What is the currency of Japan?",
                "options": ["Yuan", "Dollar", "Yen", "Euro"],
                "correct_answer": "Yen"
            },
            {
                "question": "Which gas is most abundant in the Earth's atmosphere?",
                "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Argon"],
                "correct_answer": "Nitrogen"
            },
            {
                "question": "What is the tallest mountain in the world?",
                "options": ["K2", "Mount Everest", "Kangchenjunga", "Lhotse"],
                "correct_answer": "Mount Everest"
            },
            # Add more questions following the same format
        ]
        self.current_question = 0
        self.score = 0
        self.total_questions = len(self.questions)

        self.label_question = tk.Label(root, text="", font=("Arial", 12), bg="black", fg="white")  # Set text and foreground color
        self.label_question.pack()

        self.option_vars = []
        self.radio_buttons = []
        for i in range(4):
            var = tk.StringVar()
            self.option_vars.append(var)
            option = tk.Radiobutton(root, text="", variable=var, value=i, font=("Arial", 10), bg="black", fg="white", selectcolor="black")
            self.radio_buttons.append(option)
            option.pack()

        self.next_button = tk.Button(root, text="Next", command=self.check_answer, bg="white", fg="black")  # Set button background and foreground color
        self.next_button.pack()
        
        self.display_question()

    def display_question(self):
        current = self.questions[self.current_question]
        self.label_question.config(text=current["question"])
        for i in range(4):
            self.radio_buttons[i].config(text=current["options"][i])

    def check_answer(self):
        user_choice = -1
        for i, var in enumerate(self.option_vars):
            if var.get():
                user_choice = int(var.get())

        correct_answer = self.questions[self.current_question]["correct_answer"]
        if user_choice == self.questions[self.current_question]["options"].index(correct_answer):
            self.score += 1
            messagebox.showinfo("Correct", "Correct Answer!")
        else:
            correct_answer_index = self.questions[self.current_question]["options"].index(correct_answer)
            messagebox.showerror("Incorrect", f"Incorrect Answer! Correct answer is {correct_answer_index + 1}")

        self.current_question += 1
        if self.current_question < self.total_questions:
            self.display_question()
        else:
            messagebox.showinfo("Quiz Completed", f"Quiz completed! Your final score is: {self.score}/{self.total_questions}")
            self.root.destroy()

def start_quiz():
    root = tk.Tk()
    quiz_game = QuizGame(root)
    root.mainloop()

if __name__ == "__main__":
    start_quiz()
