"""
What do you think will be on the final?
Syntax
inputs
variables
data types*
Error Analysis
Basic Prints
Math Functions
Exponents
Floor division (//)
Modulus (%)
booleans (>, <, >=, !=, ==, etc)
printing with variables
recasting
Escape Characters****
rounding
keywords (print, input, etc)
concatenation

"""

# Basic prints
print("Hello World")

# Basic Math
print(5 + 3)
print(13241651341 * 2356)
print(155 / 23)

# Exponents
print(52 ** 2)  # This is 52 to the power of 2
print(25 ** (1/2))  # This is the square root of 25

# Floor Division
print(11 // 4)  # This divides and rounds down

# Escape Characters
# THIS IS THE NEW ONE!!!!!!
print("The cow goes \"Moo\"")
print('Welcome to Mr Wiebe\'s class')
print("This is on one line. \nThis is on the other.")
print("\tThis is a tab!")
print("AM\\PM")


print("\tIndent this. \nPrint this on a new line.")

# Rounding
number = 5.29234634354313543246843216546543246
print("This is about {:.2f}".format(number))
print("This is about {:.7f}".format(number))

# Modulus
print(17 % 5)  # 2
print(599 % 100)  # 99

# Booleans
print(5 > 3)  # True
print(5 == 5)  # 5 is equal to 5
print(5 != 6)  # 5 is not equal to 6
print(5 <= 10)  # 5 is less than or equal to 10

# Variables
number = 500
number -= 300
print(number)  # This prints 200

num1 = 890
num1 %= 2
print(num1)  # 0

first_num = 15
second_num = 4
third_num = 12
first_num = third_num - second_num
first_num += 2
third_num -= 7
second_num /= 2
print(first_num)
print(second_num)
print(third_num)

num1 = 13
num2 = 16
num3 = 10
num2 = num1 - num3  # num2 = 3
num2 -= 2  # num2 = 1
num1 += 5  # num1 = 18
num3 //= 2   # num3 = 5
print(num1)  # 18
print(num2)  # 1
print(num3)  # 5

# Prints with variables
num4 = "10"
print(num1)  # 18
print("Num1 is", num1)  # Num1 is 18
print("Num2 is" + str(num2))  # Num2 is1
print("Num3 is {}".format(num3))  # Num3 is 5

# Inputs
on_task = input("Are we on task?")
print(on_task)

# Recasting
age = int(input("How old are you"))
print("Next year, you will be {} years old"
      .format(age + 1))

cost = float(input("How much does it cost?"))
tax = 1.0795  # Sales tax in Fresno is 7.95%
print("The item costs ${:.2f}".format(cost * tax))

# Keywords
"""
These are special keywords
You cannot use these as variable names
(They are also blue!)
print
float
int
input
str
False
True
"""

# Concatenation
thing1 = "a"
thing2 = "b"
print(thing1 + thing2)  # ab

thing3 = "6123"
thing4 = "32416"
print(thing3 + thing4)  # 612332416

print(int("5") + int("15") + 5)  # 25
