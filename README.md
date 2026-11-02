# Virtual AI Assistant (Mini Alexa)

Nexbridge Technologies - AI Internship Program, Project 1 (`AI-INT-P1-VAA`).

A text-based, rule-based assistant that runs offline in the terminal using only
the Python 3 standard library. No datasets, APIs, ML libraries or persistence.

## Run

```bash
python3 main.py
```

Run the automated checks (mirrors the PRD acceptance criteria):

```bash
python3 test_assistant.py
```

## Commands

| Command | What it does | PRD |
|---|---|---|
| `hello` | Greets you by name | FR-01/02 |
| `time` / `date` | Current time / date | FR-03/04 |
| `calculate 12 + 8` (or just `12 + 8`) | + - * / with friendly errors | FR-05 |
| `quote` / `joke` / `fact` | Random item from a predefined list | FR-06/07/08 |
| `game` | Number guessing game (1-20, 5 tries, higher/lower hints) | FR-09 |
| `help` | List all commands | FR-10 |
| `exit` / `quit` / `bye` | Quit gracefully | FR-11 |
| anything else | Friendly fallback message | FR-12 |
| `recommend` | Activity suggestion by hour (rule-based decision tree) | FR-13 |
| `perceptron` | Single neuron: inputs, weights, bias, step activation, hidden layer | FR-14 |

## Structure

```
main.py            entry point, main loop, intent routing
greetings.py       name capture and greeting
datetime_utils.py  date and time
calculator.py      parsing and arithmetic
content.py         quotes, jokes, facts
game.py            number guessing game
ai_concepts.py     recommendation + perceptron demos
help_menu.py       help text
test_assistant.py  automated tests
```

## How the AI / ML / DL ideas map to the code

| Concept | Where |
|---|---|
| Rule-based system, keyword detection, intent recognition, pattern matching | `main.py` - `INTENTS`, `detect_intent()` |
| Session memory (name reused in replies) | `greetings.py`, `main.py` |
| Decision tree / classification by if-elif | `ai_concepts.recommend_activity()` |
| Artificial neuron, weights, bias, activation, forward propagation, hidden layer | `ai_concepts.neuron()`, `step_activation()`, `hidden_layer_demo()` |

Nothing is trained: the perceptron's weights are fixed. A real network would
learn them from data.

## Known limitation

Matching is keyword-based, so unusual phrasings fall through to the fallback.
That is expected for a rule-based system.
