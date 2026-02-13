list = []
n = int(input("Enter number of elements: "))
print("Enter number: ")
for i in range(n):
    x = int(input())
    list.append(x)
k = int(input("Enter number of position to rotate clockwise: "))
for i in range(k):
    last = list[n-1]
    for j in range(n-1, 0, -1):
        list[j] = list[j-1]
    list[0] = last
print(list)