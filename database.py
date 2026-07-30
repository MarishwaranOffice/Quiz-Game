# database.py

import sqlite3
from datetime import datetime

DB_NAME = "quiz.db"


class Database:

    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cur = self.conn.cursor()

        self.create_tables()

    def create_tables(self):

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS players(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            level INTEGER DEFAULT 1,
            xp INTEGER DEFAULT 0,
            coins INTEGER DEFAULT 0
        )
        """)

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS scores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            score INTEGER,
            total INTEGER,
            percentage REAL,
            played_on TEXT
        )
        """)

        self.conn.commit()

    def create_player(self, username):

        try:
            self.cur.execute(
                "INSERT INTO players(username) VALUES(?)",
                (username,)
            )
            self.conn.commit()

        except:
            pass

    def get_player(self, username):

        self.cur.execute(
            "SELECT * FROM players WHERE username=?",
            (username,)
        )

        return self.cur.fetchone()

    def add_score(self, username, score, total):

        percentage = (score / total) * 100

        self.cur.execute(
            """
            INSERT INTO scores
            (username,score,total,percentage,played_on)
            VALUES(?,?,?,?,?)
            """,
            (
                username,
                score,
                total,
                percentage,
                datetime.now().strftime("%d-%m-%Y %H:%M")
            )
        )

        self.conn.commit()

    def update_xp(self, username, xp):

        player = self.get_player(username)

        if player is None:
            return

        current_xp = player[3]
        current_level = player[2]
        current_coins = player[4]

        new_xp = current_xp + xp

        level = current_level
        coins = current_coins

        while new_xp >= 100:
            new_xp -= 100
            level += 1
            coins += 50

        self.cur.execute(
            """
            UPDATE players
            SET xp=?,
                level=?,
                coins=?
            WHERE username=?
            """,
            (
                new_xp,
                level,
                coins,
                username
            )
        )

        self.conn.commit()

    def leaderboard(self):

        self.cur.execute("""
        SELECT username,
               MAX(score),
               MAX(percentage)
        FROM scores
        GROUP BY username
        ORDER BY percentage DESC
        """)

        return self.cur.fetchall()

    def history(self, username):

        self.cur.execute(
            """
            SELECT score,total,percentage,played_on
            FROM scores
            WHERE username=?
            ORDER BY id DESC
            """,
            (username,)
        )

        return self.cur.fetchall()

    def close(self):
        self.conn.close()


if __name__ == "__main__":

    db = Database()

    db.create_player("Mari")

    db.add_score("Mari", 18, 20)

    db.update_xp("Mari", 75)

    print(db.get_player("Mari"))

    print(db.leaderboard())

    print(db.history("Mari"))

    db.close()
