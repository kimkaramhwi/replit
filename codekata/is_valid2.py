def is_valid(string):
    my_list = ['(','{','[']
    my_list2 = [')','}',']'] 
    result = []

    for i in string:
        if i in my_list:
            result += i
        elif i in my_list2:
            if len(result) == 0:
                return False 
            if my_list.index(result[-1]) != my_list2.index(i):
                return False
            del result[-1]

    if len(result) != 0:
        return False
    return True

print(is_valid('(({}'))