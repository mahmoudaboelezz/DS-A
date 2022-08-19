def multi(number):
    for i in range(1,11):
        result = number * i
        print(f"{number} x {i} = {result}")

n = int(input())
multi(n)