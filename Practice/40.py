d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
result = {}
for key in d1:
    result[key] = d1[key]
for key in d2:
    result[key] = d2[key]
print(result)

#result = d1 | d2