a = [1,2,3,4,3,2,1,5]

def lonelyinteger(a):
    list1=[]
    for i in a:
        if i in list1:
            list1.remove(i)
            continue
        list1.append(i)
    print(list1[0])
    
lonelyinteger(a)


def lonelyinteger(a):
    for i in a:
        if a.count(i) == 1:
            print(i)
            break
        
lonelyinteger(a)