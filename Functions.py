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

