def d(n):
    n = n + sum(map(int, str(n)))
    return n

n_self = set()

for i in range(1, 10001):
    n_self.add(d(i))
    
for j in range(1, 10001):
    if j not in n_self:
        print(j)