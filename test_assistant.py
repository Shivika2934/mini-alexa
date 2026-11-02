"""Automated checks mirroring the PRD acceptance criteria. Run: python3 test_assistant.py"""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import ai_concepts, calculator, content, datetime_utils, game, main


def run_session(inputs):
    out = io.StringIO()
    with patch("builtins.input", side_effect=inputs), redirect_stdout(out):
        main.main()
    return out.getvalue()


class Tests(unittest.TestCase):
    def test_name_used_and_exit(self):  # FR-01/02/11
        out = run_session(["priya", "time", "date", "exit"])
        self.assertGreaterEqual(out.count("Priya"), 3)
        self.assertIn("Goodbye, Priya!", out)

    def test_calculator(self):  # FR-05
        self.assertEqual(calculator.respond_calculator("calculate 12 + 8"), "The result is 20")
        self.assertEqual(calculator.respond_calculator("7*6"), "The result is 42")
        self.assertEqual(calculator.respond_calculator("calculate 7 / 2"), "The result is 3.5")
        self.assertEqual(calculator.respond_calculator("calculate -3 + 5"), "The result is 2")
        self.assertIn("divide by zero", calculator.respond_calculator("calculate 5 / 0"))
        self.assertIn("couldn't read", calculator.respond_calculator("calculate abc + 1"))

    def test_random_content(self):  # FR-06/07/08
        for fn in (content.get_random_quote, content.get_random_joke, content.get_random_fact):
            self.assertGreaterEqual(len({fn() for _ in range(40)}), 2)

    def test_datetime(self):  # FR-03/04
        self.assertRegex(datetime_utils.get_current_time(), r"\d{1,2}:\d{2} [AP]M")
        self.assertTrue(datetime_utils.get_current_date().startswith("Today is"))

    def test_game_win_lose_hints(self):  # FR-09
        out = io.StringIO()
        with patch("builtins.input", side_effect=["x", "5", "15", "10"]), redirect_stdout(out):
            self.assertTrue(game.play_guessing_game(secret=10))
        self.assertIn("higher", out.getvalue()); self.assertIn("lower", out.getvalue())
        with patch("builtins.input", side_effect=["1"] * 5), redirect_stdout(io.StringIO()):
            self.assertFalse(game.play_guessing_game(secret=10))

    def test_help_and_fallback(self):  # FR-10/12
        out = run_session(["sam", "help", "asdkfj", "exit"])
        for word in ("time", "date", "calculate", "joke", "quote", "fact", "game", "exit"):
            self.assertIn(word, out)
        self.assertIn("not sure I understood", out)

    def test_recommend_varies(self):  # FR-13
        self.assertNotEqual(ai_concepts.recommend_activity(7), ai_concepts.recommend_activity(13))

    def test_perceptron(self):  # FR-14
        self.assertEqual(ai_concepts.neuron([1, 1, 1])[1], 1)
        self.assertEqual(ai_concepts.neuron([0, 0, 0])[1], 0)
        out = run_session(["sam", "perceptron", "1 0.5 0.2", "perceptron", "a b", "exit"])
        self.assertIn("output = 1", out); self.assertIn("weren't all numbers", out)

    def test_never_crashes(self):
        out = run_session(["sam", "", "???", "calculate", "5 / 0", "ctrl", "exit"])
        self.assertIn("Goodbye", out)

    def test_ctrl_d(self):
        self.assertIn("Goodbye", run_session(["bob"]))  # EOF after name


if __name__ == "__main__":
    unittest.main()
