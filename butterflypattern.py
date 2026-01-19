'''
n = 5
for i in range (1, n+1):
    for j in range(1, i+1):
        print("*", end = "")
    for j in range(i+1, n+1):
        print(" ", end = "")
    for j in range (1, n-i+1):
        print(" ", end = "")
    for j in range (n-i+1, n+1):
        print("*", end = "")
    print()
for i in range (n, 0, -1):
    for j in range(0, i):
        print("*", end = "")
    for j in range(i, n):
        print(" ", end = "")
    for j in range (0, n-i):
        print(" ", end = "")
    for j in range (n-i, n):
        print("*", end = "")
    print()
'''



n = 5
for i in range (1, n+1):
    print("*"*i+" "*(2*(n-i))+"*"*i)
for i in range (n, 0, -1):
    print("*"*i+" "*(2*(n-i))+"*"*i)
print()