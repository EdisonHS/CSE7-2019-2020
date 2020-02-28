# Creating a list
groceries = ["milk", "eggs", "bread", "oranges", "milk"]
boring_list = [7, 7, 7, 7, 7, 7, 0]
numbers = [1, 2, 3.5, 12]

# Counting items in a list
length = len(groceries)
print("Our groceries list has {} items".format(length))
length2 = len(boring_list)
length3 = len(numbers)

# Accessing items in a list (we do this by index)
print(groceries[2])
print(groceries[0])  # Index starts at 0 not 1
print(groceries[3])
print(groceries[-1], "has an index of -1")
print(groceries[-2], "has an index of -2")

# Adding items to a list
print(groceries)
groceries.append("Apples")  # Always adds to the END
print(groceries)

groceries.insert(2, "soda")
print(groceries)
print(groceries[5])
# print(groceries[1000])

# Removing items from a list
groceries.remove("milk")  # Only the first "milk" was removed
print(groceries)

groceries.pop(0)  # This removes the item at index 0
print(groceries)

# Finding items in a list
spot = groceries.index("oranges")
print("Oranges are at index {}".format(spot))

print(boring_list)
position = boring_list.index(7)  # This finds only the first one!
print("The number 7 is at index {}".format(position))

groceries.append("oranges")
print(groceries)
print(groceries.count("oranges"))

# Sort the list
print(groceries)
groceries.reverse()  # Python can reverse the order
print(groceries)

print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)

print(groceries)
groceries.sort()
print(groceries)

