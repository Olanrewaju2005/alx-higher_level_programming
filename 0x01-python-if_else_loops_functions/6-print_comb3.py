#!/usr/bin/python3
for first_no in range(0, 10):
    for second_no in range(first_no + 1, 10):
        if first_no == 8 and second_no == 9:
            print("{}{}".format(first_no, second_no))
        else:
            print("{}{}, ".format(first_no, second_no), end='')
