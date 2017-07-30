print "You want to study using this machine. Do you learn task #1 or task #2?"

task = raw_input("> ")

if task == "1":
	print "You will start to learn English."
	print "1. BBC materials"
	print "2. VOA materials"

	materials = raw_input("> ")

	if materials == "1":
		print "Let's learn British accent."
	elif materials == "2":
		print "Let's learn American accent."
	else:
		print "Sorry, we just have two materials."

elif task == "2":
	print "You will start to learn programming."
	print "1. Python."
	print "2. Javascript."

	language = raw_input("> ")

	if language == "1":
		print "Reading 'Learn python the hard way'."
	elif language == "2":
		print "Reading 'You dont't know JS'."
	else:
		print "Sorry, just two languages to learn."

else:
	print "You don't want to study actually, go fuck yourself."
