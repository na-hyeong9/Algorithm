def solution(my_string, overwrite_string, s):
    answer = ''
    my_str = list(my_string)
    over_str = list(overwrite_string)
    
    for i in range(len(over_str)):
        my_str[s+i] = over_str[i]
    return "".join(my_str)