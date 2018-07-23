class Animal(object):
	"""docstring for Animal"""
	pass

class Mammal(object):
	"""docstring for Mammal"""
	pass

class Bird(object):
	"""docstring for Bird"""
	pass


class Dog(Mammal,RunnableMixIn):
	"""docstring for Dog"""
	pass

class Bat(Mammal,Flyable):
	"""docstring for Bat"""
	pass

class Parrot(Bird):
	"""docstring for Parrot"""
	pass

class Ostrich(Bird):
	"""docstring for Ostrich"""
	pass
						
class RunnableMixIn(object):
	"""docstring for Runnable"""
	def run(self):
		print('Running...')

class FlyableMixIn(object):
	"""docstring for Flyable"""
	def fly(self):
		print('Flying...')
						
		