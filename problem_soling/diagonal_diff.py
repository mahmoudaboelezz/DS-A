def diagonalDifference(arr):
    # Write your code here
    left_to_right = 0
    right_to_left = 0
    for i in range(len(arr)):
        left_to_right += arr[i][i]
        right_to_left += arr[i][len(arr) - 1 - i]
        print(arr[i][len(arr) - 1 - i], arr[i][(i+1)*-1],)
    return abs(left_to_right - right_to_left)

arr = [[1,2,3],[4,8,6],[7,8,-12]]
print(diagonalDifference(arr))
