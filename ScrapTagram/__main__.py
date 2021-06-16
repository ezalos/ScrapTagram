from selenium.webdriver.common.by import By
from selenium import webdriver
from config import login
from time import sleep
from profile import Profile
import argparse

url_log = "https://www.instagram.com//sign_in"
url = "https://www.instagram.com/"


class logInInsta():
	def __init__(self, args):
		self.args = args
		self.driver = webdriver.Firefox(".")
		self.driver.get(url)
		self.accept_cookies()
		sleep(3)
		self.site_login()
		sleep(7)
		self.dont_save_info()
		sleep(7)
		self.refuse_notifications()

	def accept_cookies(self):
		# We do accept cookies
		xpath = "/html/body/div[3]/div/div/button[1]"
		for button in self.driver.find_elements_by_xpath(xpath):
			button.click()
			print(f"Grandma has accepted cookies with pleasure")


	def site_login(self):
		self.driver.get(url)
		self.driver.find_element_by_name('username').send_keys(login["user"])
		self.driver.find_element_by_name('password').send_keys(login["password"])
		xpath_login = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button"
		self.driver.find_elements_by_xpath(xpath_login)[0].click()
		print(f"User {login['user']} has been logged!")


	def dont_save_info(self):
		# We dont save info
		xpath_not_now = "/html/body/div[1]/section/main/div/div/div/div/button" 
		for button in self.driver.find_elements_by_xpath(xpath_not_now):
			button.click()
			print("No thanks, we do not wish to save info")


	def refuse_notifications(self):
		xpath = "/html/body/div[4]/div/div/div/div[3]/button[2]" 
		for button in self.driver.find_elements_by_xpath(xpath):
			button.click()
			print("No thanks, we do not wish to have notifications")

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"-x", "--xxxx", help="Exemple argument", type=int, nargs=2)
	args = parser.parse_args()
	log = logInInsta(args)
	eza = "https://www.instagram.com/ezalos/"
	profile = Profile(log.driver, eza)
	profile.collect_pic_data()

