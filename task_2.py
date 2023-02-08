def fibonacci(i):
    if i == 0 or i == 1:
        return i
    return fibonacci(i - 1) + fibonacci(i - 2)


def fibonacci_sequence(n):
    result = []
    while len(result) != n:
        for i in range(n):
            result.append(fibonacci(i))
    return result
