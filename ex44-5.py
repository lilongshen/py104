from other import *

class Children(object):

	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print "son override()"

	def alter(self):
		print "before other alter"
		self.other.alter()
		print "after other alter"

son = Children()

son.implicit()
son.override()
son.alter()