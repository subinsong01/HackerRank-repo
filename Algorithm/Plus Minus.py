#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    minus = 0
    plus = 0
    zero = 0
    
    for i in range(len(arr)):
        if arr[i] > 0 :
            plus += 1
        elif arr[i] == 0:
            zero += 1
        else :
            minus += 1
 
    return (plus / len(arr), minus / len(arr), zero / len(arr))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = plusMinus(arr)
    for value in result:
        print("{:.6f}".format(value))
