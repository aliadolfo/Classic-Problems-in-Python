def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name"""
    if middle:

        full_name = "{first} {middle} {last}".format(first = first, middle = middle, last = last)
    
    else:

        full_name = "{first} {last}".format(first = first, last = last)

    return full_name.title()

if '__main__'==__name__:
    print(">>>>>>>>>>> ", get_formatted_name("ali adolfo", "gonzalez aguilar"))
