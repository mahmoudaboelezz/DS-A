arr = [1,3,5,7,9]

def miniMaxSum(arr):
    results = []
    topCounter = 0
    counter = 0
    tempSum = 0
    while True:
        for i in range(len(arr)):
            if len(results)== len(arr):
                break
            if counter == len(arr) -1:
                topCounter +=1
                
                results.append(tempSum)
                counter =0
                tempSum =0
            tempSum += arr[i]
            counter += 1
            
        if topCounter == len(arr):
            break
    
    print(min(results),max(results))       

miniMaxSum(arr)

import math
import os
import random
import re
import sys



def miniMaxSum(arr):
    print(sum(arr) - max(arr), sum(arr) - min(arr))
    
miniMaxSum(arr)