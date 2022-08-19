n = int(input())
phonebook = dict()
i = 0
while i < n:
    name,number = input().split()
    name = name.lower()
    phonebook[name] = number
    i+=1

# for key , value in phonebook.items():
#     print(f"{key}  {value}")

inputs = [] 
input1 = input() 
try:
    while input1 != "": 
        inputs.append(input1) 
        input1 = input()   
except EOFError:
    pass
  

for i in range(len(inputs)):
    if inputs[i] in phonebook:
        print(f"{inputs[i]}={phonebook[inputs[i]]}")
    else:
        print("Not found")

