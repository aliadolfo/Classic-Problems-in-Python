employees = {'Alice' : 100000,
             'Bob' : 99817,
             'Carol' : 122908,
             'Frank' : 88123,
             'Eve' : 93121}

top_earners = []


# The items() method return a view object.
# that contains key-value pairs of the dictionary
# as a tuple in a list
for key, val in employees.items():
    if val >= 100000:
        top_earners.append((key, val))

print(top_earners) # [('Alice', 100000), ('Carol', 122908)]


# List Comprehension

list_earners = [(k, v) for k, v in employees.items() if v >= 100000]

print(list_earners)
