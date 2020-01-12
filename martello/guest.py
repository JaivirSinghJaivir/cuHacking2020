import SystemRandom

class guest:
        def __init__(self,name):
		self.__name = name
		self.__colour = (randint(50,255),randint(50,255),randint(50,255))
		self.__xpos = 200
		self.__ypos = 0

	def xpos(self):
		return self.__xpos

	def ypos(self):
		return self.__ypos

	def new_pos(x,y):
		self.__ypos = y
		self.__xpos = x


	def name(self)
		return self.__name


	def colour(self):
		return self.__colour

	def new_colour(self):
		self.__colour = (randint(50,255),randint(50,255),randint(50,255),randint(50,255))
