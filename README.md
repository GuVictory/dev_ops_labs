# Python Web Application: Current Time in Moscow

## Description of the project

This is a simple Python web application that displays the current time in Moscow. The application is built using Flask, a lightweight web framework for Python. It provides a single route ("/") that, when accessed, returns the current time in Moscow.

## Instructions

### Setup

1. **Install Python:** If Python is not already installed on your system, download and install it from the [official Python website](https://www.python.org/) following the provided instructions.
2. **Install Dependencies:** Open a terminal or command prompt and navigate to the project directory. Run the following command to install the required dependencies:
    ```shell
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

### Start the Application

1. **Run the Application:** In the terminal or command prompt, navigate to the project directory. Execute the following command to start the application:

    ```shell
    python app.py
    ```

    The Flask application will start running.

2. **Access the Application:** Open a web browser and visit http://localhost:5000. You will see the current time in Moscow displayed on the webpage.

### Run Tests

1. **Execute Tests:** In the terminal or command prompt, navigate to the project directory. Run the following command to execute the tests:

    ```shell
     python tests.py
    ```

    The test runner will execute the tests and display the results, indicating whether they passed or failed.

### Linting

1. **Flake8:** In the terminal or command prompt, navigate to the project directory. Execute the following command to run Flake8 and check for code style and potential errors:

    ```shell
     flake8
    ```

    Flake8 will analyze the Python files in the project directory and display any linting errors or warnings.

2. **Pylint:** In the terminal or command prompt, navigate to the project directory. Run the following command to run Pylint and perform a static analysis of the code:

    ```shell
     pylint app.py
    ```

    Pylint will analyze the specified file and provide feedback on any code issues it finds.
