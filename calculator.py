"""Basic calculator (FR-05).

Supports: +  -  *  /  (also x for multiply) on two numbers, e.g.
"calculate 12 + 8" or "5 * 3". Never raises on bad input.
"""

OPERATORS = ("+", "-", "*", "/", "x")


def parse_expression(text):
    """Extract (num1, operator, num2) from free-form text.

    Returns a tuple of (float, str, float), or None if the text does not
    contain a valid "number operator number" pattern.
    """
    # Drop the trigger word so "calculate 12 + 8" -> "12 + 8".
    for trigger in ("calculate", "calc", "compute"):
        text = text.replace(trigger, "")
    text = text.strip()

    # Allow both "12 + 8" and "12+8" by padding operators with spaces.
    # A '-' directly after another operator or at the start is a negative sign.
    spaced = ""
    for i, ch in enumerate(text):
        is_sign = ch == "-" and (i == 0 or text[i - 1] in OPERATORS + (" ",)) \
            and (i + 1 < len(text) and (text[i + 1].isdigit() or text[i + 1] == "."))
        if ch in OPERATORS and not is_sign:
            spaced += f" {ch} "
        else:
            spaced += ch
    parts = spaced.split()

    if len(parts) != 3 or parts[1] not in OPERATORS:
        return None
    try:
        return float(parts[0]), parts[1], float(parts[2])
    except ValueError:
        return None


def calculate(num1, operator, num2):
    """Apply the operator to two numbers; returns a number or an error string."""
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator in ("*", "x"):
        return num1 * num2
    if operator == "/":
        if num2 == 0:
            return "I can't divide by zero - try a different number."
        return num1 / num2
    return "Sorry, I don't know that operator."


def format_number(value):
    """Show 20.0 as 20 but keep 2.5 as 2.5."""
    return str(int(value)) if value == int(value) else str(round(value, 6))


def respond_calculator(text):
    """Full calculator flow: parse -> calculate -> sentence. Never crashes."""
    parsed = parse_expression(text)
    if parsed is None:
        return ("I couldn't read that calculation. "
                "Try something like: calculate 12 + 8")
    result = calculate(*parsed)
    if isinstance(result, str):  # an error message
        return result
    return f"The result is {format_number(result)}"
