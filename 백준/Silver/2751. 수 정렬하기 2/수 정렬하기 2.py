import sys

ipt = sys.stdin.readline
arr = []

for i in range(int(input())):
    arr.append(int(input()))

arr = sorted(arr)
print(*arr, sep='\n')