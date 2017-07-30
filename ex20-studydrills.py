from sys import argv
# unpack
script, input_file = argv

# define a function
def print_all(f):
	# print all content
    print f.read()

# define a function
def rewind(f):
	# look for original position
    f.seek(0)

# define a function
def print_a_line(line_count, f):
	# print line number and content of each line 
    print line_count, f.readline()

# documents object
current_file = open(input_file)

# print
print "First let's print the whole file:\n"

# call func print_all()
print_all(current_file)

# print
print "Now let's rewind, kind of like a tape."

# call func rewind()
rewind(current_file)

# print three lines:
print "Let's print three lines:"

for current_line in range(1,4):
	print_a_line(current_line, current_file)





