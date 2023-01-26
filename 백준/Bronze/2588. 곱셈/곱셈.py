n = int(input())
m = list(input())
x = 1
result = 0

for i in m[::-1]:
    a = int(i) * n
    sum = a * x
    result += sum
    x *= 10
    print(a)
    
print(result)