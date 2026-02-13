dic = {'A': 40, 'B': 44, 'C': 35, 'D': 48, 'E': 28}
print(dic)
rev_dic = {}
for key, value in dic.items():
    rev_dic[value] = key
print(rev_dic)


# rev_dic = {value: key for key, value in dic.items()}