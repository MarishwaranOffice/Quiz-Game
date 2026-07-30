# utils.py

import json
import random
import os
import csv
from datetime import datetime


QUESTION_FOLDER = "questions"
SCORE_FILE = "scores.csv"


def load_questions(category):

    path = os.path.join(
        QUESTION_FOLDER,
        f"{category}.json"
    )

    if not os.path.exists(path):
        return []

    with open(path, "r", encoding="utf-8") as file:
        questions = json.load(file)

    random.shuffle(questions)

    return questions


def save_score(username, score, total):

    percentage = round((score / total) * 100, 2)

    file_exists = os.path.exists(SCORE_FILE)

    with open(
        SCORE_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        if not file_exists:

            writer.writerow([
                "Username",
                "Score",
                "Total",
                "Percentage",
                "Date"
            ])

        writer.writerow([
            username,
            score,
            total,
            percentage,
            datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        ])


def get_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    return "Fail"


def get_rank(score, total):

    percent = (score / total) * 100

    if percent == 100:
        return "Legend"

    elif percent >= 90:
        return "Master"

    elif percent >= 80:
        return "Expert"

    elif percent >= 70:
        return "Advanced"

    elif percent >= 60:
        return "Intermediate"

    return "Beginner"


def shuffle_options(question):

    options = question["options"][:]

    random.shuffle(options)

    question["options"] = options

    return question


def format_time(seconds):

    minutes = seconds // 60

    seconds = seconds % 60

    return f"{minutes:02}:{seconds:02}"


def random_tip():

    tips = [

        "Read every question carefully.",

        "Manage your time wisely.",

        "Use logic before guessing.",

        "Practice daily to improve.",

        "Stay calm during the quiz.",

        "Eliminate wrong answers first.",

        "Accuracy is more important than speed."

    ]

    return random.choice(tips)


def welcome_message(username):

    return f"""
Welcome {username}

Good Luck!

Today's Tip:

{random_tip()}
"""


if __name__ == "__main__":

    print(format_time(135))

    print(get_grade(92))

    print(get_rank(18,20))

    print(random_tip())

    print(welcome_message("Mari"))
