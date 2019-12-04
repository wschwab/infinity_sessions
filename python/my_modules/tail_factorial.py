import sys

number = int(sys.argv[1])

def recursive_factorial(n, accumulator=1):
    print(accumulator) if n == 0 else recursive_factorial(n-1, accumulator*n)

recursive_factorial(number)
