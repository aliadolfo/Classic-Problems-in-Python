"""
Python’s reduce() is a function that implements 
reduction. reduce() is useful when you need to apply a function,
to an iterable and reduce it to a single cumulative value.
"""

from functools import reduce 
# functools.reduce(function, iterable[, initializer])

def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

numbers = [0,1,2,3,4]

print(">>>>>> ", reduce(my_add, numbers))
"""
This means that the first call to function will use the value of initializer and the first item
of iterable to perform its first partial computation. 
After this, reduce() continues working with the subsequent items of iterable.
"""
print("using a Initializer >>> ", reduce(my_add, numbers, 100))

"""
If you call reduce() with an empty iterable,
then the function will return the value supplied to initializer. 
If you don’t supply an initializer, then reduce() will raise a TypeError when processing empty iterable
"""
