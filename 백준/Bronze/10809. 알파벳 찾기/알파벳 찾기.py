word = input()
al = ['a', 'b', 'c' ,'d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
idx = []

for i in al:
    if i in word:
        idx.append(word.index(i))
    else:
        idx.append('-1')
print(*idx)