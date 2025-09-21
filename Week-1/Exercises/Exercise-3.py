################################################################################
"""
Recommended readings: 
  Chapter on lists: https://automatetheboringstuff.com/3e/chapter6.html 
  List comprehension: https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
"""
################################################################################

"""
Exercise 3.1

Task:
------
Write code that prints the sum of the elements in the following list.
[1, 4, -6, 7, 2, 3, 9, 11, 6]
"""

lst = [1, 4, -6, 7, 2, 3, 9, 11, 6] # In all exercises in this script, you will work with this list

print("Exercise 3.1")

print(sum(lst))

print("---")

"""
Exercise 3.2

Task:
------
Print the product of the elements in the list.
"""

print("Exercise 3.2")

product = 1

for i in range(len(lst)):
  product = product * lst[i] 
print(product)
print("---")

"""
Exercise 3.3

Task:
------
Print the sum of the squares of the list.
"""

print("Exercise 3.3")

sum_value = 0
for i in range(len(lst)):
  squared_value = lst[i] * lst[i]
  sum_value = sum_value + squared_value
print(sum_value)
print("---")

"""
Exercise 3.4

Task:
------
Print the largest element of the list.
"""

print("Exercise 3.4")

print(max(lst))


print("---")

"""
Exercise 3.5

Task:
------
Print the largest element of the list.
"""

print("Exercise 3.5")

# I suppose task was to print out the minimum element of the list
# Here is the code for minimum element of the list:
# print(min(lst))

# In case task is to print largest element of the list, exactly like previous exercise
# then here is another solution:
find_max = 0
for i in range(len(lst)):
  if(lst[i] > find_max):
    find_max = lst[i]
  elif(lst[i] < find_max):
    pass
print(find_max)
print("---")