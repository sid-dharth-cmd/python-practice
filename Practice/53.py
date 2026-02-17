# map

nums = [1, 2, 3, 4, 5, 6]
square = list(map(lambda x: x**2, nums))
print(square)

# filter

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# reduce

from functools import reduce
product = reduce(lambda x, y: x * y, nums)
print(product)