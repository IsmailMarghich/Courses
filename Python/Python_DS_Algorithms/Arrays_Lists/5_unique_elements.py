my_list = [1, 20, 30, 44, 5, 56, 57, 8, 19, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]

def uniquesearch(list):
    empty_list = []
    for i in list:
        if i in empty_list:
            print(i)
            return False
        else:
            empty_list.append(i)
    return True
print(uniquesearch(my_list))