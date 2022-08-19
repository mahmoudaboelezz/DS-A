arr = []
for i in range(6):
    arr.append(list(map(int, input().rstrip().split())))
i = 0
o = 0
maxSeq = []
for i in range(6):
    for o in range(6):
        try:
            hourglass = arr[i][o] + arr[i][o+1] + arr[i][o+2] + arr[i+1][o+1] + arr[i+2][o] + arr[i+2][o+1] + arr[i+2][o+2]
            maxSeq.append(hourglass)
            # print(f"{arr[i][o]} {arr[i][o+1]} {arr[i][o+2]} \n {arr[i+1][o+1]} \n {arr[i+2][o]} {arr[i+2][o+1] } {arr[i+2][o+2]}")
            # print(hourglass)
        except:
            pass
print(max(maxSeq))