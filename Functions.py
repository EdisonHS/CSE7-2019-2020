def say_hi():
    print("Hello")


say_hi()
say_hi()


def create_divide():
    print()
    print("-----------------------------------")
    print()


create_divide()


def party(cheese, crackers):
    print("We have {} blocks of cheese and {} "
          "boxes of crackers".format(cheese, crackers))


party(15, 20)
party(10, 30)
party(7, 5)
party(15 * 4, 200 - 50)


def add_stuff(num1, num2):
    print("{} + {}". format(num1, num2))
    answer = num1 + num2
    print("The answer is {}".format(answer))


# print(answer)
# This is a local variable
# It only exists inside of the function

def subtract(num1, num2):
    print("SUBTRACTING {} and {}".format(num1, num2))
    return num1 - num2


age = subtract(10, 2)
print(age)


def f(x):
    return x**2 + 3*x + 9


print(f(43))
print(f(750))
print(f(53768435768468768768654676546765767637))


def divisible_by_56435(number):
    if number % 56435 == 0:
        return True
    return False


def divisible_by_2(number):
    return number % 2 == 0


for i in range(1000000):
    if divisible_by_2(i) and divisible_by_56435(i):
        print(i)


def can_sleep_in(weekday, vacation):
    """This function returns true if we can sleep in"""
    if vacation:
        return True
    elif not weekday:
        return True
    return False

# Alternate Answer
#     if  vacation or not weekday:
#         return True
#     return False
