n_ = 0
max_ = 0
for i in range(10):
    n = int(input())
    n_ += n
    if 100 - max_ >= abs(100 - n_):
        max_ = n_
    else:
        continue
print(max_)