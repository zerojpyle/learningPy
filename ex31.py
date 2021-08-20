print("""You enter a dark room with three doors.
Do you go through door #1, #2, or #3?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off.  Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Bluberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The instanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("A mirror of infinite darkness stands before you.")
    print("1. Smash the mirror with an intense stare.")
    print("2. Run through the mirror into the 7th dimension.")

    mirror = input("> ")

    if mirror == "1":
        print("The mirror stares back and absorbs your soul.  You lose!")
    elif mirror == "2":
        print("The 7th dimension welcomes you warmly, but then")
        print("you are stretched out of shape and you die.  You lose!")
    else:
        print("The blackness disappears and you are staring back at yourself.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die.  Good job!")
