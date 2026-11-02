"""Quotes, jokes and facts (FR-06, FR-07, FR-08).

Each feature is a predefined list; random.choice picks one per request.
AI/ML link: picking content by a simple rule is a toy "recommendation".
"""

import random

QUOTES = [
    "The secret of getting ahead is getting started. - Mark Twain",
    "It always seems impossible until it's done. - Nelson Mandela",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "Whether you think you can or you think you can't, you're right. - Henry Ford",
    "Small steps every day add up to big results.",
    "Mistakes are proof that you are trying.",
    "You don't have to be great to start, but you have to start to be great. - Zig Ziglar",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
]

JOKES = [
    "Why did the developer go broke? Because they used up all their cache.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "I would tell you a UDP joke, but you might not get it.",
    "Why was the computer cold? It left its Windows open.",
    "There are 10 kinds of people: those who understand binary and those who don't.",
    "A SQL query walks into a bar, sees two tables and asks: 'Can I join you?'",
    "Why did the neural network cross the road? It was trained to.",
    "How many programmers does it take to change a light bulb? None - that's a hardware problem.",
]

FACTS = [
    "The term 'Artificial Intelligence' was coined by John McCarthy in 1956.",
    "The first computer bug was a real moth found in a Harvard computer in 1947.",
    "The perceptron, an early artificial neuron, was introduced by Frank Rosenblatt in 1958.",
    "Python is named after Monty Python, not the snake.",
    "Honey never spoils - edible honey has been found in ancient Egyptian tombs.",
    "Octopuses have three hearts and blue blood.",
    "A day on Venus is longer than a year on Venus.",
    "The first 1 GB hard drive, in 1980, weighed over 200 kilograms.",
]


def get_random_quote():
    """Return one random motivational quote."""
    return random.choice(QUOTES)


def get_random_joke():
    """Return one random joke."""
    return random.choice(JOKES)


def get_random_fact():
    """Return one random fact."""
    return random.choice(FACTS)
