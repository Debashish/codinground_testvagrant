from selenium.webdriver.common.by import By
from page_testvagrant import Page
import Conf_Reader, os
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Hotel_booking_test(Page):
	def start(self):

		self.url = ""

		self.open(self.url)

		self.wait(2)

		self.hotel_link = self.driver.find_element(By.XPATH, "//ul[@class='navGroup productNav withArrows']/li[2]/a")
		self.click_element(self.hotel_link)
		self.locality = self.driver.find_element(By.ID, "Tags")
		self.select = Select(self.driver.find_element(By.ID, "travellersOnhome"))
		self.search_btn = self.driver.find_element(By.ID, "SearchHotelsButton")

	def book_hotel(self, locality, traveller):

		login_flag = False

		self.set_locality(locality)
		self.set_traveller(traveller)
		self.set_date()
		self.submit()

		title = self.driver.title

		if "Book Cheap Hotels" in title:

			login_flag = True
			self.write("Booking success", level = 'debug')
			self.teardown()

		else:

			self.write("Failed: Booking error", level = 'debug')
			self.write(" Obtained driver title"+ title, level = 'debug')
			self.teardown()

		return login_flag 

	def set_locality(self, locality):
		"Set the locality on search screen"
		self.locality.send_keys(locality)
		self.wait(2)
		self.driver.find_element(By.XPATH, "//ul[@id='ui-id-1']/li[1]").click()
		

		

	def set_traveller(self, traveller):
		self.select.select_by_visible_text(traveller)

	def submit(self):
		self.click_element(self.search_btn)
		self.wait(5)

	def set_date(self):

		self.datepicker = self.driver.find_element(By.ID, "CheckInDate")
		self.click_element(self.datepicker)
		self.wait(2)
		self.from_day = self.driver.find_element(By.XPATH, "//div[@class='monthBlock first']/table/tbody/tr[2]/td[6]/a")
		self.click_element(self.from_day)
		self.to_day = self.driver.find_element(By.XPATH, "//div[@class='monthBlock last']/table/tbody/tr[2]/td[5]/a")
		self.click_element(self.to_day)


if __name__ == '__main__':

	locality = "Indiranagar, Bangalore"
	traveller = "1 room, 2 adults"
	
	# create a booking page object
	driver = webdriver.Firefox()
	booking_obj = Hotel_booking_test(driver, base_url = "https://www.cleartrip.com/")

	if (booking_obj.book_hotel(locality, traveller)):
		msg = "Booking was successful"
		booking_obj.write(msg)
	else:
		msg = "Booking failed"
		booking_obj.write(msg)


