#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx > 0 or idx > len(my_list)):
        count = 0
        for i in range(len(my_list)):
            if (count == idx):
                return (my_list[i])
            count = count + 1
            if (count == len(my_list)):
                return ("None")
    else:
        return ("None")
