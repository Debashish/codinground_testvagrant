from selenium.webdriver.common.by import By
from page_testvagrant import Page
import Conf_Reader, os
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Flight_booking_test(Page):
	def start(self):

		self.url = ""

		self.open(self.url)

		self.wait(2)

		self.driver.find_element(By.ID, "OneWay").click()

		self.elem = self.driver.find_element(By.ID, "FromTag")
		self.set_text(self.elem, "Bangalore")

		self.wait(2)
		self.elems = self.driver.find_element(By.ID, "ui-id-1").find_elements(By.TAG_NAME, "li")
		self.elems[0].click()

		self.elem = self.driver.find_element(By.ID, "ToTag")
		self.set_text(self.elem, "Delhi")

		self.wait(2)
		self.elems = self.driver.find_element(By.ID, "ui-id-2").find_elements(By.TAG_NAME, "li")
		self.elems[0].click()


		self.driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div[1]/table/tbody/tr[3]/td[7]/a").click()

		self.search_btn = self.driver.find_element(By.ID, "SearchBtn").click()

		self.wait(5)

		self.assertTrue(self.is_element_present(By.CLASS_NAME, "searchSummary"))

		self.teardown()

	def is_element_present(self, how, what):
		try: 
			self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e: 
			return False
		return True


if __name__ == '__main__':

	# create a flight booking page object
	driver = webdriver.Firefox()
	booking_obj = Flight_booking_test(driver, base_url = "https://www.cleartrip.com/")

