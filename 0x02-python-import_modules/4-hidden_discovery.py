#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    list_n = dir(hidden_4)
    for i in range(len(list_n)):
        if list_n[i][0] != '_':
            print(list_n[i])
