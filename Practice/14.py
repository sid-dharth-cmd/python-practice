n = int(input("Enter a number: "))
flag = False
for i in range (2, int(n**0.5)+1):
    if n % i == 0:
        flag = True
        break
print(f"{n} is a prime number." if not flag else f"{n} is not a prime number.")