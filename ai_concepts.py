"""AI / ML / DL concept demonstrations (FR-13, FR-14).

Nothing here is trained: it is plain Python that makes the ideas visible.
"""

from datetime import datetime


def recommend_activity(hour=None):
    """Recommend an activity from the hour of day (0-23).

    CONCEPT - rule-based decision making / simple decision tree:
    the if/elif chain below is a tiny decision tree. The "feature" is the
    hour and the "label" it predicts is an activity - the same shape as a
    classifier assigning an input to one of several categories.
    """
    if hour is None:
        hour = datetime.now().hour

    if 5 <= hour < 9:
        label = "Time for a healthy breakfast and a stretch."
    elif 9 <= hour < 12:
        label = "Prime focus time - tackle your hardest task now."
    elif 12 <= hour < 14:
        label = "It's lunch time - take a proper break."
    elif 14 <= hour < 17:
        label = "Good time for a walk or a light, creative task."
    elif 17 <= hour < 20:
        label = "Wind down with some exercise or cooking dinner."
    elif 20 <= hour < 23:
        label = "Relax, read, or review what you learned today."
    else:
        label = "It's late - time to rest and recharge."
    return f"(Hour {hour}) {label}"


# --- Perceptron demo -------------------------------------------------------
# Fixed, hand-picked parameters. A real network would LEARN these from data.
WEIGHTS = [0.6, 0.3, 0.1]
BIAS = -0.5


def step_activation(value):
    """CONCEPT - activation function: output 1 if value > 0, else 0."""
    return 1 if value > 0 else 0


def neuron(inputs, weights=WEIGHTS, bias=BIAS):
    """CONCEPT - artificial neuron / forward propagation.

    inputs -> multiply by weights -> add bias -> activation -> output.
    Returns (weighted_sum_plus_bias, output).
    """
    total = sum(x * w for x, w in zip(inputs, weights)) + bias
    return total, step_activation(total)


def hidden_layer_demo(inputs):
    """CONCEPT - layering: feed the first neuron's output into a second one."""
    _, first_out = neuron(inputs)
    second_total, second_out = neuron([first_out], weights=[1.0], bias=-0.5)
    return first_out, second_total, second_out


def perceptron_demo():
    """Ask for 2-3 numbers, run them through one neuron, explain each step."""
    print("Assistant: Perceptron demo - history's simplest neural network unit.")
    print(f"Assistant: Fixed weights = {WEIGHTS}, bias = {BIAS}")
    raw = input("Enter 2 or 3 numbers separated by spaces (0-1 works well): ")
    try:
        inputs = [float(x) for x in raw.split()]
    except ValueError:
        return "Those weren't all numbers - try again with e.g. 1 0.5 0.2"
    if not 2 <= len(inputs) <= 3:
        return "Please give me 2 or 3 numbers."

    total, out = neuron(inputs)
    steps = []
    for x, w in zip(inputs, WEIGHTS):
        steps.append(f"{x:g} x {w} = {x * w:.2f}")
    first, _, second = hidden_layer_demo(inputs)
    return (
        "Inputs x weights:  " + ",  ".join(steps) + "\n"
        f"Weighted sum + bias ({BIAS}) = {total:.2f}\n"
        f"Step activation (sum > 0 ? 1 : 0) -> output = {out}\n"
        f"Hidden layer: neuron 1 output {first} feeds neuron 2 -> {second}\n"
        "Note: nothing was learned - training would adjust the weights for you."
    )
