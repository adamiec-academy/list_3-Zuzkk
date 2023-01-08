def is_perfect(number):
    sum = 0
    for divider in range(1, number):
        if number % divider == 0:
            sum += divider
    if sum == number:
        perfect = True
    else:
        perfect = False
    return perfect


def get_perfect_numbers(n):
    result = []
    number = 1
    while len(result) != n:
        for _ in range(number + 1):
            if is_perfect(number):
                result.append(number)
                number += 1
            else:
                number += 1
    return result


print(get_perfect_numbers(4))

