# Question 1: Create an empty list
my_list = []

# Question 2: Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Question 3: Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# Question 4: Extend my_list with [50, 60, 70]
my_list.extend([50, 60, 70])

# Question 5: Remove the last element
my_list.pop()

# Question 6: Sort the list in ascending order
my_list.sort()

# Question 7: Find and print the index of the value 30
index_of_30 = my_list.index(30)

print("my_list:", my_list)
print("inserted_list:", my_list[1:])
print("Extended List:", my_list)
print("List after removing last element:", my_list[:-1])
print("Sorted List:", my_list)
print("Index of 30:", index_of_30)
