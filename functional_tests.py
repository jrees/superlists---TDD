import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool new online to do app
		# she goes to checkout its homepage
		self.browser.get('http://localhosts:8000')


		# she notices the page title and header mention to -do lists
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')
	
if __name__ == '__main__':
	unittest.main(warnings='ignore')

