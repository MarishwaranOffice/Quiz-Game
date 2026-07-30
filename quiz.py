# quiz.py

import customtkinter as ctk
from tkinter import messagebox
import random

from database import Database

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
        "question": "Capital of India?",
        "options": [
            "Delhi",
            "Mumbai",
            "Chennai",
            "Kolkata"
        ],
        "answer": "Delhi"
    },
    {
        "question": "5 + 15 = ?",
        "options": [
            "18",
            "19",
            "20",
            "21"
        ],
        "answer": "20"
    }
]

random.shuffle(QUESTIONS)


class QuizWindow(ctk.CTk):

    def __init__(self, username):
        super().__init__()

        self.db = Database()

        self.user = username

        self.title("Ultimate Quiz Master")

        self.geometry("900x600")

        self.score = 0
        self.index = 0

        self.timer = 20

        self.titleLabel = ctk.CTkLabel(
            self,
            text=f"Player : {username}",
            font=("Arial",28,"bold")
        )

        self.titleLabel.pack(pady=15)

        self.timerLabel = ctk.CTkLabel(
            self,
            text="Time : 20",
            font=("Arial",20)
        )

        self.timerLabel.pack()

        self.progress = ctk.CTkProgressBar(
            self,
            width=600
        )

        self.progress.pack(pady=20)

        self.question = ctk.CTkLabel(
            self,
            text="",
            wraplength=700,
            font=("Arial",24)
        )

        self.question.pack(pady=25)

        self.var = ctk.StringVar()

        self.buttons=[]

        for i in range(4):

            b=ctk.CTkRadioButton(
                self,
                text="",
                variable=self.var,
                value=i,
                font=("Arial",18)
            )

            b.pack(anchor="w",padx=150,pady=10)

            self.buttons.append(b)

        self.nextBtn=ctk.CTkButton(
            self,
            text="Next Question",
            command=self.next_question,
            width=220,
            height=45
        )

        self.nextBtn.pack(pady=25)

        self.load_question()

        self.countdown()

    def load_question(self):

        self.var.set("")

        self.timer=20

        q=QUESTIONS[self.index]

        self.question.configure(text=q["question"])

        for i in range(4):
            self.buttons[i].configure(text=q["options"][i])

        self.progress.set((self.index+1)/len(QUESTIONS))

    def countdown(self):

        self.timerLabel.configure(
            text=f"Time : {self.timer}"
        )

        if self.timer>0:

            self.timer-=1

            self.after(
                1000,
                self.countdown
            )

        else:

            self.next_question()

    def next_question(self):

        if self.var.get()!="":

            choice=int(self.var.get())

            if QUESTIONS[self.index]["options"][choice]==QUESTIONS[self.index]["answer"]:

                self.score+=1

        self.index+=1

        if self.index==len(QUESTIONS):

            self.finish()

            return

        self.load_question()

    def finish(self):

        xp=self.score*20

        self.db.add_score(
            self.user,
            self.score,
            len(QUESTIONS)
        )

        self.db.update_xp(
            self.user,
            xp
        )

        player=self.db.get_player(
            self.user
        )

        messagebox.showinfo(
            "Completed",
            f"""
Quiz Finished

Score : {self.score}/{len(QUESTIONS)}

XP Earned : {xp}

Level : {player[2]}

Coins : {player[4]}
"""
        )

        self.destroy()
