"""Help menu (FR-10)."""

COMMANDS = [
    ("hello", "say hello"),
    ("time", "show current time"),
    ("date", "show current date"),
    ("calculate", "do a calculation, e.g. calculate 12 + 8"),
    ("joke", "tell a joke"),
    ("quote", "motivational quote"),
    ("fact", "random fact"),
    ("game", "play number guessing game"),
    ("recommend", "activity suggestion for this time of day (rule-based AI)"),
    ("perceptron", "single artificial neuron demo (deep learning idea)"),
    ("help", "show this menu"),
    ("exit", "quit the assistant (also: quit, bye)"),
]


def print_help():
    """Print every supported command with a one-line description."""
    print("Assistant: Here is what I can do:")
    for command, description in COMMANDS:
        print(f"  - {command:<11} {description}")
