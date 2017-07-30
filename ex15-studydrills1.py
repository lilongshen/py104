from sys import argv 

# unpack argv
script, filename = argv

# open file, return a file object
txt = open(filename)

# pirnt filename 
print "Here's your file %r:" % filename
# print file content
print txt.read()

# print a statement
print "Type the filename again:"
# input another filename
file_again = raw_input("> ")

#open this file, return a file object
txt_again = open(file_again)

# print this file content
print txt_again.read()