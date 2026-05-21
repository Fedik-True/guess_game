import random

DIFFICULTIES = {
    "easy": (10, 50),
    "medium": (7, 40),
    "hard": (4, 25),
    "extreme": (2, 10)
}

def difficulty_set(max_attempts, max_number):
    secret = random.randint(1, max_number)
    attempts = 0
    history = []

    while True:
        try:
            guess = int(input(f"Guess a number(1-{max_number}): "))
        except ValueError:
            print("Please enter a whole number!")
            continue

        if guess <= 0:
            print("Not a zero or negative number!")
            continue

        if guess > secret:
            history.append(guess)
            print("-" * 25)
            print("You're too high!")
            attempts += 1
            print(f"Attempts left: {max_attempts - attempts}")

        elif guess < secret:
            history.append(guess)
            print("-" * 25)
            print("You're too low!")
            attempts += 1
            print(f"Attempts left: {max_attempts - attempts}")

        elif guess == secret:
            attempts += 1
            history.append(guess)
            print(f"{"-" * 25}\nYou guessed the right number! With a {attempts} attempts")
            print(f"History of your attempts:\n{history}")
            break

        if attempts == max_attempts:
            print("You're out of attempts!")
            print(f"{"-" * 25}\nHistory of your attempts:\n{history}")
            print("-" * 25)
            print(f"The secret number was {secret}!")
            break

def play_game():
    while True:
        difficulty = input("Enter difficulty (easy, medium, hard, extreme): ")

        if difficulty in DIFFICULTIES:
            attempts, max_number = DIFFICULTIES[difficulty]
            print("=" * 25)
            print(f"You chose {difficulty.upper()} difficulty!")
            print(f"Max attemps: {attempts}")
            print("-" * 25)

            difficulty_set(attempts, max_number)
            break

        else:
            print("=" * 25)
            print("Please enter a valid difficulty (easy, medium, hard, extreme): ")
            continue
    
play_game()