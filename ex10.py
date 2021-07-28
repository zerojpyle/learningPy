tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Practice escape character "\b"
test = "{}{}{}{}"
print(test.format('test','\b','\b','?'))
print(test.format('test','\b','','?'))
print(test.format('test','1','2','3'))
print(test.format('test','\b\b\b\b','?','?'))
print('...^...^...^...^')
