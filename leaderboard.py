# leaderboard.py

import customtkinter as ctk
from database import Database


class LeaderboardWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.db = Database()

        self.title("Ultimate Quiz Master - Leaderboard")
        self.geometry("700x550")

        ctk.CTkLabel(
            self,
            text="🏆 Leaderboard",
            font=("Arial", 30, "bold")
        ).pack(pady=20)

        self.frame = ctk.CTkScrollableFrame(
            self,
            width=620,
            height=400
        )

        self.frame.pack(pady=10)

        self.load()

        ctk.CTkButton(
            self,
            text="Refresh",
            command=self.refresh
        ).pack(pady=15)

    def load(self):

        players = self.db.leaderboard()

        headers = [
            "Rank",
            "Player",
            "Best Score",
            "Percentage"
        ]

        for c, h in enumerate(headers):

            lbl = ctk.CTkLabel(
                self.frame,
                text=h,
                width=140,
                font=("Arial",18,"bold")
            )

            lbl.grid(row=0,column=c,padx=10,pady=10)

        for r, player in enumerate(players,start=1):

            rank = ctk.CTkLabel(
                self.frame,
                text=str(r),
                width=140
            )

            rank.grid(row=r,column=0)

            user = ctk.CTkLabel(
                self.frame,
                text=player[0],
                width=140
            )

            user.grid(row=r,column=1)

            score = ctk.CTkLabel(
                self.frame,
                text=str(player[1]),
                width=140
            )

            score.grid(row=r,column=2)

            percent = ctk.CTkLabel(
                self.frame,
                text=f"{player[2]:.2f} %",
                width=140
            )

            percent.grid(row=r,column=3)

    def refresh(self):

        self.destroy()

        app = LeaderboardWindow()
        app.mainloop()


if __name__ == "__main__":
    app = LeaderboardWindow()
    app.mainloop()
