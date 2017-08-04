class Parrent(object):

	def alter(self):
		print "PARRENT alter"

class Children(parrent):

	def alter(self):
		print "BEFORE PARRENT alter"
		super(children,self).alter()
		print "AFTER PARENT alter"

dad = Parrent()
son = Children()

dad.alter()
son.alter()