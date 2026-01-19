num = int(input("Enter a number: "))
flag = True
for i in range (2, num**0.5+1):
    if num % i == 0:
        flag = False
        break
if flag:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")