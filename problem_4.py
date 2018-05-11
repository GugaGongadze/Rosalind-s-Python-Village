def sumOfOddInts(a, b):
    sum = 0
    for number in range(a, b + 1):
        if number % 2 is 1:
            sum += number

    print(sum)


sumOfOddInts(4685, 8735)