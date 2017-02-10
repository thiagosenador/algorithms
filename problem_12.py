def find_triangle_number(number):

    triangle = 0

    for i in range(1, number + 1):
        triangle += i

    return triangle


def find_number_divisors(number):

    divisors = 2

    for i in range(2, int((number / 2)) + 1):
        if number % i == 0:
            divisors += 1

    return divisors


i = 1
biggest_triangle = 0
biggest_divisors = 0

while biggest_divisors < 500:
    biggest_triangle = find_triangle_number(i)
    biggest_divisors = find_number_divisors(biggest_triangle)
    i += 1

print(biggest_triangle, biggest_divisors)
