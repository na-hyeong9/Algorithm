h, m = map(int, input().split())
time = int(input())

hour = (h + (m + time) // 60) % 24
minute = (m + time) % 60
print(hour, minute)