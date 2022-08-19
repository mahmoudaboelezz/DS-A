class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        list = []
        for i in range(n+1):
            try:
                if n % i == 0:
                    list.append(int(n/i))
                    list.append(i)
            except:
                pass
        return sum(set(list))


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
