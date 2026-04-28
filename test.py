import tkinter as tk
from tkinter import messagebox
import requests
import random
import os

API_URL = "https://api.balldontlie.io/v1/teams"
API_KEY = ("f9eb4f44-79b4-48c2-9e40-38d25c59b741")  # safer than hardcoding


class NBAGuessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🏀 Guess the NBA Team")

        self.teams = []
        self.current_team = None
        self.hint_level = 0
        self.score = 0
        self.rounds_played = 0

        self.build_ui()
        self.fetch_teams()

    def build_ui(self):
        tk.Label(self.root, text="Guess the NBA Team!", font=("Arial", 16)).pack(pady=10)

        self.hint_label = tk.Label(self.root, text="Loading teams...", font=("Arial", 12))
        self.hint_label.pack(pady=5)

        self.dropdown_var = tk.StringVar(self.root)
        self.dropdown = tk.OptionMenu(self.root, self.dropdown_var, "")
        self.dropdown.pack(pady=10)

        tk.Button(self.root, text="Submit Guess", command=self.check_guess).pack(pady=5)
        tk.Button(self.root, text="Get Hint", command=self.show_hint).pack(pady=5)

        self.score_label = tk.Label(self.root, text="Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        self.rounds_label = tk.Label(self.root, text="Rounds: 0", font=("Arial", 12))
        self.rounds_label.pack(pady=5)

        tk.Button(self.root, text="Next Team", command=self.new_round).pack(pady=5)

    def fetch_teams(self):
        try:
            headers = {"Authorization": API_KEY} if API_KEY else {}

            response = requests.get(API_URL, headers=headers)

            if response.status_code != 200:
                raise Exception(f"API error: {response.status_code}")

            data = response.json()
            if "data" not in data:
                raise Exception("Unexpected API response")

            self.teams = [
                teams for teams in data["data"]
                if teams["conference"] in ["East" , "West"]
            ]
            
            self.populate_dropdown()
            self.new_round()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch teams:\n{e}")
            self.hint_label.config(text="Failed to load teams.")

    def populate_dropdown(self):
        menu = self.dropdown["menu"]
        menu.delete(0, "end")

        team_names = [team["full_name"] for team in self.teams]

        for name in team_names:
            menu.add_command(
                label=name,
                command=tk._setit(self.dropdown_var, name)
            )

        if team_names:
            self.dropdown_var.set(team_names[0])

    def new_round(self):
        if not self.teams:
            return

        self.rounds_played += 1
        self.rounds_label.config(text=f"Rounds: {self.rounds_played}")

        self.current_team = random.choice(self.teams)
        self.hint_level = 0
        self.hint_label.config(text="New team selected! Click 'Get Hint'")
        self.dropdown_var.set(self.teams[0]["full_name"])

    def show_hint(self):
        if not self.current_team:
            self.hint_label.config(text="No team loaded")
        
        

        hints = [
            f"This team plays in the {self.current_team['conference']}ern Conference.",
            f"This team is in the {self.current_team['division']} Division",
            f"This team has {len(self.current_team['full_name'])} letters in the name",
            f"Its first letter is: {self.current_team['full_name'][0]}",
            f"This team plays in: {self.current_team['city']}",
            ]

        if self.hint_level < len(hints):
            hint_text = hints[self.hint_level]
            self.hint_label.config(text=f"Hint {self.hint_level + 1}: {hint_text}")
            self.hint_level += 1
        else:
            self.hint_label.config(text="No more hints!")

    def check_guess(self):
        if not self.current_team:
            return

        guess = self.dropdown_var.get()
        correct = self.current_team["full_name"]

        if guess == correct:
            if self.hint_level <= 1:
                self.score += 5
            elif self.hint_level <= 3:
                self.score += 2
            else:
                self.score += 1

            self.hint_level = 0

            messagebox.showinfo("Correct!", f"Nice! It was {correct}")
        else:
            messagebox.showerror("Wrong!", f"It was {correct}")
            
        self.rounds_played += 1
        self.rounds_label.config(text=f"Rounds: {self.rounds_played}")
        
        self.score_label.config(text=f"Score: {self.score}")

    


if __name__ == "__main__":
    root = tk.Tk()
    app = NBAGuessGame(root)
    root.mainloop()