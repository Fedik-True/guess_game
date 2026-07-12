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

    def game_over(self):
        """Logic behind reaching a maximum of attempts."""

        if self.attempts == self.max_attempts:
            print("Out of attempts!")
            return True

    def play_round(self):
        """Initializes a game round."""

        answer = randint(1, self.range)
        self.attempts = 0

        while True:
            try:
                guess = int(input(f"Enter your guess (1-{self.range}):\n"))
                if guess == answer:
                    print("You jezzed right")
                    break
                elif guess != answer:
                    print("Wrong jezz! Try again!")
                    self.attempts += 1
                    continue
                if self.game_over():
                    break
            except ValueError:
                print("\tEnter a number!")
                continue


hra = Game("easy")
hra.play_round()
