# this is a simplified version of the file copy script
# it may not be 1-line like Zed claims, but it's shorter!
from sys import argv

script, from_file, to_file = argv

# I just learned that if a file is opened and read in one line,
# it doesn't need to be closed!
indata = open(from_file).read()
outdata = open(to_file, 'w').write(indata)
