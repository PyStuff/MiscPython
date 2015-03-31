
def Singleton(klass):

	class Decorated(klass):

		def __init__(self, *args, **kwargs):

			if hasattr(klass, '__init__'):
				klass.__init__(self, *args, **kwargs)

		def __str__(self): return klass.__name__ + " obj."

	Decorated.__name__ = klass.__name__

	class ClassObject:

		def __init__(cls):
			cls.instance = None

		def __str__(self): return klass.__name__

		def __call__(cls, *args, **kwargs):

			if not cls.instance:

				cls.instance = Decorated(*args, **kwargs)

			return cls.instance

	return ClassObject()

@Singleton
class Test:

	@property
	def var(self):
		return self._var

	@var.setter
	def var(self, value):
		self._var = value


a = Test()
# a = Test(3.0)
a.x = 1
a.y = {'2': 2.0}

b = Test()
print b.__dict__

@Singleton
class Colour:

	def __init__ (self, high, low):

		# Lightest colour
		self.high = high

		# Darkest colour
		self.low = low

		# Incremental colour change
		self.stepinr = [int((self.high[x] - self.low[x]) / 180) for x in range(3)]

	def NightFall(self, time):

		# Total darkness
		if time <= 360:
			return self.low
		# Sunrise
		elif time <= 540:
			return [self.low[x] + (time - 361) * self.stepinr[x] for x in range(3)]
		# Total sunshine
		elif time <= 1200:
			return self.high
		# Sunset
		elif time <= 1380:
			return [self.high[x] - (time - 1201) * self.stepinr[x] for x in range(3)]
		else:
			return self.low

MyColour  = Colour([0, 0, 0], [100, 100, 100])
MyColour2 = Colour([0, 0, 0], [200, 200, 200])

print MyColour2.low

# Potential singleton instances in a game?
# Clock, 'World'