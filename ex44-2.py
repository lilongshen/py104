class Parrent(object):

	def override(self):
		print "print dad"

class Children(parrent):

	def override(self):
		print "print son"

dad = Parrent()
son = Children()

dad.override()
son.override()