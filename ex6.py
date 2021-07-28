# define variable with a number
types_of_people = 10
# define a variable as a literal string
x = f"There are {types_of_people} types of people."

# define a couple strings as variables
binary = "binary"
do_not = "don't"
# define a variable as a literal string
y = f"Those who know {binary} and those who {do_not}."

# print x & y literal strings
print(x)
print(y)

# print more literal strings directly, with embedded literal strings x & y
print(f"I said: {x}")
print(f"I also said: '{y}'")

# define a variable with a boolean
hilarious = False

# define a variable with a string
joke_evaluation = "Isn't that joke so funny?! {}"

# print the variable, adding the boolean that's formatted to be a string
print(joke_evaluation.format(hilarious))

# define more strings
w = "This is the left side of..."
e = "a string with a right side."

# combine and then print two strings
print(w + e)
