num_pad = [[7, 8 ,9],
           [4 ,5, 6],
           [1, 2, 3],
           ["*" ,0, "#"]]
for num in num_pad:
    for numbers in num:
        print(numbers,end=" ")
    print()
