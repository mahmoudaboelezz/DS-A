#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Write your code here
    total = 0
    l =0
    #even case
    median = 0
    list = []
    fraud = 0
    woo = []
    for i in  range (d,len(expenditure)):
        
        if d % 2 == 0:
            for i in range(d):
                total += expenditure[i]
                median = total/d
            if expenditure[i] >= 2 * median:
                fraud += 1
                total -= expenditure[l]
                total += expenditure[i]
                median = total/d
                l += 1
            elif expenditure[i] <= 2 * round(median):
                total -= expenditure[l]
                total += expenditure[i]
                median = total/d
                l += 1
        else:
            w= 0
            for q in expenditure[w:i]:
                list.append(q)
                list.sort()
                
                if len(list) > d:

                    list.pop(0)
                w += 1
            woo = list
            list = []
            index = int((len(woo) / 2.0) - 0.50)
            median = woo[index]
            if expenditure[i] >= 2 * median:
                fraud += 1
                total -= expenditure[l]
                total += expenditure[i]
                median = total/d
                l += 1
            elif expenditure[i] <= 2 * round(median):
                total -= expenditure[l]
                total += expenditure[i]
                median = total/d
                l += 1
                

        
    return fraud
        



activityNotifications([10,20,30,40,50],3)




from bisect import bisect_left, insort_left
 
 
# def activityNotifications(expenditure, d):
#     warnings = 0
     
#     running_median = sorted(expenditure[:d])
#     for i,ele in enumerate(expenditure):
#         if i < d:
#             continue
                             
#         if d % 2 == 1:
#             median = running_median[d//2]
#         else:
#             median = (running_median[d//2 - 1] + running_median[d//2])/float(2)
             
#         if ele >= median*2:
#             warnings += 1
             
#         # remove previous element
#         del running_median[bisect_left(running_median, expenditure[i-d])]
         
#         # add new element
#         insort_left(running_median, ele)
 
#     return warnings
