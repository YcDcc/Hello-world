from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notice the page tile and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)

        # She is invited to enter a to-do item straigh away
        self.fail('Finsh the tset!')

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')