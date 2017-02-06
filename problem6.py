def sum_square_difference(numbers):
    sum_of_squares = 0
    square_of_sum = 0

    for i in range(1, numbers + 1):
        sum_of_squares += i ** 2
        square_of_sum += i

    square_of_sum = square_of_sum ** 2

    print('sum of squares: %i' % sum_of_squares)
    print('square of sum: %i' % square_of_sum)
    print('sum square difference: %i' % (square_of_sum - sum_of_squares))

sum_square_difference(100)