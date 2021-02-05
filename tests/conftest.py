"""
This module contains shared fixtures
"""

import pytest
import selenium.webdriver

@pytest.fixture
def browser():
    # Initialse the ChromeDriver instance
    b = selenium.webdriver.Chrome()

    # Makes its calls wait up to 10 seconds for elements to appear before timing out
    b.implicitly_wait(10)

    # Returns the WebDriver instance for setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()