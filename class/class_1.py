#coding=UTF_8
##第一个class 例程
#

stuff = ["test",'this','out']

print stuff
print ' '.join(stuff)

class thing(object):
	def __init__(self,value=1):
		self.value = value;

	def printf(self):
		print self.value

Something = thing()

Something.printf()

class Athlete(object):
	"""docstring for Athlete"""
	def __init__(self, value ):
		super(Athlete, self).__init__()
		self.value = value
		
	def printf(self):
		print self.value

A_athlete = Athlete(8)

A_athlete.printf()
