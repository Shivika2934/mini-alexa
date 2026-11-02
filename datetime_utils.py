"""Date and time reporting (FR-03, FR-04) using the datetime module."""

from datetime import datetime


def get_current_time():
    """Return the current time as a friendly sentence, e.g. 3:45 PM."""
    now = datetime.now()
    # %I is 01-12; lstrip("0") removes the leading zero ("03:45" -> "3:45").
    return f"It's currently {now.strftime('%I:%M %p').lstrip('0')}."


def get_current_date():
    """Return today's date as a friendly sentence."""
    today = datetime.now()
    return f"Today is {today.strftime('%A, %d %B %Y')}."
