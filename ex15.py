# from the sys module, import argv
from sys import argv

# store arguments into two variables
script, filename = argv

# open file with name stored in "filename" into variable "txt"
# open creates a "file object"
txt = open(filename)

# print the file name, and then read the opened file object and print it
print(f"Here's your file {filename}:")
print(txt.read())

# prompt user to type file name again
print("Type the filename again:")
file_again = input("> ")

# using file name by user input, open the file into "txt_again"
txt_again = open(file_again)

# read and then print the file object
print(txt_again.read())
