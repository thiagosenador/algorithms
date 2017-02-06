def palindrome(number):
    max_number = 10 ** number - 1

    max_palindrome = 0

    for i in range(max_number, 0, -1):
        for j in range(max_number, 0, -1):
            result = i * j
            result_str = str(result)
            if result_str == result_str[::-1] and result > max_palindrome:
                max_palindrome = result

    print(max_palindrome)

palindrome(3)
