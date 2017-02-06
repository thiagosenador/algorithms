def fibonacci(num):
    if num == 1:
        return 1
    if num == 2:
        return 2

    return fibonacci(num - 1) + fibonacci(num - 2)


def fibonacci_iterative():
    numbers = [1, 2]

    for i in range(2, 10):
        numbers.append(numbers[i - 1] + numbers[i - 2])

    print(numbers)


i = 1
fibo_sum = 0

fibo_result = fibonacci(i)

while fibo_result <= 4000000:
    if fibo_result % 2 == 0:
        fibo_sum += fibo_result
    i += 1

    fibo_result = fibonacci(i)

print(fibo_sum)

# fibonacci_iterative()