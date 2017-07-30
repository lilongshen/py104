people = 40
cars = 30
trucks = 45

# if cars > people
if cars > people:
    print "We should take the cars."
# if cars < people
elif cars < people:
    print "We should not take the cars."
# if cars == people
else:
    print "We can't decide."

# if trucks > cars
if trucks > cars:
    print "That's too many trucks."
# if trucks < cars
elif trucks < cars:
    print "Maybe we could take the trucks."
# if trucks == cars
else:
    print "We still can't decide."

# if people > trucks
if people > trucks:
    print "Alright, let's just take the trucks."
# if people <= trucks
else:
    print "Fine, let's stay home then."

if (cars > people and trucks < cars):
	print "Take cars."
elif (cars > people and trucks > cars):
	print "Take trunks."
else:
	print "Let's stay home."
