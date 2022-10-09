n = int(input())
line = 1

while n > line:
    n -= line
    line += 1
    
if line % 2 == 0:
    top = n
    bottom = line - n + 1
else:
    bottom = n
    top = line - n + 1
    
print(top, "/", bottom, sep='')