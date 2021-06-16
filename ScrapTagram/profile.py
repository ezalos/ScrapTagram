from picture import Picture

class Profile():
	def __init__(self, driver, profile):
		self.driver = driver
		self.profile = profile

	def open(self):
		print(f"Taking care of this profile: {self.profile}")
		self.driver.get(self.profile)
		xpath_posts = "/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span"
		nb_posts = self.driver.find_elements_by_xpath(xpath_posts)[0].text
		print(f"There is {int(nb_posts)} posts")
		xpath_followers = "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span"
		nb_followers = self.driver.find_elements_by_xpath(xpath_followers)[0].text
		print(f"There is {int(nb_followers)} followers")
		xpath_following = "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span"
		nb_following = self.driver.find_elements_by_xpath(xpath_following)[0].text
		print(f"There is {int(nb_following)} following")


	def collect_pic_data(self):
		self.open()
	
# pic 1 1
# /html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a
# pic 1 2
# /html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[2]
# pic 2 1
# /html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[2]/div[1]