# tau-intro-selenium-webdriver-with-python

Useful URLs

- [Selenium WebDriver With Pyton](https://testautomationu.applitools.com/selenium-webdriver-python-tutorial/)
- [TAU - Report](https://github.com/AndyLPK247/tau-intro-selenium-py)
- [Beneficial To Have Followed Previously](https://testautomationu.applitools.com/python-tutorial/)
- [Python can be downloaded from Python.Org](https://www.python.org/downloads/)
- [WebDriver API - Read the Docs](https://selenium-python.readthedocs.io/api.html)
- [Waits - Implicit and Explicity](https://selenium-python.readthedocs.io/waits.html)

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

## Chapter 4 - Defining Page Objects

- Create a folder call `pages` at the root of the project creating the below within the folder
  - Create a package called `__init__.py`
  - Create a file call `search.py`
  - Create a file call `result.py`

## Chapter 7 - Confifuring Multiple Browsers

Adding a configuration file at the root of the project, currently it has 2 values

```bash
{
    "browser": "Headless Chrome",
    "implicit_wait": 10
}
```

To enable our tests to read the config file, a fixture is required which means we need to update out `conftest.py` file with the below:

```bash
@pytest.fixture
def config(scope='session'):

    # read the find_element
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert value are acceptable
    assert config['browser'] in ['Firefox', 'Chrom', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    #Return config so it can be used
    return config
```

By default this will run in `Headless Chrome` due to the configuration in the `config.json` configuration file.  

## Chapter 8 - Race Conditions

When running in Firefox, we encountered a failed test, the test tried to check the value of the new title before it had changed - this is known as a `race condition`

```bash
# And the search result title contains "panda"
  # (In this instance - putting this assertion last guarantees that the page title will be ready)
  assert PHRASE in result_page.title()
```

## Chapter 9 - Running Tests In Paralell

First we added more tests to demonstrate how slow it can be waiting for individual tests to run.
To do this we need to add a decorator function

```bash
@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
```

We also need to have `pytest-xdist` installed which can be installed using the command `pipenv install pytest-xdist` in the terminal.

### Commands For Paralell Tests

- `python -m pytest -n 3`

The "-n 3" arguments tells pytest to run 3 tests in parallel. We have 3 example tests, and most machines can handle 3 Web UI tests simultaneously. When the tests run, notice how 3 browser instances open at once - one per test.

#### Run Time

Headless Mode

- Without Parallelisation - `approx 22 seconds`
- With Parallelisation - `approx 8.5 seconds`
