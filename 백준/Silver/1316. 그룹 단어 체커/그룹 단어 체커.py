N = int(input())
group = N

for _ in range(N):
    word = input()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            continue
        elif word[i] in word[i+1:]:
            group -= 1
            break
print(group)