"""Greeting logic and name capture (FR-01, FR-02).

AI/ML concept: the stored name is "session memory" - the assistant keeps a
value in a variable and reuses it, loosely echoing how a model reuses
learned parameters.
"""

ASSISTANT_NAME = "Mini Alexa"
DEFAULT_USER_NAME = "friend"  # Used if the user enters nothing.


def get_user_name():
    """Ask the user for their name and return it (title-cased)."""
    print(f"Assistant: Hi! I'm {ASSISTANT_NAME}. What's your name?")
    name = input("You: ").strip()
    return name.title() if name else DEFAULT_USER_NAME


def build_greeting(user_name):
    """Return the welcome message shown after the name is captured."""
    return f"Nice to meet you, {user_name}! Type 'help' to see what I can do."


def respond_greeting(user_name):
    """Reply to a casual 'hello' / 'hi' typed during the session."""
    return f"Hello again, {user_name}! How can I help?"
