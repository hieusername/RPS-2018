def user_input():
    choose1 = input("Choose a number... ")
    choice1 = float(choose1)
    decision = input("What would you like to do? a/s/m/d: ")
    while decision != "a" and decision != "s" and decision != "m" and decision != "d":
        decision = input("Try again... ")

    choose2 = input("Choose another number... ")
    choice2 = float(choose2)

    if decision == "a":
        print("Result: " + str(choice1 + choice2))
    elif decision == "s":
        print("Result: " + str(choice1 - choice2))
    elif decision == "m":
        print("Result: " + str(choice1 * choice2))
    else:
        print("Result: " + str(choice1 / choice2))

user_input()

