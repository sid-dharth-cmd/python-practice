t = (3, 5, 9, 1, 6)
key = int(input("Enter key element: "))
index = 0
found = False
for i in t:
    if key != i:
        index += 1
    else:
        found = True
        break
print(f"Index of the element: {index}" if found else "Element not found.")