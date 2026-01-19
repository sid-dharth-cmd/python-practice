num = int(input("Enter a number: "))
sum = 0
for i in range (1, num):
    if num % i == 0:
        sum +=i
print(f"{num} is {'a perfect number.' if sum == num else 'not perfect number.'}")