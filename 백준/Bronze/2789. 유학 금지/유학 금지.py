li = list("CAMBRIDGE")
n = input()
word = ""

for i in n:
    if not i in li:
        word += i

print(word)