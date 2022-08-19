def decimalToBinary(n):
    return bin(n).replace("0b", "")
   
# Driver code
if __name__ == '__main__':
    n = int(input().strip())
    array0 = []
    totalOnes = 0

    for i in decimalToBinary(n):
        if i == '1':
            totalOnes +=1 
        elif i == '0':
            array0.append(totalOnes)
            totalOnes = 0
            array0.append(0)

    if decimalToBinary(n)[-1] == '1':
        array0.append(totalOnes)

    print(max(array0))