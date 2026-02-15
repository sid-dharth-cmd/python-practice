def sum_avg_max(lst):
    max = lst[0]
    sum = 0
    for i in lst:
        sum += i 
        if max < i:
            max = i
    avg = sum / len(lst)
    return sum, avg, max
lst = [2, 4, 6, 8]
sum, avg, max = sum_avg_max(lst)
print(f"sum = {sum}\naverage = {avg}\nlargest number = {max}")