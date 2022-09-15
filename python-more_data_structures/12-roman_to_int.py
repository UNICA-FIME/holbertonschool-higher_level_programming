#!/usr/bin/python3
def roman_to_int(roman_string):
    if (type(roman_string) is not str):
        return (None)
    sum_t = 0
    i = 0
    j = 0
    dic_rm = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_t = list(roman_string)
    new = list(map(lambda x: dic_rm[x], list_t))
    while (i < len(new) - 1):
        if (new[i] >= new[i + 1]):
            sum_t = sum_t + new[i]
            i += 1
        elif (new[i] < new[i + 1]):
            sum_t = sum_t + (new[i + 1] - new[i])
            i += 2
            j += 1
    if ((i == (len(new) - 1)) or j == 0):
        sum_t = sum_t + new[i]
    return (sum_t)
