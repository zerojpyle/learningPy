from sys import argv

script, filename = argv

file = open(filename)
txt = file.read()

print("This is what your file says:")
print(txt)

print("What a funny thing for a file to say...")
