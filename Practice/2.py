n = int(input("Enter a number: "))
m = int(input("Enter another number: "))
print(f"First number is {n} and second is {m}")
n = n+m
m = n-m
n = n-m
print(f"Now the first number is {n} and the second number is {m}")