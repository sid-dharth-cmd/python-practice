n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
p = int(input("Enter third number: "))
if n > m and m > p:
    print(f"{n} is largest.")
elif m > n and m > p:
    print(f"{m} is largest.")
else:
    print(f"{p} is largest.")