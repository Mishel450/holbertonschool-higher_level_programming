#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    checker = []
    flag = 0
    for i in range(len(my_list)):
        for j in checker:
            if (j == my_list[i]):
                flag = 1
        if (flag == 0):
            add = add + my_list[i]
            checker.append(my_list[i])
        flag = 0
    return (add)
