n = int(input("Enter number of elements: "))
list = []
print("Enter elements: ", end = "")
for i in range(n):
    x = int(input())
    list.append(x)
max = list[0]
min = list[0]
for i in list:
    if i > max:
        max = i
    if i < min:
        min = i
print(f"Largest element: {max}")
print(f"Smallest element: {min}")