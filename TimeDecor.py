# Test of decorator for timing routines
import time
import numpy as np
import math as m

print ""

# The time run decorator
def timeRun(count=10000):

	import inspect

	def timeDecorator(func):

		times = np.zeros(count)

		def wrapper(*args, **kwargs):

			print "Starting timed run of " + str(func.__name__) + "..."

			result = None

			for i in range(count):

				start = time.time()

				result = func(*args, **kwargs)

				times[i] = time.time() - start

			# Convert to numpy for analysis
			timesNp = np.asarray(times)

			print "Completed", str(count), "runs in", timesNp.mean() , "seconds with standard deviation " + str(timesNp.std()) + ")\n"

			# Make sure we have the same return value
			return result

		return wrapper

	return timeDecorator


