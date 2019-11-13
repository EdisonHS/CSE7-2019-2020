print("Hello World!")

# Congrats! You just made your
# first Python program!

'''
This is a multi-line comment
Everything in between is ignored 
by the program
'''

print(True)
print(15)

print("TRUE")
print(9001)
print('the thing')
# print('the other thing")
# print("Make sure quotes (" close ))
print(7.14)

# ------------
# Math Section
# ------------
print()
print()
print("Math")
print(3 + 4)  # Prints 7
print(4 * 5)  # Prints 20
print(5 - 2)  # Prints 3
print(144 / 12)  # Prints 12

# Powers
print(3 ** 2)  # This should be 3^2
print(2 ** 4)  # This should print 16

print()
# Floor Division
print(9 // 3)  # Prints 3
print(9 // 4)  # Prints 2
print(8 // 3)  # Prints 2
print(12 // 4)  # Prints 3
print(11 // 4)  # Prints 2
print(24 // 5)  # Print 4
print(-8 // 3)  # Prints -3


# ---------
# Data Types
# ---------
print()
print()
print(15)  # Integer
print("seven")  # String
print(9.81)  # Float
print(False)  # Boolean

# Modulus (It's a math thing)
print(14 % 12)  # The answer is 2
print(13 % 12)  # The answer is 1
print(25 % 12)  # The answer is 1
print(7 % 2)
print(14 % 4)
print(5 % 3)

# Mixed Review
print()
print()
print(3 ** 3)  # 27
print(15 // 4)  # 3
print(13 % 4)  # 1
print(18 // 10)  # 1


# -----------
# Variables
# -----------

print()
print()
the_number = 3
print("The number is: ")
print(the_number)
the_number = the_number + 2
the_number = the_number * 100
print("The number is: ")
print(the_number)

print()
screens = 4
screens + 2
print(screens)
# This prints 4
# The "=" is the assignment operator

account = 150
account += 50  # account = account + 50
print(account)

balance = 5000
balance -= 1000
balance *= 2
print(balance)

balance /= 4
print(balance)

seconds = 9999
minutes = seconds // 60
seconds_left = seconds % 60
print("Time remaining:")
print(minutes)
print(seconds_left)

# -----------
# Strings
# -----------
first_word = "yes"
second_word = "pineapple"
third_word = "bruh"

print("The three words we used in class")
print("were", first_word, second_word, third_word)

# If you print things separated by a comma,
# It automatically puts a space in

print()
print("I went to the store and my mother")
print("told me to buy some " + second_word + " and")
print("some " + first_word + ".")

# Concatenation - Adding multiple strings together

first_number = 13
second_number = 564
third_number = 58.9

print("""I'm going to buy {} pizzas, 
{} sodas, and {} bread sticks
""".format(first_number, second_number, third_number))

working = True
question = "Does this work?"
print("My teacher asked, {} The answer is {}.".format(question, working))

print()
# -----------
# Inputs
# -----------
name = input("What is your name? ")
print("Hello {}!".format(name))

age = input("How old are you? ")
print("{}?!?! Wow, you belong in a museum!".format(age))

school = input("Where did you go to elementary school?")
print("I hear {} is pretty nice".format(school))

print("BIO:")
print("Name : {}   Age: {}".format(name, age))
print("Elementary: {}".format(school))


# Recasting

cost = input("How much does it cost?")
cost = int(cost)  # Change it to an integer
cost *= 1.0795  # Sales tax is 7.95%
print(cost)

# to change to a string...
str(51)  # This becomes "51"
print(str(5) + str(8))

print("a" * 100)
print("oh" + "canada" * 10000)


# Review
the_other_number = 15
the_other_number + 3
the_other_number %= 5
print(the_other_number)

adams_moms_weight = 150
adams_moms_weight += 25
adams_moms_weight // 25
adams_moms_weight /= 5
adams_moms_weight = adams_moms_weight ** 2
adams_moms_weight = adams_moms_weight ** (1/2)
print(adams_moms_weight)

# Last few things
drinks = 5
print(drinks == 5)
print(drinks > 3)
print(drinks <= 10)
print(drinks != 15)

# Rounding (the real kind)
number = 5.6862
print("The number is about {:.2f}".format(number))
print("The number is about {:.3f}".format(number))
