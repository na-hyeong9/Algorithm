n,m = list(map(int,input().split()))
li = []
def dfs(start):
    if len(li)==m:
        print(' '.join(map(str,li)))
        return
    
    for i in range(start,n+1):
        if i not in li:
            li.append(i)
            dfs(i+1)
            li.pop()
dfs(1)