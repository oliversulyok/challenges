#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'printTable' function below.
#
# The function accepts INTEGER n as parameter.
#

def printTable(n):
    table = []
    array = []
    for i in range(1, n + 1):
        array.append(i)
    for i in range(1, n + 1):
        modified_array = []
        for tmp in array:
            modified_array.append(i * tmp)
        table.append(modified_array)
    for row in table:
        string = ""
        separator_length = len(str(array[len(array) - 1] ** 2))
        lst_lenght = 1
        for el in row:
            if len(str(el)) > lst_lenght:
                separator_length -= 1*(len(str(el))-lst_lenght)
            lst_lenght = len(str(el))
            string += str(el)
            string += ' ' * separator_length
        print(string)


if __name__ == "__main__":
    n = int(input().strip())
    printTable(107)

