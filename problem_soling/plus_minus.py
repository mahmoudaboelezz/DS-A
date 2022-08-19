def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zeros = 0
    arrlen = len(arr)
    for i in arr:
        if i > 0 :
            positive +=1
        if i < 0:
            negative += 1
        if i == 0:
            zeros +=1 
    # format to 6 decimal places
    print(format(positive/arrlen, '.6f'))
    print(format(negative/arrlen, '.6f'))
    print(format(zeros/arrlen, '.6f'))

