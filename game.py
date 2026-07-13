# important imports

from random import randint

from difficulty import difficulties

# ====  Game logic =====
# ======================


class Game:
    """A game model with the basic logic."""

    def __init__(self, difficulty):
        """initializes the instance's attributes."""

        self.difficulty = difficulty
        self.range = difficulties[self.difficulty]["range"]
        self.max_attempts = difficulties[self.difficulty]["attempts"]
        self.guess = 0
        self.answer = randint(1, self.range)
        self.attempts = 0

    def game_over(self):
        """Logic behind reaching a maximum of attempts."""

        if self.attempts >= self.max_attempts:
            print("\tOut of attempts!")
            return True

    def hint(self):
        """Output depending on input"""

        if self.guess < self.answer:
            print("Too low! Jezz again!")
            self.attempts += 1
        elif self.guess > self.answer:
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
            return True

    def play_round(self):
        """Initializes a game round."""

        print("=" * 14)
        print("=  WELCOME  =")
        print("-" * 14)
        while True:
            try:
                print(f"\tAttempts: {self.attempts}/{self.max_attempts}")
                self.guess = int(input(f"Enter your guess (1-{self.range}):\n"))

                if self.guess == self.answer:
                    print("You jezzed right")
                    print(f"With {self.attempts + 1} attempts")
                    if self.another_one():
                        continue
                    else:
                        break
                if self.guess != self.answer:
                    self.hint()
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
