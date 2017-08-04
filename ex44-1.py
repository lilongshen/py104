class Parrent(object):

	def implicit(self):
		print "print imlicit()"


class Children(parrent):
	pass

father = Parrent()

son = Children()

father.implicit()
son.implicit()