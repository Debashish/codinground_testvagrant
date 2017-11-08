from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from base_logging import Base_Logging
import unittest, time, logging

class Page(unittest.TestCase):
	""" Page class that all page models can inherit from
	"""

	def __init__(self, selenium_driver, base_url='https://www.cleartrip.com/'):

		if base_url[-1] != '/':

			base_url += '/'
		self.base_url = base_url
		self.driver = selenium_driver

		self.start()

		self.log_obj = Base_Logging(level= logging.DEBUG)

	def open(self, url):

		url = self.base_url+url
		self.driver.get(url)


	def click_element(self, elem):

		""" Click the button supplied """
		link  = elem
		if link is not None:

			try:
				link.click()
			except Exception as e:

				self.write('Exception while clicking the elem: %s'%elem)
				self.write(e)
			else:
				return True
		else:

			return False

	def write(self, msg, level='info'):
		self.log_obj.write(msg, level)

	def wait(self, wait_seconds=5):
		"Performs wait for time provided"
		time.sleep(wait_seconds)

	def set_text(self, elem, value):

		"Set the value of text field"

		text_field = elem
		try:
			text_field.clear()
		except Exception as e:
			self.write('Error: could not clear the text field: %s' %xpath)

		if value is None:
			return
		else:
			text_field.send_keys(value)

	def teardown(self):
		" Tears down the driver"
		self.driver.close()




