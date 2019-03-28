def binary_search(l: list, value):
    a = 0
    b = len(l) - 1
    counter = 0

    while(a <= b):
        m = a + (b - a) // 2
        counter += 1
        if l[m] == value:
            print('{} was found at {}'.format(value, m))
            return counter
        elif l[m] > value: b = m - 1
        else: a = m + 1 
    
    print("{} wasnt found".format(value))
    return counter
    


