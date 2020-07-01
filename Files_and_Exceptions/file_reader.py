with open('pi_digits.txt') as file_object:
    contents = file_object.read()


def not_whitespace():
    with open('pi_digits.txt') as file_object:
        pi_string = ''
        lines = file_object.readlines()
        for line in lines:
            pi_string += line.strip()
        print(pi_string)
        print("$ Len >>>> : ", pi_string)

if '__main__'==__name__:
    print("# contents : ", contents.rstrip())
    print("-------")
    print("not Whiteespace : ", not_whitespace())

"""
Recall that Python’s rstrip() method removes, or strips,
any whitespace characters from the right side of a string. 
"""
