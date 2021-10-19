def ms(list_1,list_2):
    new_list = list_1 + list_2
    new_list.sort()
    return new_list

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
print(ms(l_1,l_2))