def insertion_sort():
    numbers = [8, 1, 6, 7, 3, 2, 9, 4, 5]

    for i in range(1, len(numbers)):
        aux = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > aux:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = aux

    print(numbers)

insertion_sort()
