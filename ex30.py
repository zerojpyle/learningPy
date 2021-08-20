people = 30
cars = 40
trucks = 15

# compare whether there are enough cars
if cars > people:
    # if there are more cars than people:
    print("We should take the cars.")
elif cars < people:
    # if there are fewer cars than people:
    print("We should not take the cars.")
else:
    # if neither are true, then:
    print("We can't decide.")

# compare how many trucks vs. cars
if trucks > cars:
    # if there are more trucks than cars:
    print("That's too many trucks.")
elif trucks < cars:
    # if there are fewer trucks than cars:
    print("Maybe we could take the trucks.")
else:
    # if neither are true, then:
    print("We still can't decide.")

# compare whether there are more people than trucks
if people > trucks:
    # if there are more people than trucks:
    print("Alright, let's just take the trucks.")
else:
    # if not, then:
    print("Fine, let's stay home then.")
