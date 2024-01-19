list = [1,2,"name", 3, "surname", "nickname", 4,5]
list2 = []

def find_int(lst, lst2):
    for x in lst:
        if type(x) == int:
            lst2.append(x)
    print(lst2)
find_int(list,list2)