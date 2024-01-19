num = [5, 4, 3, 2, 1]
num2 = []

for x in num:
    m = num.index(x)
    n = x + m
    num2.append(n)
print(num2)