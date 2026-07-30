# main.py
# Ultimate Quiz Master - Starter

import customtkinter as ctk
from tkinter import messagebox
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

QUESTIONS = [
    {
        "question": "Who developed Python?",
        "options": [
            "Guido van Rossum",
            "Dennis Ritchie",
            "James Gosling",
            "Bjarne Stroustrup"
        ],
        "answer": "Guido van Rossum"
    },
    {
        "question": "5 + 7 = ?",
        "options": ["10", "11", "12", "13"],
        "answer": "12"
    },
    {
        "question": "Capital of India?",
        "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "HTML stands for?",
        "options": [
            "Hyper Text Markup Language",
            "High Text Machine Language",
            "Hyper Tool Markup Language",
            "None"
        ],
        "answer": "Hyper Text Markup Language"
    },
    {
        "question": "Which keyword creates a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    }
]

random.shuffle(QUESTIONS)


class QuizApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Ultimate Quiz Master")
        self.geometry("900x600")

        self.index = 0
        self.score = 0

        self.titleLabel = ctk.CTkLabel(
            self,
            text="Ultimate Quiz Master",
            font=("Arial", 30, "bold")
        )
        self.titleLabel.pack(pady=20)

        self.progress = ctk.CTkProgressBar(self, width=500)
        self.progress.pack()

        self.question = ctk.CTkLabel(
            self,
            text="",
            wraplength=700,
            font=("Arial", 22)
        )
        self.question.pack(pady=30)

        self.var = ctk.StringVar()

        self.buttons = []

        for i in range(4):
            b = ctk.CTkRadioButton(
                self,
                text="",
                variable=self.var,
                value=i,
                font=("Arial",18)
            )
            b.pack(anchor="w", padx=150, pady=10)
            self.buttons.append(b)

        self.nextBtn = ctk.CTkButton(
            self,
            text="Next",
            command=self.next_question,
            width=200,
            height=40
        )
        self.nextBtn.pack(pady=30)

        self.load_question()

    def load_question(self):

        self.var.set(-1)

        q = QUESTIONS[self.index]

        self.question.configure(text=q["question"])

        for i in range(4):
            self.buttons[i].configure(text=q["options"][i])

        self.progress.set((self.index + 1) / len(QUESTIONS))

    def next_question(self):

        if self.var.get() == "":
            messagebox.showwarning("Warning", "Select an answer")
            return

        selected = int(self.var.get())

        if QUESTIONS[self.index]["options"][selected] == QUESTIONS[self.index]["answer"]:
            self.score += 1

        self.index += 1

        if self.index == len(QUESTIONS):
            self.finish()
        else:
            self.load_question()

    def finish(self):

        for widget in self.winfo_children():
            widget.destroy()

        percent = (self.score / len(QUESTIONS)) * 100

        ctk.CTkLabel(
            self,
            text="Quiz Completed!",
            font=("Arial",32,"bold")
        ).pack(pady=30)

        ctk.CTkLabel(
            self,
            text=f"Score : {self.score}/{len(QUESTIONS)}",
            font=("Arial",24)
        ).pack(pady=20)

        ctk.CTkLabel(
            self,
            text=f"Percentage : {percent:.2f}%",
            font=("Arial",24)
        ).pack(pady=20)

        ctk.CTkButton(
            self,
            text="Play Again",
            command=self.restart,
            width=220,
            height=45
        ).pack(pady=30)

    def restart(self):

        random.shuffle(QUESTIONS)

        self.destroy()

        app = QuizApp()
        app.mainloop()


app = QuizApp()
app.mainloop()
