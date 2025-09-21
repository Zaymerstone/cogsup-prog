################################################################################
"""
Recommended readings: 
  Chapter on dictionaries: https://automatetheboringstuff.com/3e/chapter7.html 
  Iterating through dictionaries: https://realpython.com/iterate-through-dictionary-python/
"""
################################################################################

"""
Exercise 4.1

Task:
------
Print the sum of the values in the dictionary.
"""

dct = {'a': 3, 'b': 7, 'c': -2, 'd': 10, 'e': 5}

print("Exercise 4.1")

print(sum(dct.values()))

print("---")

"""
Exercise 4.2

Task:
------
Print the key that has the largest value in dct.
"""

print("Exercise 4.2")

print(max(dct, key=dct.get))

print("---")

"""
Exercise 4.3

Task:
------
Create a new dictionary with the squares of all the values in dct.
"""

print("Exercise 4.3")
squared_dct = {}
print(dct)
for key, value in dct.items():
    squared_dct[key] = value **2
    # print(key, value)
print(squared_dct)



print("---")

"""
Exercise 4.4

Task:
------
Print only the keys in dct whose values are even numbers.
"""

print("Exercise 4.4")
for key, value in dct.items():
  if(value % 2 == 0):
    print(key)
  else:
    pass
  

print("---")

"""
Exercise 4.5

Task:
------
Create a new dictionary that swaps the keys and values in dct.
"""

print("Exercise 4.5")

new_dct = {}

for key, value in dct.items():
  new_dct[value] = key
print(new_dct)

print("---")

"""
Exercise 4.6

Task:
------
Count the number of times each letter appears in the string 'ccctcctttttcc'
and print the resulting dictionary.
"""

s = 'ccctcctttttcc'
print("Exercise 4.6")

dicti = {}
for char in s:
    if char in dicti:
        dicti[char] += 1
    else:
        dicti[char] = 1

print(dicti)

print("---")

"""
Exercise 4.7

Task:
------
Given the dictionary of responses_mapping = {'j':'jazz', 'p':'pop'},
and the string responses = 'jjjpjjpppppjj',
print the list of corresponding words.
"""

responses_mapping = {'j':'jazz','p':'pop'}
responses = 'jjjpjjpppppjj'

print("Exercise 4.7")

result = []
for char in responses:
    result.append(responses_mapping[char])
print(result)



print("---")

"""
Exercise 4.8

Task:
------
Merge the following two dictionaries into one:
{'a': 1, 'b': 2} and {'c': 3, 'd': 4}
"""

print("Exercise 4.8")

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
merged = {**d1, **d2}
print(merged)


print("---")

"""
Exercise 4.9

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose keys are sorted alphabetically.
"""

print("Exercise 4.9")

animals = {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9}
sorted_animals = {key: animals[key] for key in sorted(animals)}
print(sorted_animals)


print("---")

"""
Exercise 4.10

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose values appear in increasing order.
"""

print("Exercise 4.10")

animals = {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9}
sorted_items = sorted(animals.items(), key=lambda item: item[1])

sorted_by_values = {}
for k, v in sorted_items:
    sorted_by_values[k] = v

print(sorted_by_values)

print("---")