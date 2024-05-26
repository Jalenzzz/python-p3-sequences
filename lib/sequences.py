#!/usr/bin/env python3

# prints empty list when length is 0
def print_fibonacci(length):
    if length <= 0:
        print([])
        return

    fibonacci_sequence = [0, 1]
    for i in range(2, length):
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)

    print(fibonacci_sequence[:length])

# print the first 10 numbers
print_fibonacci(10)