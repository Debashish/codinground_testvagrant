from selenium.webdriver.common.by import By
from page_testvagrant import Page
import Conf_Reader, os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Signin_Page(Page):
	def start(self):

		self.url = ""

		self.open(self.url)

		self.wait(2)

		self.trip_link = self.driver.find_element(By.LINK_TEXT, "Your trips")
		self.signin_button = self.driver.find_element(By.ID, "SignIn")

		self.click_element(self.trip_link)
		self.click_element(self.signin_button)

		self.wait(2)

		# Used below ways to jump to modal but couldn't hence redirected to signin page directly

		# self.parent_h = self.driver.current_window_handle
		# self.handles = driver.window_handles
		# print self.handles
		# self.handles.remove(self.parent_h)

		# self.driver.switch_to_window(self.handles.pop())

		self.url = "signin"

		self.open(self.url)


		self.login_email = self.driver.find_element(By.ID, "email")
		self.login_password = self.driver.find_element(By.ID, "password")
		self.submit_button = self.driver.find_element(By.ID, "signInButton")

	def login(self, username, password):

		"login using credentials provided"

		login_flag = False

		self.set_login_email(username)
		self.set_login_password(password)
		self.submit_login()

		title = self.driver.title

		if "Your trips" in title:

			login_flag = True
			self.write("Login success", level = 'debug')
			self.teardown()

		else:

			self.write("Failed: Login error", level = 'debug')
			self.write(" Obtained driver title"+ title, level = 'debug')
			self.teardown()

		return login_flag 

	def set_login_email(self, username):
		"Set the username on login screen"
		self.set_text(self.login_email, username)

	def set_login_password(self, password):
		self.set_text(self.login_password, password)

	def submit_login(self):

		self.click_element(self.submit_button)
		self.wait(5)


if __name__ == '__main__':

	# get the test account credentials from the .credentials file
	credentials_file = os.path.join(os.path.dirname(__file__),'login.credentials')
	username = Conf_Reader.get_value(credentials_file,'LOGIN_USER')
	password = Conf_Reader.get_value(credentials_file,'LOGIN_PASSWORD')
	
	# create a login page object
	driver = webdriver.Firefox()
	login_obj = Signin_Page(driver, base_url = "https://www.cleartrip.com/")

	if (login_obj.login(username, password)):
		msg = "Login was successful"
		login_obj.write(msg)
	else:
		msg = "Login failed"
		login_obj.write(msg)


