
# Decorators are functions that add functionality to an existing funtion, 
# in python whitout changing the structure of the funtion itself.

# Represented by a @decorator_name 

# Examples: 

# decorator function to convert to lowercase
def lowercase_decorator(function):
    def wrapper():
        func = function()
        string_lowercase = func.lower()
        return string_lowercase
    return wrapper

# decorator function to split words
def splitter_decorator(function):
    def wrapper():
        func = function()
        string_split = func.split()
        return string_split
    return wrapper

@splitter_decorator	# this is executed next
@lowercase_decorator	# this is executed first
def hello():
    return 'HELLO World'

def to_string(function):
    def wrapper():
        func = function()
        to_string_from_number = str(func)

        return to_string_from_number
    return wrapper

@to_string
def enter_number():
    return 1991



# output => [ 'hello' , 'world' ]
if '__main__' == __name__:

    print(">>>>>>>>>>>>>>>>>>>>  : ", hello())
    print("<<<<<<<<<<<<<<<<<<<<  : ", enter_number())
    print(">>>>>>>>>>>> type of return in enter_number : ", type(enter_number()) )
    

