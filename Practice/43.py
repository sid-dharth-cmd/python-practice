dic = {'A': 40, 'B': 44, 'C': 35, 'D': 48, 'E': 28}
print(f"Before sorting: {dic}")
lst = list(dic)
for i in range(len(lst)):
    for j in range(len(lst)-1):
        if dic[lst[j]] > dic[lst[j+1]]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
sorted_dic = {key: dic[key] for key in lst}
print(f"Sorted dictionary: {sorted_dic}")