"""Number guessing game (FR-09)."""

import random

MIN_NUMBER = 1
MAX_NUMBER = 20
MAX_ATTEMPTS = 5


def play_guessing_game(secret=None):
    """Run one game. `secret` can be passed in for testing; otherwise random.

    Returns True if the player won, False otherwise.
    """
    if secret is None:
        secret = random.randint(MIN_NUMBER, MAX_NUMBER)

    print(f"Assistant: I'm thinking of a number between {MIN_NUMBER} and "
          f"{MAX_NUMBER}. You have {MAX_ATTEMPTS} tries.")

    attempts = 0
    while attempts < MAX_ATTEMPTS:
        raw = input("Guess a number: ").strip()
        try:
            guess = int(raw)
        except ValueError:
            # Invalid input does not use up an attempt.
            print(f"Assistant: Please enter a whole number "
                  f"({MIN_NUMBER}-{MAX_NUMBER}).")
            continue

        attempts += 1
        left = MAX_ATTEMPTS - attempts
        if guess == secret:
            print(f"Assistant: You got it in {attempts} "
                  f"{'try' if attempts == 1 else 'tries'}!")
            return True
        hint = "higher" if guess < secret else "lower"
        if left:
            print(f"Assistant: Go {hint}! {left} "
                  f"{'try' if left == 1 else 'tries'} left.")

    print(f"Assistant: Out of tries! The number was {secret}.")
    return False
