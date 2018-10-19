print("[Welcome to RPS]")
x = 0
y = 5
z = 'Loading in 5 seconds...: '
print(z + str(x + y))

while x < 5:
    x = x + 1
    print('Loading... ' + str(x))
print("========================")
age=input("What is your age? ")
print("========================")
print("Your age is: " + str(age))

while int(age) < 18:
    print("You're too young! Try again next year.")
    age=input("How old are you really? ")
else:
    print("Okay you may enter!")
    print("========================")

def rps():
    import random
    x = random.randint(1,3)

    if x < 2:
        print("Computer chose [Paper]")
    elif x == 2:
        print("Computer chose [Scissors]")
    else:
        print("Computer chose [Rock]")

    print("Hey, no cheating!")
    print("========================")

    number = input("Rock, Paper, or Scissors? ")
    print("You selected " + number)

    if number == "Paper":
        number = 1
        print("Let's see if Paper wins...")
    elif number == "Scissors":
        number = 2
        print("Let's see if Scissors wins...")
    elif number == "Rock":
        number = 3
        print("Let's see if Rock wins...")
    else:
        print("That is an invalid selection, please try again. (Case-sensitive)")

    print("========================")

    if x-number == -1 or x-number == 2 :
        print("You win!")
    elif x-number == 1 or x-number == -2:
        print("You lose!")
    else:
        print("Tie!")

def Try_again():
    choice = input("Would you like to try again? y/n ")
    if choice == "y" or choice == "yes" or choice == "Yes":
        rps()
        Try_again()
    elif choice == "n" or choice == "no" or choice == "N":
        print("Thank you for playing!")
    else:
        print("Please input a valid response.")
        Try_again()

rps()
Try_again()


