def flight_number_and_destination(flight_number, destination):
	print "We take %s airplane." % flight_number
	print "We're about to travel %s." % destination
	print "Have a great time."

print "Running 1:"
flight_number_and_destination(BK202, Dubai)

print "Running 2:"
Num = BK202
Place = Dubai
flight_number_and_destination(Num, Place)

print "Running 3:"
Num = 202
Place = Beijing
flight_number_and_destination(202, Beijing)

print "Running 4:"
Num = 202
Place = Beijing
flight_number_and_destination(202 + 40, Beijing)

print "Running 5:"
input1 = raw_input('> ')
input2 = raw_input('> ')

flight_number_and_destination(input1, input2)

print "Running 6:"
input = raw_input('> ')
Place = Beijing
light_number_and_destination(input, Beijing)

print "Running 7:"
input = int(raw_input('> '))
Place = Beijing
light_number_and_destination(input, Beijing)

print "Running 8:"
input = int(raw_input('> '))
Place = Beijing
light_number_and_destination(input + 20, Beijng)

print "Running 9:"
Num = 202
input = raw_input('> ')

flight_number_and_destination(202, input)

print "Running 10:"
Num = 202
input = raw_input('> ')

flight_number_and_destination(202 + 40, input)



