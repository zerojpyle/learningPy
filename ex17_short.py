# this is a simplified version of the file copy script
# it may not be 1-line like Zed claims, but it's shorter!
from sys import argv

script, from_file, to_file = argv

indata = open(from_file).read()
outdata = open(to_file, 'w').write(indata)

# not sure if this is the proper way to close a file previously opened
# it may just open them again, then immediately close them
open(from_file).close()
open(to_file).close()
