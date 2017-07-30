def numbers(max_num):
	i = 0
	numbers = []
	while i < max_num:
	    print "At the top i is %d" % i
	    numbers.append(i)

	    i = i + 1
	    print "Numbers now: ", numbers
	    print "At the bottom i is %d" % i
	return numbers

number = numbers(7)

print "The numbers: "

for num in number:
    print num
