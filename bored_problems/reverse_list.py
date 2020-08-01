

def reverse_object(list):

    reversed_list = []
    counter = len(list)

    for i in range(counter):
        counter -= 1
        reversed_list.append(list[counter])

    return reversed_list

if '__main__' == __name__:

    objects_to_reverse = [[9, 8, 7, 6, 5, 4, 3, 2, 1], ['a', 'b', 'c', 'd', 'e']]

    for i in objects_to_reverse:
        print(" >>>>>>>> ", reverse_object(i))
