# try binary search
arr = [1,3,5,8,12,34,35]
# linear search
def linear_search(arr, target):
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            print('steps:', steps)
            return i
    return 'not found'



def binary_search(arr, target):
    steps = 0
    low = 0
    high = len(arr) - 1
    while low <= high:
        steps += 1
        
        mid = (low + high) // 2
        print('mid:', mid, 'low:', low, 'high:', high)

        if arr[mid] == target:
            print('steps:', steps)
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return 'not found'

# print('linear search',end='\n')
# print(linear_search(arr, 34))
# print()
print('binary search', end='\n')
print(binary_search(arr, 34))