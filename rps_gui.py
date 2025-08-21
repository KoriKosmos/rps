import tkinter as tk
from tkinter import messagebox
from rps import rps_logic, normalize_throw, random_throw, load_scores, save_scores


class RPSApp:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")

        self.player_wins, self.cpu_wins, self.ties = load_scores()

        self.label = tk.Label(master, text="Choose your throw:")
        self.label.pack()

        self.button_frame = tk.Frame(master)
        self.button_frame.pack()

        self.rock_button = tk.Button(
            self.button_frame, text="Rock", command=lambda: self.play("rock")
        )
        self.rock_button.grid(row=0, column=0)
        self.paper_button = tk.Button(
            self.button_frame, text="Paper", command=lambda: self.play("paper")
        )
        self.paper_button.grid(row=0, column=1)
        self.scissors_button = tk.Button(
            self.button_frame, text="Scissors", command=lambda: self.play("scissors")
        )
        self.scissors_button.grid(row=0, column=2)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.score_label = tk.Label(master, text=self.get_score_text())
        self.score_label.pack()

        self.quit_button = tk.Button(master, text="Quit", command=self.quit)
        self.quit_button.pack()

    def get_score_text(self):
        return f"Player Wins: {self.player_wins}, CPU Wins: {self.cpu_wins}, Ties: {self.ties}"

    def play(self, player_throw):
        computer_throw = random_throw()
        result = rps_logic(player_throw, computer_throw)
        self.result_label.config(text=f"Computer chose: {computer_throw}\n{result}")
        t1 = normalize_throw(player_throw)
        t2 = normalize_throw(computer_throw)
        if t1 == t2:
            self.ties += 1
        elif (
            (t1 == "rock" and t2 == "scissors")
            or (t1 == "paper" and t2 == "rock")
            or (t1 == "scissors" and t2 == "paper")
        ):
            self.player_wins += 1
        else:
            self.cpu_wins += 1
        self.score_label.config(text=self.get_score_text())
        save_scores(self.player_wins, self.cpu_wins, self.ties)

    def quit(self):
        save_scores(self.player_wins, self.cpu_wins, self.ties)
        self.master.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = RPSApp(root)
    root.mainloop()
