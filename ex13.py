from sys import argv
# read the WYSS (What you should see) section for how to run this
#   NOTE: Run normally, but include additional arguments after script named
#   Example: python3.6 ex13.py first 2nd 3rd
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
