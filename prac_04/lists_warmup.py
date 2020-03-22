
numbers = [3, 1, 4, 1, 5, 9, 2]

# What values do the following expressions have?
# (solutions not provided; figure it out, then run with print or in console to test)
numbers[0]  #produces the number 3
numbers[-1] #produces the numebr 2
numbers[3]  #produces the number 1
numbers[:-1] # produces [3, 1, 4, 1, 5, 9]
numbers[3:4] # produces [1]
5 in numbers # true
7 in numbers # false
"3" in numbers # false
numbers + [6, 5, 3] # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Write Python expressions (in your Python file) to achieve the following:

# Change the first element of numbers to "ten"
numbers[0] = "ten"
print(numbers)
# Change the last element of numbers to 1
numbers[-1] = 1
print(numbers)
# Get all the elements from numbers except the first two
numbers[2:]
print(numbers[2:])
# Check if 9 is an element of numbers
9 in numbers
print(9 in numbers)