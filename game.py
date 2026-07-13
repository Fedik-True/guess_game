# ====  Game logic =====
# ======================

from random import randint

from difficulty import difficulties


class Game:
    """A game model with the basic logic."""

    def __init__(self, difficulty):
        """initializes the instance's attributes."""
        self.difficulty = difficulty
        self.range = difficulties[self.difficulty]["range"]
        self.max_attempts = difficulties[self.difficulty]["attempts"]

        self.answer = randint(1, self.range)
        self.attempts = 0
        self.history = []

    def get_guess(self):
        """Inputs for a guess."""
        guess = int(input(f"Enter your guess (1-{self.range}):\n"))
        return guess

    def game_over(self):
        """Logic behind reaching a maximum of attempts."""
        if self.attempts >= self.max_attempts:
            print("\tOut of attempts!")
            return True

    def hint(self, guess):
        """Output depending on input"""
        if guess < self.answer:
            print("Too low! Jezz again!")
            self.attempts += 1
        elif guess > self.answer:
            print("Too  high! Jezz again!")
            self.attempts += 1

    def another_one(self):
        """Questioning another game."""
        another = input("Play again? (y/n)\n")
        if another == "n":
            print("Bye!")
            return False
        else:
            print("Let's go!")
            self.attempts = 0
            self.history.clear()
            self.answer = randint(1, self.range)
            return True

    def history_attempts(self, guess):
        """Recording the history of attempts."""
        return self.history.append(guess)

    def show_history(self):
        """Return the history of attempts."""
        for idx, value in enumerate(self.history):
            tabs = min(idx, len(self.history) - idx - 1)

            print(f"{'\t' * tabs}{idx + 1}.) {value}")

    def play_round(self):
        """Initializes a game round."""
        print("=" * 14)
        print("=  WELCOME  =")
        print("-" * 14)
        while True:
            try:
                print(f"\tAttempts: {self.attempts}/{self.max_attempts}")
                guess = self.get_guess()
                self.history_attempts(guess)

                if guess == self.answer:
                    print("You jezzed right")
                    print(f"With {self.attempts + 1} attempts")
                    self.show_history()
                    if self.another_one():
                        continue
                    else:
                        break
                if guess != self.answer:
                    self.hint(guess)
                if self.game_over():
                    if self.another_one():
                        continue
                    else:
                        break
            except ValueError:
                print("\tEnter a number!")
                continue


hra = Game("easy")
hra.play_round()
