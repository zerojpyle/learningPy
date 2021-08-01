from sys import argv

script, input_file = argv

# function to print the entire file
def print_all(f):
    print(f.read())

# function to set the file object to the beginning
def rewind(f):
    f.seek(0)

# function to print a specific line
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

# define the current_line and then pass it to print_a_line function
current_line = 1
print_a_line(current_line, current_file)

# increase current_line and then print it
current_line = current_line + 1
print_a_line(current_line, current_file)

# increase current_line and then print it
current_line = current_line + 1
print_a_line(current_line, current_file)
