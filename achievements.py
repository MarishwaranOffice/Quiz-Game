# achievements.py

import customtkinter as ctk
from database import Database


class AchievementSystem:

    def __init__(self, username):

        self.db = Database()
        self.username = username

    def get_achievements(self):

        player = self.db.get_player(self.username)

        history = self.db.history(self.username)

        achievements = []

        if player is None:
            return achievements

        level = player[2]
        coins = player[4]

        if len(history) >= 1:
            achievements.append("🎯 First Quiz Completed")

        if len(history) >= 10:
            achievements.append("🔥 Quiz Veteran")

        if level >= 5:
            achievements.append("⭐ Level 5 Reached")

        if level >= 10:
            achievements.append("👑 Level 10 Master")

        if coins >= 100:
            achievements.append("💰 Coin Collector")

        if coins >= 500:
            achievements.append("🏆 Rich Player")

        for record in history:

            if record[2] == 100:
                achievements.append("💯 Perfect Score")
                break

        return achievements


class AchievementWindow(ctk.CTk):

    def __init__(self, username):

        super().__init__()

        self.title("Achievements")
        self.geometry("600x500")

        system = AchievementSystem(username)

        ctk.CTkLabel(
            self,
            text="🏅 Achievements",
            font=("Arial",30,"bold")
        ).pack(pady=20)

        frame = ctk.CTkScrollableFrame(
            self,
            width=500,
            height=340
        )

        frame.pack()

        achievements = system.get_achievements()

        if len(achievements) == 0:

            ctk.CTkLabel(
                frame,
                text="No Achievements Yet",
                font=("Arial",20)
            ).pack(pady=20)

        else:

            for achievement in achievements:

                card = ctk.CTkFrame(
                    frame,
                    width=450,
                    height=60
                )

                card.pack(pady=10)

                ctk.CTkLabel(
                    card,
                    text=achievement,
                    font=("Arial",18)
                ).pack(pady=15)


if __name__ == "__main__":

    app = AchievementWindow("Mari")
    app.mainloop()
