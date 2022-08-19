# Bubble sort in Python

def bubbleSort(array):
    
  # loop to access each array element
  print(len(array))
  for i in range(len(array)):
    print(f'index of i {i}')
    # loop to compare array elements
    for j in range(0, len(array) - i - 1):
      print(f'index of j {j}')
      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        # temp = array[j]
        # array[j] = array[j+1]
        # array[j+1] = temp
        array[j],array[j+1] = array[j+1],array[j]


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)