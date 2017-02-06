def find_factors(number):
    half = int(number / 2)

    factors = []

    for i in range(1, half + 1):
        if number % i == 0:
            factors.append(i)

    print("factors: %s" % factors)
    return factors


def is_prime(number):
    half = int(number / 2)

    if number % 2 == 0:
        return False

    for i in range(3, half + 1, 2):
        if number % i == 0:
            return False

    return True

NUMBER = 600851475143

factors = find_factors(NUMBER)

for i in range(len(factors) - 1, 0, -1):
    if is_prime(factors[i]):
        print('largest prime factor: %i' % factors[i])
        break
