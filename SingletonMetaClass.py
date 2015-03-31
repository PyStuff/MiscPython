
class SingletonMC(type):

	def __init__(cls, name, bases, dict):

		original_new = cls.__new__

		def myNew(cls, *args, **kwds):

			# If this is the first time we've instantiated a class
			if cls.instance == None:

				cls.instance = original_new(cls, *args, **kwds)

			return cls.instance

		cls.instance = None

		# Make our __new__ the default one
		cls.__new__ = staticmethod(myNew)

class Character(object): pass

class Hero(Character): pass

class Enemy(Character): pass

class World(object):

	__metaclass__ = SingletonMC

	__heroes  = []
	__enemies = []

	def __init__(self, Name=None):

		if not Name:

			self.Name = Name

	def __iadd__(self, other):

		assert isinstance(other, Character), "ERROR!  Can't add non-Character type to World..."

		if   isinstance(other, Hero):  World.__heroes.append(other)
		elif isinstance(other, Enemy): World.__enemies.append(other)

		return self

	def __str__(self): return "\nHeroes:  " + self.__heroes.__str__() + "\nEnemies: " + self.__enemies.__str__()

	# Getters
	def Heroes (self): return self.__heroes

	def Enemies(self): return self.__enemies

	# Contained classes
	class Level(object):

		def readMap(self): pass

		def saveMap(self): pass
