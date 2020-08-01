# A common use case of generators is to work with data streams or large files
# generator expression (also called a generator comprehension)
# csv_gen = (row for row in open(file_name))
# Using yield will result in a generator object. 

# Generate a infinite sequence|

def infinite_sequence():

    num = 0
    while True:
        yield num
        num += 1

for i in infinite_sequence():
    print(i, end = "")
