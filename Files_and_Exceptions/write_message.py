
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I like programing \n')
    file_object.write('I love creating new games.\n')


def appending_to_file():
    with open(filename, 'a') as file_object:
        file_object.write('appending new line \n')

if '__main__'==__name__:
    print(">>>>>>>>>>>>>>")
    print("appending ")
    print(appending_to_file())

"""
The second argument, 'w', tells Python that we want to open the file in write mode.
You can open a file in read mode ('r'),
write mode ('w'), 
append mode ('a'),
or a mode that allows you to read and write to the file ('r+').
If you omit the mode argument, Python opens the file in read-only mode by default.
"""
