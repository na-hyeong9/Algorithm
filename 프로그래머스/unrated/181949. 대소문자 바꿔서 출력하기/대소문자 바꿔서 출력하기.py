str = input()
result = ''

for i in str:
    if ord(i) >= 97:
        result += chr(ord(i)-32)
    else:
        result += chr(ord(i)+32)
print(result)
