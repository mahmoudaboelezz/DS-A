from statistics import median, mean


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        if mean(self.scores) >= 90 and mean(self.scores) <= 100:
            result = "O"
        elif mean(self.scores) >= 80 and mean(self.scores) < 90:
            result = "E"
        elif mean(self.scores) >= 70 and mean(self.scores) < 80:
            result = "A"
        elif mean(self.scores) >= 55 and mean(self.scores) < 70:
            result = "P"
        elif mean(self.scores) >= 40 and mean(self.scores) < 55:
            result = "D"
        else:
            result = "T"
        return result


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
