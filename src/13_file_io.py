"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

foo_file = open('foo.txt', 'r')
for i in foo_file:
    print(i)
foo_file.close()





# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

content = '''
just checking
that this is
working
'''

# open file to write
bar_file = open('bar.txt', 'w')

# write to file
bar_file.write(content)
bar_file.close()

# check what was written
bar_file = open('bar.txt', 'r')