def loopy(mynum,inc):
    i = 0
    numbers = []

    while i < mynum:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + inc
        print("Numbers now: ", numbers)
        print(f"At the bottim i is {i}")

        print("The numbers: ")

        for num in numbers:
            print(num)

print("Give me a number to count to:")
number = int(input("> ")) + 1
print("What should I count by?")
increment = int(input("> "))
loopy(number,increment)
