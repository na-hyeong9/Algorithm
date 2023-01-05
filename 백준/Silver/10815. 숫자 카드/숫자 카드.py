import sys
n = int(sys.stdin.readline())
n_data=set(map(int,input().split()))
m = int(sys.stdin.readline())
m_data=(list(map(int,sys.stdin.readline().split())))
for i in m_data:
    if i in n_data:
        print(1, end=' ')
    else:
        print(0, end=' ')