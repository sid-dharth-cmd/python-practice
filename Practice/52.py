data = [(1, 5), (2, 3), (4, 1), (3, 8)]
second_element = lambda x: x[1]
for i in range(len(data)-1):
    for j in range(len(data)-1-i):
        if second_element(data[j]) > second_element(data[j+1]):
            data[j], data[j+1] = data[j+1], data[j]
print(data)



sdata = [(1, 5), (2, 3), (4, 1), (3, 8)]
sdata.sort(key = lambda x: x[-1])
print(sdata)


tdata = [(1, 5), (2, 3), (4, 1), (3, 8)]
print(sorted(tdata, key = lambda x: x[-1]))