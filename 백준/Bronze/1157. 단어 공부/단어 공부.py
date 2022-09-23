word = input().upper()
word_li = list(set(word))
cnt = []

for i in word_li:
    cnt.append(word.count(i))

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(word_li[(cnt.index(max(cnt)))])