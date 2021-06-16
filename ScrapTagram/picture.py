class Picture():
	def __init__(self, driver, url):
		self.driver = driver
		self.url = url
		self.likes = 0
		self.nb_comments = 0
		self.comments = []

	def get_likes(self):
		pass
