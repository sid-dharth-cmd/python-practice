list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = []
odd = []
for i in list:
    even.append(i) if i % 2 == 0 else odd.append(i)
print(f"Even: {even}")
print(f"Odd: {odd}")