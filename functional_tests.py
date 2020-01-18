from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Edith found out a new app to manage a todo list
        # She decided to visit the main page for the app
        self.browser.get('http://localhost:8000')

        # She noticed that the page title and header contain word 'Lists'
        self.assertIn('Lists', self.browser.title)
        self.fail('End of test!')

        # She immediately decides to write some stuff

        # In the text view she wrote 'buy peacock feathers' (Edith's hobby
        # is making nice baits

        # After hitting enter the page refreshed and is shows
        # '1: buy peacock feathers' as element of the list

        # There is still a text view to add new items to the list
        # Edith wrote down 'use peacock feathers to make a bait' (Edith is very meticulous)

        # The page reloaded and now it shows two items on the list

        # Edith was curious if her list will be saved and she noticed
        # a unique URL generated for her with a description

        # She went for the URL and found her list

        # Content with results she goes to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
