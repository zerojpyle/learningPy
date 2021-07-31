from sys import argv

# create variables from argv input
script, filename = argv

# warn that the input file will be erased
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

# Open input file with write access, store to "target" variable
print("Opening the file...")
target = open(filename, 'w')

# erase file
print("Truncating the file.  Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

# get three lines from user input
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# write user input lines on a separate line each
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# close file
print("And finally, we close it.")
target.close()
