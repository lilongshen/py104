# Using formatters assign digital value
x = "There are %d types of people." % 10
# Using formatters assign string value
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# print x,y two sentences
print x
print y

# Using formatters raw value
print "I said: %r." % x
# Using formatters assign string value
print "I also said: '%s'." % y

# Using formatters assign boolen value
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# print the combination of two string
print w + e
