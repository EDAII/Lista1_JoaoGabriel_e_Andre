def linear_search(l, value):
    counter = 0
    for i in range(len(l)):
        counter += 1
        if value == l[i]:
            print('{} was found at {}'.format(value, i))
            return counter
    print("{} wasnt found".format(value))
    return counter
