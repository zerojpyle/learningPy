# prints several statements, including a string appended with another
print("Mary had a little lamb.")
print("It's fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
# print 10 periods
print("." * 10) # what'd that do?

# create 12 variables with a single letter in each
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Add all the above variables together
# watch end = ' ' at the end. try removing it to see what happens
#   end=' ' appears to prevent the output from starting a new line
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
