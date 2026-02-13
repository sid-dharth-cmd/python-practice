list1 = [4, 5, 7, 3, 9]
list2 = [5, 8, 3, 9, 6]
common = []
for i in list1:
    if i in list2:
        common.append(i)
print(common)