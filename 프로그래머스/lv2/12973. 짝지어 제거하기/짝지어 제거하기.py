from collections import deque

def solution(s):
    temp = deque()
    for i in range(len(s)):
        if temp and temp[-1] == s[i]:
            temp.pop()
        else:
            temp.append(s[i])
    return 0 if temp else 1