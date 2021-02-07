"""
This module containt DuckDuckGoSearchPage, the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage:

    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        # TODO
        pass

    def search(self, phrase):
        # TODO
        pass