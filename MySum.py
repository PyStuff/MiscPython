import TimeDecor

# How to decorate a method
# @TimeDecor.timeRun(count=10000000)
def Sum(x, y):

	return x + y

# This is now to decorate on-the-fly
NewSum = TimeDecor.timeRun(count=10000000)(Sum)

print NewSum(3, 4.0)