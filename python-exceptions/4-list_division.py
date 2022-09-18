#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    list_r = []
    div_t = 0
    while (i < list_length):
        try:
            div_t = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div_t = 0
        except ZeroDivisionError:
            print("division by 0")
            div_t = 0
        except IndexError:
            print("out of range")
        finally:
            list_r.append(div_t)
        i = i + 1
    return list_r
