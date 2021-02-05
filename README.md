# tau-intro-selenium-webdriver-with-python

Useful URLs

- [Selenium WebDriver With Pyton](https://testautomationu.applitools.com/selenium-webdriver-python-tutorial/)
- [TAU - Report](https://github.com/AndyLPK247/tau-intro-selenium-py)
- [Beneficial To Have Followed Previously](https://testautomationu.applitools.com/python-tutorial/)
- [Python can be downloaded from Python.Org](https://www.python.org/downloads/)
- [WebDriver API - Read the Docs](https://selenium-python.readthedocs.io/api.html)

## Chapter 2 - Setting Up Pytest

- Ensure you have installed `Python` before starting this course, in the terminal run `python --version`.  An install can be found at `Python.Org` or using the above link
- Ensure you have installed `pipenv` to do this, you can run `pipenv --version` in the terminal.  An install can be installed using the command `pip install pipenv`
- Create a virtual environment, run the command in the terminal `pipenv install`
- Activate your shell by running `pipenv shell`, I am running this in Visual Studio Code

Create the test_search file with the content shell shown in the video and run the command `python -m pytest`.
At this point we expect the test to fail with the exception `"Incomplete Test"`

## Chapter 3 - Setting Up Selenium Web Driver

Each test should initialise its own WebDriver Instance and Quit the instances regardless of the outcome.  This ensures test case independence and avoids zombie processes which can affect system resources.

To install Selenium run the command `pipenv install selenium` within the terminal.

To make use of Fixtures we need to create a file within the `tests` folder called `conftest.py`
