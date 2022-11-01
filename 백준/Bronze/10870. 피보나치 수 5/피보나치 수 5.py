N = int(input())
num1 = 0
num2 = 1
plus_num = 0

for i in range(N):
    num1 = num2
    num2 = plus_num
    plus_num = num1 + num2

print(plus_num)