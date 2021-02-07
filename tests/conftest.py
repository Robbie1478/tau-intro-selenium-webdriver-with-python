"""
This module contains shared fixtures
"""

import json
import pytest
import selenium.webdriver

@pytest.fixture
def config(scope='session'):

    # read the find_element
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert value are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    #Return config so it can be used
    return config

@pytest.fixture
def browser(config):
    # Initialse the ChromeDriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')
        
    # Makes its calls wait up to 10 seconds for elements to appear before timing out
    b.implicitly_wait(config['implicit_wait'])

    # Returns the WebDriver instance for setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()