"""
Practical 04 - Lists Warm-up
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# Expression results
# numbers[0] -> 3
# numbers[-1] -> 2
# numbers[3] -> 1
# numbers[:-1] -> [3, 1, 4, 1, 5, 9]
# numbers[3:4] -> [1]
# 5 in numbers -> True
# 7 in numbers -> False
# "3" in numbers -> False
# numbers + [6, 5, 3] -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# elements of numbers to ten
numbers[0] = "ten"
# last element of numbers to 1
numbers[-1] = 1

# Print all elements except the first two
print(numbers[2:])

# Check if 9 is in the list
print(9 in numbers)
