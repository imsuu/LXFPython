# class Student(object):
# 	"""docstring for Student"""
# 	def get_score(self):
# 		return self._score

# 	def set_score(self,value):
# 		if not isinstance(value,int):
# 			raise ValueError('score must be an integer')
# 		if value < 0 or value > 100:
# 			raise ValueError('score must between 0~100')
# 		self._score = value

# s = Student()
# s.set_score(60)
# print(s.get_score())

# s.set_score(999)

# class Student(object):
# 	"""docstring for Student"""
# 	@property
# 	def score(self):
# 		return self._score
	
# 	@score.setter
# 	def score(self,value):
# 		if not isinstance(value,int):
# 			raise ValueError('score must be an integer')
# 		if value < 0 or value > 100:
# 			raise ValueError('score must between 0~100')
# 		self._score = value

# s = Student()
# s.score = 60
# print(s.score)
# s.score = 999

class Student(object):
	"""docstring for Student"""
	@property
	def birth(self):
		return self._birth
	
	@birth.setter
	def birth(self,value):
		self._birth = value

	@property
	def age(self):
		return self._age
	
