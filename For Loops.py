for variable in range(10):
    print("Hello World")

for i in range(20):
    print("Hello World")

for i in range(2, 5):
    print("Computer Science")

for iterator in range(4, 10):
    print("How many times will this print?")

for i in range(8):
    print(200)

for i in range(5):
    print(i)

for i in range(25):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(125, 140):
    print(i + 4)

for i in range(125, 140):
    print("The value of 'i' is: ")
    print(i)
    print("But this value is printed instead: ")
    print(i + 4)
    print()

for i in range(0, 16, 2):
    print(i)

for i in range(1, 17, 2):
    print(i)

for i in range(1, 18, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

# -----------
# Day 2
# -----------
print()
print("Day 2")
print()

total = 0
for i in range(1, 10001):
    total += i
    print("The total so far is {}".format(total))
print("The final total is {}".format(total))

total = 1
for i in range(1, 101):
    total *= i
print(total)

# Divisibility
# Only print the numbers divisible by 2
for i in range(101):
    if i % 2 == 0:
        print(i)

for i in range(101):
    if i % 7 == 0:
        print(i)

for i in range(101):
    if i % 7 == 0 and i % 4 == 0:
        print("{} is divisible by both".format(i))
    elif i % 7 == 0:
        print("{} is divisible by 7".format(i))
    elif i % 4 == 0:
        print("{} is divisible by 4".format(i))
