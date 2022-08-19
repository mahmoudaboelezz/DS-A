if __name__ == '__main__':
    N = int(input().strip())
    def day4(n):
        if n % 2 != 0:
            print("Weird")
        elif n % 2 == 0 and n in range(2,6):
            print("Not Weird")
        elif n % 2 == 0 and n in range(6,21):
            print("Weird")
        elif n % 2 ==0 and n >20:
            print("Not Weird")
        else:
            pass

    day4(N)