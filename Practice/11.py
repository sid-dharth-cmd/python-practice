n = int(input("Enter a number: "))
temp = n
sum = 0
while temp != 0:
    sum += temp % 10
    temp //= 10
print(f"Sum of the digits of {n} is {sum}")