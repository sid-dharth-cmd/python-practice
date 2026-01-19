n = int(input("Enter number elements: "))
a, b = 0, 1
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a+b
    count=count+1
    
