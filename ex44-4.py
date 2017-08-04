class Parrent(object):

	def implicit(self):
		print "parrent implicit()"

	def override(self):
		print "parrent override()"

	def alter(self):
		print "parrent alter()"


class Children(parrent):

	def override(self):
		print "childern override()"

	def alter(self):
		print "before parrent alter"
		super(children,self).alter()
		print "alter parrent alter"


dad = Parrent()
son = Children()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.alter()
son.alter()