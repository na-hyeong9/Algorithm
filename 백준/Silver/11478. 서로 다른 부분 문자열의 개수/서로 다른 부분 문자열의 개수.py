S = input()
li = []

for i in range(len(S)):
    text = ''
    for j in range(i,len(S)):
        text += S[j]
        li.append(text)
set_li = set(li)
print(len(set_li))