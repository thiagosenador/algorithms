def smallest_multiple(number):

    dividers = []

    for i in range(1, number + 1):
        dividers.append(i)

    smallest = number
    hits = 0

    while True:
        for i in range(0, len(dividers)):
            if smallest % dividers[i] == 0:
                hits += 1
                if hits == number:
                    return smallest
            else:
                hits = 0
                smallest += 10
                break

print(smallest_multiple(20))
