import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a_dict = {}

for i in a:
    a_dict[i] = 1
    
m = int(input())
b = list(map(int, input().split()))

for j in b:
    try:
        print(a_dict[j])
    except KeyError:
        print(0)