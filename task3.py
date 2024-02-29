import tkinter as tk
from tkinter import messagebox
import time


class CountdownTimer:
    def __init__(self, minutes):
        self.root = tk.Tk()
        self.root.title("Countdown Timer")

        self.minutes = minutes
        self.seconds = self.minutes * 60

        self.label = tk.Label(self.root, text="", font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_timer)
        self.stop_button.pack(pady=10)

        self.running = False

    def start_timer(self):
        self.running = True
        while self.running and self.seconds > 0:
            self.update_timer()
            time.sleep(1)
            self.seconds -= 1

        if self.seconds == 0:
            messagebox.showinfo("Timer", "Time's up!")
            self.stop_timer()

    def stop_timer(self):
        self.running = False

    def update_timer(self):
        minutes = self.seconds // 60
        seconds = self.seconds % 60
        self.label.config(text=f"{minutes:02d}:{seconds:02d}")
        self.root.update()


if __name__ == "__main__":
    timer = CountdownTimer(1)  # Set timer duration in minutes
    timer.root.mainloop()
