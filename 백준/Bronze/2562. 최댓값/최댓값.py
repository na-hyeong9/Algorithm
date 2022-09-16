numbers = [int(input()) for i in range(9)]
M = max(numbers)
print(M)
print(numbers.index(M) + 1)