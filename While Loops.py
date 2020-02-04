number = 0
while number < 10:
    print(number)
    number += 1

start = 100
while start > 0:
    print("The number started at {}".format(start))
    start -= 10
    print("The number is now {}".format(start))
    print()

num = 0
while num != 5437:
    num = int(input("Type the number 5437"))
print("YAY!!!☺☻☺☻☺☻☺☻☺☻☺☻←←←←")

name = ""
while len(name) < 4:
    name = input("Enter your full name")

import random  # This only happens once
num = 0
counter = 0
while num != 24:
    num = random.randint(1, 100)
    counter += 1
    print("We got the number: {}".format(num))
print("FINALLY!!!!! We got 24!☺☻☺☻☺☻☺☻☺")
print("It took {} tries to get it".format(counter))

number2 = 0
while number2 != 32:
    try:
        number2 = int(input("Type in 32"))
        if number2 != 32:
            print("Try again")
    except ValueError:
        print("That's not a number.")
print("Yay!")