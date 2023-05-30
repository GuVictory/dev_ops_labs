"""
This module implements a simple Python web application
that displays the current time in Moscow.

The application is built using the Flask framework and provides
a single route ("/") that, when accessed,
returns the current time in Moscow.

Usage:
1. Run the script and access the application through a web browser.
2. The home route ("/") will display the current time in Moscow.

Dependencies:
- Flask: A lightweight web framework for Python.
- datetime: A module for manipulating dates and times in Python.

Author: Your Name
"""

from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/")
def show_current_time():
    """
    Handler function for the home route ("/") that displays the current time in Moscow.

    Returns:
    str: A string message displaying the current time in the format:
    "The current time in Moscow is: <time>".

    Raises:
    None.

    Example:
    >>> show_current_time()
    'The current time in Moscow is: 2023-05-30 14:30:00'
    """
    moscow_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"The current time in Moscow is: {moscow_time}"


if __name__ == "__main__":
    app.run()
