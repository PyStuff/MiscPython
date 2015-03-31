# class myDecorator(object):

#     def __init__(self, f):
#         print "inside myDecorator.__init__()"
#         f() # Prove that function definition has completed

#     def __call__(self):
#         print "inside myDecorator.__call__()"

# @myDecorator
# def aFunction():
#     print "inside aFunction()"

# print "Finished decorating aFunction()"

class shoutOut(object):

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print "Woop"
        self.f()
        print "Woop"

class entryExit(object):

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print "Entering", self.f.__name__
        self.f()
        print "Exited", self.f.__name__

print entryExit.__dict__

@entryExit
def func1():
    print "inside func1()"

@shoutOut
@entryExit
def func2():
    print "inside func2()"

# func1()
func2()