def tower(n):
    total_width = 2 * n - 1
    for i in range(1, n + 1):
        current_width = 2 * i - 1
        for _ in range(3):
            print((total_width - current_width) / 2 * " " + current_width * "#" + (total_width - current_width) / 2 * " ")


def towers(data):
    pass


tower(4)
