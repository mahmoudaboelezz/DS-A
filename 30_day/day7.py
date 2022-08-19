n = int(input().strip())

arr = list(map(int, input().rstrip().split()))
for i in range(len(arr)):
    last_item = arr.pop()
    arr.insert(i, last_item)

print(' '.join(str(i) for i in arr))
# for i in arr:
#     print(i)
