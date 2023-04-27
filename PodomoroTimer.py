import tkinter as tk
import pygame

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Timer")

        self.seconds_left = 25 * 60  # 25 minutes
        self.is_running = False

        self.timer_label = tk.Label(master, text="00:00", font=("Arial", 48))
        self.timer_label.pack(pady=50)

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack(side="left", padx=10)

        self.pause_button = tk.Button(master, text="Pause", command=self.pause_timer, state="disabled")
        self.pause_button.pack(side="left", padx=10)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer, state="disabled")
        self.stop_button.pack(side="left", padx=10)

        pygame.mixer.init()

    def countdown(self):
        if self.seconds_left > 0 and self.is_running:
            self.seconds_left -= 1
            self.update_timer_label()
            self.master.after(1000, self.countdown)  # Call this method again after 1000 ms (1 second)
        elif self.is_running:
            self.play_alarm()

    def update_timer_label(self):
        minutes, seconds = divmod(self.seconds_left, 60)
        self.timer_label.configure(text=f"{minutes:02d}:{seconds:02d}")

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.config(state="disabled")
            self.pause_button.config(state="normal")
            self.stop_button.config(state="normal")
            self.countdown()

    def pause_timer(self):
        if self.is_running:
            self.is_running = False
            self.start_button.config(state="normal")
            self.pause_button.config(state="disabled")

    def stop_timer(self):
        if self.is_running or self.seconds_left != 25 * 60:
            self.is_running = False
            self.seconds_left = 25 * 60
            self.update_timer_label()
            self.start_button.config(state="normal")
            self.pause_button.config(state="disabled")
            self.stop_button.config(state="disabled")

    def play_alarm(self):
        pygame.mixer.music.load("alarm_sound.wav")  # Replace "alarm_sound.wav" with the path to your sound file
        pygame.mixer.music.play()

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
