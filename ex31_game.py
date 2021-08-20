print("You are in the woods with no one around. What do you do first?")
print("1. Go forward into the darkness.")
print("2. Turn around and leave back to civilization.")

choice = input("> ")

if choice == "1":
    print("You are very brave. You find yourself in a meadow.")
    print("1. Look around carefully.")
    print("2. Run into the grass and roll around.")

    meadow = input("> ")

    if meadow == "1":
        print("Good thing you looked! A hungry wolf is hiding in the grass!")
        print("1. Use your bow and arrow to shoot the wolf.")
        print("2. Sneak up behind the wolf and jump on it.")

        wolf = input("> ")

        if wolf == "1":
            print("As you draw the arrow back, the wolf sees you.")
            print("It pounces on you and eats you alive!")
        elif wolf == "2":
            print("The wolf is asleep and you walk carefully up.")
            print("You pounce and choke the wolf to death. Good job!")
            print("1. Take a nap.")
            print("2. Keep going. It's too scary here.")

            next = input("> ")

            if next == "1":
                print("You fall asleep quickly. Another wolf attacks you. You die!")
            elif next == "2":
                print("You find a cabin full of treasure. You win!")
            else:
                print("That's the worst idea I've heard in a long time.")
                print("A rock falls from the sky and crushes you!")
        else:
            print("Where are you going? The wolf hears you and claws your eyes out!")
    elif meadow == "2":
        print("You somersault into the grass without a care.")
        print("But then a wolf jumps on you and eats you alive. You're dead!")
    else:
        print("Why would you do that? A tree fell on you. You're dead!")
elif choice == "2":
    print("What a coward. As you step away, a car hits you and you die!")
else:
    print("A sinkhole swallowed you up. I'm not sure why you did that. You're dead!")
