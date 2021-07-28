print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# Additional practice
print("How many quarters do you have?", end=' ')
quarters = int(input())
print("How many dimes do you have?", end=' ')
dimes = int(input())
print(f"You have {.25 * quarters + .1 * dimes} cents.")
