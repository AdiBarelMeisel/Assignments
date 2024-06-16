import tkinter as tk
from tkinter import messagebox
import random

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        self.comp_number = random.randint(1, 20)
        self.times = 0

        self.label = tk.Label(root, text="Guess a number between 1-20:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.guess_button = tk.Button(root, text="Guess", command=self.guess_number)
        self.guess_button.pack()

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game)
        self.restart_button.pack()

        self.cheat_button = tk.Button(root, text="Show Answer", command=self.show_answer)
        self.cheat_button.pack()

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def guess_number(self):
        user_input = self.entry.get()
        if user_input.isdigit():
            guessed_number = int(user_input)
            self.times += 1
            if guessed_number > self.comp_number:
                self.result_label.config(text="Your number is too high. Try again.")
            elif guessed_number < self.comp_number:
                self.result_label.config(text="Your number is too low. Try again.")
            else:
                self.result_label.config(text=f"You guessed the exact number in {self.times} attempts!")
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid number between 1 and 20")

    def restart_game(self):
        self.comp_number = random.randint(1, 20)
        self.times = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        messagebox.showinfo("Game Restarted", "A new number has been generated. Start guessing!")

    def show_answer(self):
        messagebox.showinfo("Cheat", f"The number to guess is: {self.comp_number}")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
