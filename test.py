import tkinter as tk
import requests
import random

API_URL = "https://www.balldontlie.io/api/v1/teams"
def fetch_teams(self):
    headers = {
        "Authorization": "f9eb4f44-79b4-48c2-9e40-38d25c59b741"  # <-- replace this
    }

    response = requests.get(API_URL, headers=headers)

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text[:300])  # 👈 THIS is the key

    if response.status_code != 200:
        print("Request failed.")
        return []

    try:
        data = response.json()
        return data.get("data", [])
    except Exception as e:
        print("JSON PARSE ERROR:", e)
        return []
class NBAQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NBA Team Guessing Game")

        self.teams = self.fetch_teams()
        self.current_team = None

        self.label = tk.Label(root, text="Guess the NBA Team!", font=("Arial", 16))
        self.label.pack(pady=10)

        self.hint_label = tk.Label(root, text="", font=("Arial", 12))
        self.hint_label.pack(pady=5)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.next_btn = tk.Button(root, text="Next Team", command=self.new_round)
        self.next_btn.pack(pady=5)

        self.choice_buttons = []
        for i in range(4):
            btn = tk.Button(self.button_frame, text="", width=25,
                            command=lambda i=i: self.check_guess(i))
            btn.grid(row=i, column=0, pady=5)
            self.choice_buttons.append(btn)

        self.new_round()

    def fetch_teams(self):
        response = requests.get(API_URL)
        data = response.json()
        return data["data"]

    def new_round(self):
        self.current_team = random.choice(self.teams)
        self.result_label.config(text="")

        # Hint
        hint = f"Hint: {self.current_team['conference']} Conference, {self.current_team['division']} Division"
        self.hint_label.config(text=hint)

        # Generate choices
        choices = [self.current_team]
        while len(choices) < 4:
            team = random.choice(self.teams)
            if team not in choices:
                choices.append(team)

        random.shuffle(choices)
        self.correct_index = choices.index(self.current_team)

        # Update buttons
        for i, btn in enumerate(self.choice_buttons):
            btn.config(text=choices[i]["full_name"], state=tk.NORMAL)

    def check_guess(self, index):
        if index == self.correct_index:
            self.result_label.config(text="✅ Correct!", fg="green")
        else:
            correct_name = self.current_team["full_name"]
            self.result_label.config(
                text=f"❌ Wrong! It was {correct_name}",
                fg="red"
            )

        # Disable buttons after answer
        for btn in self.choice_buttons:
            btn.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = NBAQuizApp(root)
    root.mainloop()