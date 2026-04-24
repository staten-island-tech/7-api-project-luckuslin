import tkinter as tk
from tkinter import messagebox
import requests
import random

API_URL = "https://api.balldontlie.io/v1/teams"

class NBAGuessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🏀 Guess the NBA Team")

        self.teams = []
        self.current_team = None
        self.hint_level = 0
        self.score = 0

        self.fetch_teams()

        self.label = tk.Label(root, text="Guess the NBA Team!", font=("Arial", 16))
        self.label.pack(pady=10)

        self.hint_label = tk.Label(root, text="", font=("Arial", 12))
        self.hint_label.pack(pady=5)

        self.dropdown_var = tk.StringVar(root)
        self.dropdown = tk.OptionMenu(root, self.dropdown_var, [])
        self.dropdown.pack(pady=10)

        self.guess_button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.hint_button = tk.Button(root, text="Get Hint", command=self.show_hint)
        self.hint_button.pack(pady=5)

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        self.next_button = tk.Button(root, text="Next Team", command=self.new_round)
        self.next_button.pack(pady=5)

        self.new_round()

    def fetch_teams(self):
        try:
            headers = {
            "Authorization": API_KEY
        }

            response = requests.get(API_URL, headers=headers)
            data = response.json()
            self.teams = data["data"]

        team_names = [team["full_name"] for team in self.teams]
        self.dropdown["menu"].delete(0, "end")

        for name in team_names:
            self.dropdown["menu"].add_command(
                label=name,
                command=tk._setit(self.dropdown_var, name)
            )

        self.dropdown_var.set(team_names[0])

        except Exception as e:
    messagebox.showerror("Error", f"Failed to fetch teams:\n{}")

    def new_round(self):
        self.current_team = random.choice(self.teams)
        self.hint_level = 0
        self.hint_label.config(text="New team selected! Click 'Get Hint'")

    def show_hint(self):
        if not self.current_team:
            return

        hints = [
            f"Conference: {self.current_team['conference']}",
            f"Division: {self.current_team['division']}",
            f"City: {self.current_team['city']}",
        ]

        if self.hint_level < len(hints):
            self.hint_label.config(text=hints[self.hint_level])
            self.hint_level += 1
        else:
            self.hint_label.config(text="No more hints!")

    def check_guess(self):
        guess = self.dropdown_var.get()
        correct = self.current_team["full_name"]

        if guess == correct:
            self.score += 1
            messagebox.showinfo("Correct!", f"Nice! It was {correct}")
        else:
            messagebox.showerror("Wrong!", f"It was {correct}")

        self.score_label.config(text=f"Score: {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NBAGuessGame(root)
    root.mainloop()