import sys


nums_squared_lc = [num**2 for num in range(10000)]
print(sys.getsizeof(nums_squared_lc))

nums_squared_gc = (num**2 for num in range(10000))
print(sys.getsizeof(nums_squared_gc))


# for number in nums_squared_gc:
#     print(number)
