# ====  Game logic =====
# ======================

from random import randint

from difficulty import difficulties, difficulty_map


class Game:
    """Whole game's logic and conditions."""

    def __init__(self):
        """initializes the instance's attributes."""
        self.range = 0
        self.max_attempts = 0

        self.answer = None
        self.attempts = 0
        self.history = []

    def get_guess(self):
        """Inputs for a guess."""
        while True:
            try:
                guess = int(input(f"Enter your guess (1-{self.range}):\n"))
                if 0 < guess <= self.range:
                    return guess
                print(f"Enter number in range 1 - {self.range}.")
            except ValueError:
                print("Enter a number.")

    def game_over(self):
        """Reaching a maximum of attempts."""
        if self.attempts >= self.max_attempts:
            print("\tOut of attempts!")
            return True
        else:
            return False

    def hint(self, guess):
        """Hint on wrong input."""
        if guess < self.answer:
            print("Too low! Jezz again!")
        elif guess > self.answer:
            print("Too  high! Jezz again!")

    def another_one(self):
        """Questioning another game."""
        while True:
            another = input("Play again? (y/n)\n").lower()
            if another == "n":
                print("Bye!")
                return False
            elif another == "y":
                print("Let's go!")
                return True
            else:
                print("Enter 'y' or 'n' !")
                continue

    def generate_answer(self):
        """Get a random number."""
        self.answer = randint(1, self.range)
        return self.answer

    def reset_game(self):
        """Resets game's config attributes."""
        self.attempts = 0
        self.history.clear()
        self.generate_answer()

    def history_attempts(self, guess):
        """Recording the history of attempts."""
        self.history.append(guess)

    def show_history(self):
        """Return the history of attempts."""
        for idx, value in enumerate(self.history):
            tabs = min(idx, len(self.history) - idx - 1)

            print(f"{'\t' * tabs}{idx + 1}.) {value}")

    def choose_difficulty(self):
        """Set the game's difficulty."""
        print(f"{'\t' * 2}{'=' * 20}")
        print(f"{'\t' * 2}{'=== DIFFICULTIES ==='}")
        print(f"{'\t' * 2}{'-' * 20}")
        print("Easy(1)  Medium(2)  Hard(3)  Extreme(4)  Nightmare(5)")

        while True:
            try:
                selection = int(input("Choose difficulty! (1-5)\n"))

                if selection in difficulty_map:
                    difficulty_config = difficulties[difficulty_map[selection]]
                    self.max_attempts, self.range = (
                        difficulty_config["attempts"],
                        difficulty_config["range"],
                    )
                    self.generate_answer()
                    break
                print("Please, enter a valid number.")
            except ValueError:
                print("Enter a difficulty's index.")
                continue

    def play_round(self):
        """Initializes a game round."""
        print("=" * 14)
        print("=  WELCOME  =")
        print("-" * 14)
        self.choose_difficulty()
        while True:
            print(f"\tAttempts: {self.attempts}/{self.max_attempts}")
            guess = self.get_guess()
            self.history_attempts(guess)
            self.attempts += 1

            if guess != self.answer:
                self.hint(guess)
            else:
                print("You jezzed right.")

                print(f"With {self.attempts} attempts.")
                self.show_history()
                if self.another_one():
                    self.reset_game()
                    self.choose_difficulty()
                    continue
                else:
                    break
            if self.game_over():
                print(f"The answer was '{self.answer}'")
                if self.another_one():
                    self.reset_game()
                    self.choose_difficulty()
                    continue
                else:
                    break


hra = Game()
hra.play_round()
