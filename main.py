"""Mini Alexa - Virtual AI Assistant (entry point).

Core loop: input -> normalize -> keyword match -> respond -> repeat.
This is a rule-based system: every behaviour is an explicit rule written by
the developer, not learned from data.
"""

import re

import ai_concepts
import calculator
import content
import datetime_utils
import game
import greetings
import help_menu

BANNER = "=" * 43

# CONCEPT - keyword detection / intent recognition: each intent is a set of
# trigger words. Order matters: earlier intents win when several match.
INTENTS = [
    ("exit", {"exit", "quit", "bye", "goodbye"}),
    ("help", {"help", "commands", "menu"}),
    ("calculate", {"calculate", "calc", "compute"}),
    ("time", {"time"}),
    ("date", {"date", "today"}),
    ("joke", {"joke", "funny", "laugh"}),
    ("quote", {"quote", "motivate", "motivation", "inspire"}),
    ("fact", {"fact", "facts"}),
    ("game", {"game", "guess", "play"}),
    ("recommend", {"recommend", "suggest", "activity"}),
    ("perceptron", {"perceptron", "neuron"}),
    ("greeting", {"hello", "hi", "hey"}),
]


def normalize(text):
    """Lowercase and strip surrounding spaces so matching is case-blind."""
    return text.lower().strip()


def detect_intent(text):
    """Return the intent name for `text`, or None if nothing matches.

    CONCEPT - pattern matching: split into words and check for trigger words.
    A bare arithmetic expression like '5 + 3' is also treated as a calculation.
    """
    words = set(re.findall(r"[a-z']+", text))
    for intent, triggers in INTENTS:
        if words & triggers:
            return intent
    if calculator.parse_expression(text) is not None:
        return "calculate"
    return None


def respond_fallback():
    """Friendly reply for unrecognized input (FR-12)."""
    return "I'm not sure I understood that - type 'help' to see what I can do."


def handle_command(intent, text, user_name):
    """Run the feature for `intent`; return a string to print (or None)."""
    if intent == "greeting":
        return greetings.respond_greeting(user_name)
    if intent == "time":
        return datetime_utils.get_current_time()
    if intent == "date":
        return datetime_utils.get_current_date()
    if intent == "calculate":
        return calculator.respond_calculator(text)
    if intent == "quote":
        return content.get_random_quote()
    if intent == "joke":
        return content.get_random_joke()
    if intent == "fact":
        return content.get_random_fact()
    if intent == "game":
        game.play_guessing_game()
        return None  # the game prints its own output
    if intent == "recommend":
        return ai_concepts.recommend_activity()
    if intent == "perceptron":
        return ai_concepts.perceptron_demo()
    if intent == "help":
        help_menu.print_help()
        return None
    return respond_fallback()


def end_session(user_name):
    """Print the goodbye message (FR-11)."""
    print(f"Assistant: Goodbye, {user_name}! Have a great day.")


def run_assistant():
    """Main loop."""
    print(BANNER)
    print("MINI ALEXA - VIRTUAL ASSISTANT")
    print(BANNER)

    user_name = greetings.get_user_name()
    print(f"Assistant: {greetings.build_greeting(user_name)}\n")

    while True:
        text = normalize(input("You: "))
        if not text:
            continue
        intent = detect_intent(text)
        if intent == "exit":
            break
        reply = handle_command(intent, text, user_name)
        if reply:
            # Personalise a little (FR-02): address the user on utility replies.
            prefix = f"Sure thing, {user_name}! " if intent in ("time", "date", "calculate") else ""
            print(f"Assistant: {prefix}{reply}")
        print()

    end_session(user_name)
    print(BANNER)


def main():
    """Run the assistant; never let an unexpected error show a traceback."""
    try:
        run_assistant()
    except (KeyboardInterrupt, EOFError):
        print("\nAssistant: Goodbye! (session ended)")
    except Exception as error:  # last-resort guard so the program never crashes
        print(f"\nAssistant: Something went wrong ({error}). Goodbye!")


if __name__ == "__main__":
    main()
