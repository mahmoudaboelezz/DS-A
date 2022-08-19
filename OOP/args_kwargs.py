""" #*args can be any word like *aboelezz
# * unpacking operator take any number of inputs and deal with them as a tuples (constant values)
def sum_nums(*args):
    result = 0
    for x in args:
        result += x
    return result

print(sum_nums(1,2)) """

""" #option here called keyword arguement
def my_sum(a,b,*args, option= True):
    result=0
    if option:
        for x in args:
            result += x
        return a + b + result
    else:
        return a + b
print(my_sum(1,2,3,3,3))
print(my_sum(1,2,3,3,3,option=False)) """

""" #**kwargs takes any number of keyworad arguement "**kwargs deal with them as dictionary {key:value}"
def make_sentence(**kwargs):
    result1 = ""
    result = ""
    for x in kwargs.keys():
        result1 += x
    for x in kwargs.values():
        result += x
    return result1 , result

print(make_sentence(a="abo",b="el",c="ezz")) """

""" def human_details(**kwargs):
    for key , value in kwargs.items():
        print(f"{key} : {value}")

human_details(name="mahmoud",job="developer",age="23") """

# my_list = [1,2,3]
# print(my_list)

# print("-----------------")

# my_list = [1,2,3]
# #unpacking useing *
# print(*my_list)

def my_sum(x,y,z):
    print(x+y+z)

my_list = [1,2,3]
my_sum(*my_list)