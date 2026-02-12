list = []
n = int(input("Enter number of elements: "))
print("Enter number: ")
for i in range(n):
    x = int(input())
    list.append(x)
result = []
for i in list:
    if i not in result:
        result.append(i)
print(result)   