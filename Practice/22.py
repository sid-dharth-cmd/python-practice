list = []
n = int(input("Enter number of elements: "))
print("Enter number: ")
for i in range(n):
    x = int(input())
    list.append(x)
max = list[0]
smax = list[0]
for i in list:
    if i > max:
        smax, max = max, i 
print(f"Second Largest: {smax}")