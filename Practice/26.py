list = [34, 22, 52, 43, 98, 43, 76, 23]
for i in range(len(list)-1):
    for j in range(len(list)-1-i):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print(f"Sorted list: {list}")