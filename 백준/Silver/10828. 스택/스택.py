import sys
N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    word = sys.stdin.readline().split()
    order = word[0]

    if order == 'push':
        stack.append(word[1])
    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    if order == 'size':
        print(len(stack))
    if order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])