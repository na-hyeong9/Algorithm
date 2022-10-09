N = int(input())

line = 1

bee_home = 1

while True:
    if N <= bee_home:
        print(line)
        break
    else:
        bee_home += line * 6
        line += 1