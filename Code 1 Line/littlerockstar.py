rows = int(input("Enter num of rows: "))
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(end="  ")
    for j in range(1, 2 * i):
        print("* ", end="")
    print()
