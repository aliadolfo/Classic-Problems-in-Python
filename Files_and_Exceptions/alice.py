

def count_words(filename):
    try:

        with open(filename, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        print("Sorry, this file {0} does not exist.".format(filename))

    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file {filename} has about {num_words} words.".format(filename = filename, num_words = num_words))


if '__main__' == __name__:

    filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
    for filename in filenames:
        count_words(filename)
