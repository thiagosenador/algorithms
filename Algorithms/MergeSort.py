def mergesort(numbers):
    if len(numbers) > 1:
        middle = len(numbers) // 2

        left = numbers[0: middle]
        right = numbers[middle: len(numbers)]

        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1

numbers = [8, 1, 6, 7, 3, 2, 9, 4]
mergesort(numbers)
print(numbers)
