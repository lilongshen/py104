# define a function, named cheese_and_crackers,has two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# print, using format string
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crakers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# print
print "We can just give the function numbers directly:"
# call cheese_and_crackers()，numbers as arguments.
cheese_and_crackers(20, 30)

# print 
print "OR, we can use variables from our script:"
# give value
amount_of_cheese = 10
amount_of_crackers = 50
# run cheese_and_crackers()，variables as atguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print
print "We can even do math inside too:"
# use cheese_and_crackers()，the sum as arguments
cheese_and_crackers(10 + 20, 5 + 6)

# print
print "And we can combine the two, variables and math:"
# run cheese_and_crackers()，the sum as arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# print
print "From user input:"
# # give input value to variables.
input1 = int(raw_input('> '))
input2 = int(raw_input('> '))

# call cheese_and_crackers()，input as arguments
cheese_and_crackers(input1, input2)

# key strings：int, raw_input(), +, \n, %d, def


