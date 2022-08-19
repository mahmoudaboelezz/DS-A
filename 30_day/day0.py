""" def fizzBuzz(n):
    # Write your code here
    i = 0
    while i < n :
        i += 1
        if  i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
        

n = int(input().strip())

fizzBuzz(n) """

""" def reverse_words_order_and_swap_cases(sentence):
    words = sentence.split(' ')  
    reverse_sentence = ' '.join(reversed(words))  
    print(reverse_sentence )
    new2 = ""
    for letter in reverse_sentence:
        if letter.isupper():
            letter = letter.lower()
            new2 += letter
        else:
            letter = letter.upper()
            new2 += letter
    return new2 """

  
def numCells(grid=[]):
    i = 0
    result = 0
    list = []
    for i in range (0,20):
        try:
            print(grid[:][i])
            if grid[0][i]> grid[0][i+1] and grid[0][i] > grid[0][i-1] :
                list.append(grid[0][i])
                result += 1
        except:
            pass
    for i in range (0,20):
        try:
        
            if grid[1][i]> grid[1][i+1] and grid[1][i] > grid[1][i-1]:
                list.append(grid[1][i])
                result += 1
        except:
            pass
    for i in range (0,20):
        try:
        
            if grid[2][i]> grid[2][i+1] and grid[2][i] > grid[2][i-1] :
                list.append(grid[2][i])
                result += 1
        except:
            pass
    
    print(result,list)
grid = [[1, 2, 0,1], [4, 9, 6], [8, 0, 9]]
numCells(grid)



import collections

def insertion(*arr):
    list1 = []
    n = int(input())
    for i in arr:
        list1.append(i)
    a_list = collections.deque(list1)
    a_list.rotate(n)
    shifted_list = list(a_list)
    print(shifted_list)


insertion(input())