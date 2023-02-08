def tower(n):
    total_width = 2 * n - 1
    for i in range(1, n + 1):
        current_width = 2 * i - 1
        for _ in range(3):
            print((total_width - current_width) // 2 * " " + current_width * "#" + (total_width - current_width) // 2 * " ")

            
def towers(data):
    max_size = max(data)
    shift = 1
    for i in range(1, max_size+1):
        for _ in range(3):
            for idx in range(len(data)):
                
                total_width = 2 * data[idx] - 1
                current_width = total_width - (max_size - (2 * i - (data[idx])))
                
                spaces = total_width//2 - (current_width - shift)

                
                if 2 * spaces > total_width:
                    print(" " * total_width + " ", end="")
                elif data[idx] == max_size and (current_width - (max_size - data[idx])) == 1 and max_size != data[-1]:
                    print(" " * (spaces)  + "#" * (current_width - (max_size - data[idx])) + " " * spaces, end="")
                elif idx + 1 == len(data):
                     print(" " * spaces  + "#" * (current_width - (max_size - data[idx])) + " " * spaces, end="")
                else:
                    print(" " * spaces  + "#" * (current_width - (max_size - data[idx])) + " " * spaces, end=" " )
            
            print()
        shift += 1
