#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    prim_diag = 0
    second_diag = 0

    for i in range(n):
        prim_diag = prim_diag + arr[i][i]
        second_diag = second_diag + arr[i][n-1-i]

    return abs(prim_diag - second_diag)
#
#
if __name__ == '__main__':


    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)






# sum1 = 0
# sum2 = 0
#
# for i in range(len(arr)):
#     print("arr[" + str(i) + "]["+ str(i) + "]")
#     sum1 = sum1 + arr[i][i]
#     sum2 = sum2 + arr[i][n-1]
#     n -= 1
#
# print(sum1)
# print(sum2)




# print(arr)