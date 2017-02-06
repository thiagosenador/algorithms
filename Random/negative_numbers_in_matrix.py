def negative_numbers_in_matriz(matrix):
    total_negative = 0

    for r in range(len(matrix)):
        for c in range(len(matrix[0]) - 1, -1, -1):
            if matrix[r][c] < 0:
                total_negative += c + 1
                break

    print(total_negative)


def optimal(matrix):

    r = 0
    c = len(matrix[0]) - 1
    count = 0

    while r < len(matrix) and c >= 0:
        if matrix[r][c] < 0:
            count += c + 1
            r += 1
        else:
            c -= 1

    print(count)


matrix = [[-5, -3, -1, 2], [-1, 0, 2, 3], [0, 1, 3, 4]]
# matrix = [[-5, -4, -3, -2], [-4, -3, -2, -1], [2, 3, 4, 5]]

optimal(matrix)
