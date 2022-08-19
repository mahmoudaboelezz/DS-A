#Write your code here
class Calculator():
    def __init__(self):
        self.result = 0
        
    def power(self,n,p):
        if n > -1 and p >-1 :
            self.result = int(n ** p)
            return self.result
        else:
            raise Exception('n and p should be non-negative')
        

 

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   