n = int(input())

if (n ^ n-1) & n == n:
    print("TAK")
else:
    print("NIE")