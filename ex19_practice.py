# define a function to do some math
# I'm trying to find 10 ways to run a function
def my_calc(number1, number2):
    print(f"First, {number1} + {number2} = {number1 + number2}!")
    print(f"Second, {number1} x {number2} = {number1 * number2}!")
    print(f"And that's it! Come back later and maybe you'll get more.\n")

# 1
my_calc(3,5)

# 2
print('Hit enter to run "my_calc"')
input(">")
my_calc(4,5)

# 3
num1 = input('Pick a number: ')
num2 = input('Pick another number: ')
my_calc(int(num1), int(num2))

# 4
print("Pick two numbers")
my_calc(int(input("1st: ")), int(input("2nd: ")))
