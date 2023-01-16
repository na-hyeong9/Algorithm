T = int(input())
for _ in range(T):
    # num 번째 피보나치 값
    num = int(input())
    count_zero = 1
    count_one = 0
    if num == 0:
        print(count_zero, count_one)
    else:
        for _ in range(num):
            count_zero, count_one = count_one, count_one + count_zero
        print(count_zero, count_one)