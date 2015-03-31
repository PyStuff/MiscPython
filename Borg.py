#! /usr/bin/env python

class Singleton(object):

	__instance = None

	def __new__(cls, *args, **kwargs):

		print "hereeee"

		if Singleton.__instance is None:

			# Object wide construction here
			Singleton.__instance = object.__new__(cls)

			# 'test' will be shared with all the Singleton classes
			Singleton.__instance.test = {}

		if 'name' in kwargs:

			Singleton.__instance.test['name'] = kwargs['name']

		if 'val' in kwargs:

			Singleton.__instance.test['val'] = kwargs['val']

		return Singleton.__instance

class lol(Singleton):

	def __new__(self, *args, **kwargs):

		print "In non-singleton new"

	def __init__(self, *args, **kwargs):

		print "In non-singleton init"

	@classmethod
	def __call__ (self):

		print "it worked!"

x = lol('3.0', 3.0)
y = lol('4.0', 4.0)

print x.test

z = lol(name='lol', val=-1.0)
print z.test

print x.test

lol()