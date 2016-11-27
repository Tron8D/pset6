#More Comfortable
def stairs(n):
    for i in range(1, n+1):
        for j in range(n-i, 0, -1):
            print(" ", end="")
        for k in range(i+1):
            print("#", end="")
        print("  ", end="")
        for k in range(i+1):
            print("#", end="")
        print("")

while (True):
    n = int(input("Number of stairs: "))
    if n >= 0 and n <= 23 :
        stairs(n)
        break