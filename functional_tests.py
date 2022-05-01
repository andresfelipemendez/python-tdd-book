from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        assert 'To-Do' in self.browser.title

if __name__ == '__main__':
    unittest.main()