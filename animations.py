# animations.py

import customtkinter as ctk


class FadeAnimation:

    def __init__(self, window):
        self.window = window

    def fade_in(self):

        self.window.attributes("-alpha", 0)

        self.alpha = 0

        self.animate_in()

    def animate_in(self):

        if self.alpha < 1:

            self.alpha += 0.05

            self.window.attributes("-alpha", self.alpha)

            self.window.after(20, self.animate_in)

    def fade_out(self):

        self.alpha = 1

        self.animate_out()

    def animate_out(self):

        if self.alpha > 0:

            self.alpha -= 0.05

            self.window.attributes("-alpha", self.alpha)

            self.window.after(20, self.animate_out)


class ButtonAnimation:

    def __init__(self, button):

        self.button = button

        self.default_width = 180
        self.default_height = 40

        self.button.bind("<Enter>", self.enter)
        self.button.bind("<Leave>", self.leave)

    def enter(self, event):

        self.button.configure(
            width=195,
            height=45
        )

    def leave(self, event):

        self.button.configure(
            width=self.default_width,
            height=self.default_height
        )


class PulseLabel:

    def __init__(self, label):

        self.label = label

        self.size = 24

        self.direction = 1

        self.animate()

    def animate(self):

        self.size += self.direction

        if self.size >= 30:
            self.direction = -1

        if self.size <= 24:
            self.direction = 1

        self.label.configure(
            font=("Arial", self.size, "bold")
        )

        self.label.after(
            120,
            self.animate
        )


class ProgressAnimation:

    def __init__(self, progressbar):

        self.progressbar = progressbar

    def animate(self, value):

        current = self.progressbar.get()

        if current < value:

            current += 0.01

            self.progressbar.set(current)

            self.progressbar.after(
                8,
                lambda: self.animate(value)
            )


class ShakeWindow:

    def __init__(self, window):

        self.window = window

    def shake(self):

        x = self.window.winfo_x()

        y = self.window.winfo_y()

        positions = [
            x-10,
            x+10,
            x-8,
            x+8,
            x-5,
            x+5,
            x
        ]

        self.move(positions, y)

    def move(self, positions, y):

        if len(positions) == 0:
            return

        self.window.geometry(
            f"+{positions[0]}+{y}"
        )

        self.window.after(
            30,
            lambda: self.move(positions[1:], y)
        )


class TypeWriter:

    def __init__(self, label, text):

        self.label = label

        self.text = text

        self.index = 0

        self.type()

    def type(self):

        if self.index <= len(self.text):

            self.label.configure(
                text=self.text[:self.index]
            )

            self.index += 1

            self.label.after(
                40,
                self.type
            )


if __name__ == "__main__":

    app = ctk.CTk()

    app.geometry("600x400")

    title = ctk.CTkLabel(
        app,
        text="Ultimate Quiz Master",
        font=("Arial",24,"bold")
    )

    title.pack(pady=30)

    PulseLabel(title)

    progress = ctk.CTkProgressBar(app,width=300)

    progress.pack(pady=20)

    ProgressAnimation(progress).animate(1)

    button = ctk.CTkButton(
        app,
        text="Play"
    )

    button.pack(pady=20)

    ButtonAnimation(button)

    FadeAnimation(app).fade_in()

    app.mainloop()
