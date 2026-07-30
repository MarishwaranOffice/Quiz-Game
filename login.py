# login.py

import customtkinter as ctk
from tkinter import messagebox
from database import Database
from quiz import QuizWindow

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class LoginWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.db = Database()

        self.title("Ultimate Quiz Master")
        self.geometry("700x500")
        self.resizable(False, False)

        ctk.CTkLabel(
            self,
            text="Ultimate Quiz Master",
            font=("Arial", 32, "bold")
        ).pack(pady=40)

        self.username = ctk.CTkEntry(
            self,
            width=300,
            height=40,
            placeholder_text="Enter Username"
        )
        self.username.pack(pady=20)

        self.info = ctk.CTkTextbox(
            self,
            width=400,
            height=120
        )
        self.info.pack()

        self.info.insert("0.0",
"""
✔ XP System
✔ Coins
✔ Levels
✔ Leaderboard
✔ Statistics
✔ Achievements
""")

        self.info.configure(state="disabled")

        ctk.CTkButton(
            self,
            text="Start Quiz",
            width=220,
            height=45,
            command=self.start
        ).pack(pady=30)

    def start(self):

        user = self.username.get().strip()

        if user == "":
            messagebox.showerror(
                "Error",
                "Enter Username"
            )
            return

        self.db.create_player(user)

        self.destroy()

        app = QuizWindow(user)
        app.mainloop()


if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()
